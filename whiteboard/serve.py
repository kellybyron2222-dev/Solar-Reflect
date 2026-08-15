"""Serve the parent project so the drafting board can fetch and save repo files."""

from __future__ import annotations

import argparse
import json
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PORT = 8765
REVIEW_JSON = ROOT / "reviews" / "decisions.json"
REVIEW_MD = ROOT / "reviews" / "board-decisions.md"
BOARD_START = "<!-- board-review -->"
BOARD_END = "<!-- /board-review -->"
ITER_START = "<!-- iteration -->"
ITER_END = "<!-- /iteration -->"


def _safe_under_root(rel: str) -> Path | None:
    rel = rel.replace("\\", "/").lstrip("/")
    if not rel or rel.startswith("/") or ":" in rel:
        return None
    parts = Path(rel).parts
    if ".." in parts:
        return None
    path = (ROOT / rel).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        return None
    return path


def _load_store() -> dict:
    if not REVIEW_JSON.exists():
        return {"items": {}, "notes": {}}
    try:
        data = json.loads(REVIEW_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"items": {}, "notes": {}}
    data.setdefault("items", {})
    data.setdefault("notes", {})
    return data


def _extract_iteration(text: str) -> str:
    if ITER_START in text and ITER_END in text:
        return text.split(ITER_START, 1)[1].split(ITER_END, 1)[0]
    return "\n_No iteration written yet._\n"


def _render_overview(data: dict, iteration: str) -> str:
    items = list(data.get("items", {}).values())
    lines = [
        "# Board decisions",
        "",
        "Written into this repo when you Agree or Disagree on the drafting board (`python whiteboard/serve.py`). This file is what the next review pass reads.",
        "",
    ]
    disagrees = [x for x in items if (x.get("verdict") or "").lower() == "disagree"]
    if disagrees:
        lines += ["## Open disagrees", ""]
        for rec in disagrees:
            note = (rec.get("note") or "").strip() or "(no comment)"
            lines.append(
                f"- **{rec.get('file') or '?'}** — {rec.get('title') or rec.get('id')}: {note}"
            )
        lines.append("")
    by_file: dict[str, list] = {}
    for rec in items:
        by_file.setdefault(rec.get("file") or "unknown", []).append(rec)
    for file, recs in sorted(by_file.items()):
        lines += [f"## {file}", ""]
        for rec in recs:
            verdict = rec.get("verdict") or "open"
            lines.append(f"- **{verdict}** {rec.get('title') or rec.get('id')}")
            if rec.get("recommend"):
                lines.append(f"  - Recommended: {rec['recommend']}")
            if rec.get("note"):
                comment = str(rec["note"]).replace("\n", "\n    ")
                lines.append(f"  - Comment: {comment}")
            if rec.get("updated"):
                lines.append(f"  - Updated: {rec['updated']}")
        lines.append("")
    notes = data.get("notes") or {}
    for file, rec in notes.items():
        if not rec.get("notes") and not rec.get("status"):
            continue
        lines += [
            f"## File notes — {file}",
            "",
            f"- Status: {rec.get('status') or '—'}",
            "",
            rec.get("notes") or "",
            "",
        ]
    lines += [ITER_START, iteration.rstrip() + "\n", ITER_END, ""]
    return "\n".join(lines)


def _render_file_block(file: str, recs: list, iteration: str) -> str:
    rows = ["| Concept | Vote | Comment |", "|---|---|---|"]
    if not recs:
        rows.append("| — | — | No votes yet. |")
    else:
        for rec in recs:
            title = (rec.get("title") or rec.get("id") or "").replace("|", "/")
            verdict = rec.get("verdict") or "open"
            note = (rec.get("note") or "").replace("|", "/").replace("\n", " ")
            rows.append(f"| {title} | **{verdict}** | {note} |")
    return "\n".join(
        [
            BOARD_START,
            "## Board review",
            "",
            "Votes from the drafting board. Not freeze text until an iteration below is accepted.",
            "",
            *rows,
            "",
            ITER_START,
            iteration.rstrip(),
            ITER_END,
            BOARD_END,
            "",
        ]
    )


def _patch_source(file_rel: str, recs: list) -> None:
    path = _safe_under_root(file_rel)
    if path is None or not path.is_file():
        return
    if path.suffix.lower() not in {".md", ".markdown", ".txt"}:
        return
    text = path.read_text(encoding="utf-8")
    iteration = "\n_No iteration written yet._\n"
    if BOARD_START in text and BOARD_END in text:
        old = text.split(BOARD_START, 1)[1].split(BOARD_END, 1)[0]
        iteration = _extract_iteration(BOARD_START + old + BOARD_END)
        prefix = text.split(BOARD_START, 1)[0].rstrip() + "\n\n"
        suffix = text.split(BOARD_END, 1)[1].lstrip("\n")
        path.write_text(prefix + _render_file_block(file_rel, recs, iteration) + suffix, encoding="utf-8")
        return
    path.write_text(text.rstrip() + "\n\n" + _render_file_block(file_rel, recs, iteration), encoding="utf-8")


def save_store(data: dict) -> None:
    REVIEW_JSON.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    iteration = "\n_No iteration written yet._\n"
    if REVIEW_MD.exists():
        iteration = _extract_iteration(REVIEW_MD.read_text(encoding="utf-8"))
    REVIEW_MD.write_text(_render_overview(data, iteration), encoding="utf-8")
    by_file: dict[str, list] = {}
    for rec in data.get("items", {}).values():
        file = rec.get("file")
        if file:
            by_file.setdefault(file, []).append(rec)
    for file, recs in by_file.items():
        _patch_source(file, recs)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        print(fmt % args)

    def _send_json(self, code: int, payload: dict) -> None:
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        if urlparse(self.path).path.rstrip("/") == "/whiteboard/api/decisions":
            self._send_json(200, _load_store())
            return
        super().do_GET()

    def do_POST(self) -> None:
        if urlparse(self.path).path.rstrip("/") != "/whiteboard/api/decision":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length") or "0")
        if length > 2_000_000:
            self.send_error(413)
            return
        raw = self.rfile.read(length) if length else b"{}"
        try:
            body = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_error(400, "invalid json")
            return
        data = _load_store()
        incoming_items = body.get("items")
        incoming_notes = body.get("notes")
        if isinstance(incoming_items, dict):
            data["items"].update(incoming_items)
        item = body.get("item")
        if isinstance(item, dict) and item.get("id"):
            data["items"][item["id"]] = item
        if isinstance(incoming_notes, dict):
            data["notes"].update(incoming_notes)
        save_store(data)
        self._send_json(200, {"ok": True, "path": "reviews/board-decisions.md"})


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve the parent project so the drafting board can load and save repo files"
    )
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()

    socketserver.TCPServer.allow_reuse_address = True
    url = f"http://127.0.0.1:{args.port}/whiteboard/"
    with socketserver.TCPServer(("127.0.0.1", args.port), Handler) as httpd:
        print(f"Drafting board: {url}", flush=True)
        print(f"Serving files from: {ROOT}", flush=True)
        print("Agree/Disagree writes reviews/board-decisions.md", flush=True)
        print("Stop with Ctrl+C", flush=True)
        if not args.no_browser:
            threading.Thread(target=webbrowser.open, args=(url,), daemon=True).start()
        httpd.serve_forever()


if __name__ == "__main__":
    main()
