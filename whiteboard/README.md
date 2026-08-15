# Drafting board

A local review table for Markdown (and YAML/Python/HTML): typeset math, walk logic as cards, hover definitions, agree/disagree on recommended freeze actions.

Copy this **whole folder** into another repo (keep the folder name `whiteboard`, at the project root).

## Use in another project

1. Copy `whiteboard/` to the other project’s root.
2. Copy `board.config.example.json` to `board.config.json` and edit it:
   - `id` — unique string (keeps this project’s agree/disagree votes separate in the browser)
   - `library` — files to list on the left (`path` relative to the **project root**, not this folder)
   - `pack` — files loaded by **Review key files**
   - `concepts` — optional freeze cards (`id`, `file`, `heading`, `title`, `simple`, `recommend`). If empty, Review builds one card per Markdown heading.
   - `terms` — optional extra hover terms (aliases, definition, Wikipedia URL)
3. From the project root:

```text
python whiteboard/serve.py
```

4. Open http://127.0.0.1:8765/whiteboard/

Without a config file, the board still works: **Open files** / drag-and-drop, then **Review** on whatever you loaded.

**Agree / Disagree** writes into the project (not only the browser): `reviews/board-decisions.md` and a **Board review** section at the bottom of the markdown you voted on. That is what the next review pass reads. File:// mode cannot save; use `python whiteboard/serve.py`.

## Files to copy

| File | Role |
|---|---|
| `index.html` | UI |
| `styles.css` | Layout |
| `app.js` | Math, review queue, glossary |
| `serve.py` | Serves the **parent** folder so notes in the repo can be fetched |
| `board.config.json` | This project’s library and concepts (do not copy Solar Reflect’s unless you want it) |
| `board.config.example.json` | Blank template |

Do not copy Solar Reflect’s `board.config.json` into an unrelated project. Start from the example.

Built-in hover glossary (irradiance, nadir, étendue, etc.) lives in `app.js` and comes along automatically.
