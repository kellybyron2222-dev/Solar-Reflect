/** Project library, pack, and freeze cards live in board.config.json (copy the folder; edit that file). */
let LIBRARY = [];
let PACK = [];
let CONCEPTS = [];
let NOTES_KEY = "drafting-board-notes:default";
let ITEMS_KEY = "drafting-board-items:default";
let COMMENTS_KEY = "drafting-board-comments:default";
let PACK_LABEL = "Review key files";

const KATEX_OPTS = {
  delimiters: [
    { left: "$$", right: "$$", display: true },
    { left: "\\[", right: "\\]", display: true },
    { left: "$", right: "$", display: false },
    { left: "\\(", right: "\\)", display: false },
  ],
  throwOnError: false,
  ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
};

const BUILTIN_TERMS = [
  {
    id: "irradiance",
    aliases: ["peak irradiance", "irradiance"],
    def: "Power of light hitting a surface, per square metre. Here it is how bright the ground patch is, in W/m². Not the same as how it looks to the eye (that would be lux).",
    wiki: "https://en.wikipedia.org/wiki/Irradiance",
  },
  {
    id: "solar-constant",
    aliases: ["solar constant", "AM0"],
    def: "Sunlight strength just above Earth’s atmosphere: about 1361 W/m². Called AM0 (“air mass zero”) because no air has been traversed yet.",
    wiki: "https://en.wikipedia.org/wiki/Solar_constant",
  },
  {
    id: "angular-diameter",
    aliases: ["angular diameter", "angular size", "angular width"],
    def: "How wide an object looks, in degrees or radians, not kilometres. The Sun looks about half a degree across from Earth.",
    wiki: "https://en.wikipedia.org/wiki/Angular_diameter",
  },
  {
    id: "etendue",
    aliases: ["étendue", "etendue"],
    def: "A conservation law in optics: you cannot squeeze a large, spread-out source into a tiny bright spot without losses. That is why focusing does not shrink the solar image below D = h × α.",
    wiki: "https://en.wikipedia.org/wiki/%C3%89tendue",
  },
  {
    id: "terminator",
    aliases: ["terminator-nadir", "dusk/dawn", "day/night line", "terminator"],
    def: "The moving line on Earth between day and night. A satellite “over the terminator” is above twilight, not above midnight.",
    wiki: "https://en.wikipedia.org/wiki/Terminator_(solar)",
  },
  {
    id: "nadir",
    aliases: ["looking straight down", "nadir"],
    def: "The direction straight down, toward the center of the Earth. Opposite of zenith (straight up).",
    wiki: "https://en.wikipedia.org/wiki/Nadir",
  },
  {
    id: "zenith",
    aliases: ["zenith"],
    def: "Straight up from a point on the ground. “Zenith over a dark city” would mean the satellite is directly above that city.",
    wiki: "https://en.wikipedia.org/wiki/Zenith",
  },
  {
    id: "elevation",
    aliases: ["elevation cut", "elevation"],
    def: "How high the satellite sits in the sky, from the horizon (0°) to overhead (90°). We count a pass as useful while it is above 30°.",
    wiki: "https://en.wikipedia.org/wiki/Horizontal_coordinate_system",
  },
  {
    id: "specular",
    aliases: ["specular"],
    def: "Mirror-like reflection: the beam bounces at equal angles, like a looking-glass, not like a white wall that scatters light everywhere.",
    wiki: "https://en.wikipedia.org/wiki/Specular_reflection",
  },
  {
    id: "inverse-square",
    aliases: ["inverse-square"],
    def: "A small lamp’s brightness falls as 1 over distance squared because the light spreads on a sphere. That is the wrong picture here: the Sun is an extended disk, so the ground patch is an image of that disk.",
    wiki: "https://en.wikipedia.org/wiki/Inverse-square_law",
  },
  {
    id: "solar-image",
    aliases: ["solar image", "filled solar image", "ground patch", "lit patch"],
    def: "The Sun’s disk, as projected onto the ground by the mirror. It is kilometres across from low orbit. Collected watts are spread over that whole patch.",
    wiki: "https://en.wikipedia.org/wiki/Camera_obscura",
  },
  {
    id: "extended-source",
    aliases: ["extended source", "Sun as a disk"],
    def: "A source that has visible size, not a point. The Sun subtends about 0.5°, so it cannot be treated like a star-like lamp.",
    wiki: "https://en.wikipedia.org/wiki/Solid_angle",
  },
  {
    id: "fluence",
    aliases: ["fluence", "energy per pass"],
    def: "Energy delivered per square metre over a pass (J/m²). Here we approximate it as peak brightness times useful minutes — an upper bound, not a detailed light curve.",
    wiki: "https://en.wikipedia.org/wiki/Fluence",
  },
  {
    id: "umbra",
    aliases: ["umbra", "Earth’s shadow"],
    def: "The dark shadow Earth casts in space. A satellite in umbra sees no Sun. This version does not subtract that from pass time, so duration is optimistic.",
    wiki: "https://en.wikipedia.org/wiki/Umbra,_penumbra_and_antumbra",
  },
  {
    id: "leo",
    aliases: ["low Earth orbit"],
    def: "Orbits from roughly 160 to 2000 km up. Period is about 90 minutes. The satellite is moving fast, so a pass over one site is short.",
    wiki: "https://en.wikipedia.org/wiki/Low_Earth_orbit",
  },
  {
    id: "geo",
    aliases: ["geostationary", "GEO"],
    def: "An orbit at about 36,000 km that stays over one longitude. The solar image there is hundreds of kilometres wide. We only use it as a size check, not a campaign.",
    wiki: "https://en.wikipedia.org/wiki/Geostationary_orbit",
  },
  {
    id: "optical-factor",
    aliases: ["optical factor"],
    def: "A single efficiency η = mirror reflectance × atmosphere transmittance. Ideal = 1. Estimated clear sky ≈ 0.675. Do not multiply extra loss factors on top.",
    wiki: "https://en.wikipedia.org/wiki/Reflectance",
  },
  {
    id: "reflectance",
    aliases: ["reflectance"],
    def: "Fraction of sunlight the mirror actually reflects (ρ). 0.9 is a typical aluminized-film order, not a lab measurement for a specific product.",
    wiki: "https://en.wikipedia.org/wiki/Reflectance",
  },
  {
    id: "transmittance",
    aliases: ["transmittance", "clear-sky"],
    def: "Fraction of the reflected beam that survives the air on the way down (τ). 0.75 is a clear-sky, looking-straight-down estimate, not cloudy weather.",
    wiki: "https://en.wikipedia.org/wiki/Transmittance",
  },
  {
    id: "collector-incidence",
    aliases: ["collector incidence", "fold angle"],
    def: "Angle between the incoming sunlight and the mirror’s normal. At terminator-nadir the sun-to-ground turn is 90°, so a flat fold uses 45°. Not the Sun’s angle on the ground.",
    wiki: "https://en.wikipedia.org/wiki/Angle_of_incidence_(optics)",
  },
  {
    id: "shutter",
    aliases: ["orbital shutter"],
    def: "The satellite is only over the site for a few minutes. Even if the patch is bright enough, it may not last long enough. That time limit is the shutter.",
    wiki: "https://en.wikipedia.org/wiki/Orbital_period",
  },
  {
    id: "dwell",
    aliases: ["useful dwell", "dwell"],
    def: "How long the satellite stays high enough in the sky (here, above 30° elevation) on an overhead pass.",
    wiki: "https://en.wikipedia.org/wiki/Satellite_pass",
  },
  {
    id: "pv",
    aliases: ["solar panel", "solar panels", "photovoltaic"],
    def: "Devices that turn sunlight into electricity. “Weak PV” here is just a brightness bin (~50 W/m²), not a farm design.",
    wiki: "https://en.wikipedia.org/wiki/Photovoltaics",
  },
  {
    id: "air-mass",
    aliases: ["air mass"],
    def: "How much atmosphere the beam travels through. Zenith is air mass 1. We use a zenith (nadir-downlink) estimate; we do not swap in the AM1.5 solar-panel standard spectrum.",
    wiki: "https://en.wikipedia.org/wiki/Air_mass_(solar_energy)",
  },
];

let TERMS = BUILTIN_TERMS;
let TERM_BY_ID = {};
let TERM_ALIAS = [];
let TERM_RE = /(?!)/g;
let TERM_ID_FOR = {};

function rebuildTermIndex() {
  TERM_BY_ID = Object.fromEntries(TERMS.map((t) => [t.id, t]));
  TERM_ALIAS = [];
  for (const t of TERMS) {
    for (const a of t.aliases || []) TERM_ALIAS.push({ alias: a, id: t.id, n: a.length });
  }
  TERM_ALIAS.sort((a, b) => b.n - a.n);
  const escaped = TERM_ALIAS.map((a) => a.alias.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|");
  TERM_RE = escaped ? new RegExp(`\\b(${escaped})\\b`, "gi") : /(?!)/g;
  TERM_ID_FOR = {};
  for (const a of TERM_ALIAS) TERM_ID_FOR[a.alias.toLowerCase()] = a.id;
}
rebuildTermIndex();

const state = {
  mode: "read",
  current: null,
  opened: new Map(),
  served: false,
  queue: [],
  qi: 0,
  pendingOnly: true,
  packMode: false,
  comments: {},
  pendingQuote: "",
  pendingHeading: "",
  pendingAt: null,
  activeCommentId: "",
  showDone: false,
};

const $ = (id) => document.getElementById(id);

function notesStore() {
  try {
    return JSON.parse(localStorage.getItem(NOTES_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveNotesStore(obj) {
  localStorage.setItem(NOTES_KEY, JSON.stringify(obj));
}

function itemDecisions() {
  try {
    return JSON.parse(localStorage.getItem(ITEMS_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveItemDecisions(obj) {
  localStorage.setItem(ITEMS_KEY, JSON.stringify(obj));
}

async function loadDecisionsFromRepo() {
  try {
    const res = await fetch("/whiteboard/api/decisions", { cache: "no-store" });
    if (!res.ok) return;
    const data = await res.json();
    if (data.items && Object.keys(data.items).length) {
      saveItemDecisions({ ...itemDecisions(), ...data.items });
    }
    if (data.notes && Object.keys(data.notes).length) {
      saveNotesStore({ ...notesStore(), ...data.notes });
    }
  } catch {
    /* file:// or server down: browser storage only */
  }
}

async function persistDecisionsToRepo() {
  const meta = $("save-meta");
  try {
    const res = await fetch("/whiteboard/api/decision", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        items: itemDecisions(),
        notes: notesStore(),
        comments: commentsStore(),
      }),
    });
    if (meta) {
      meta.textContent = res.ok
        ? "Saved to reviews/board-decisions.md and the note."
        : "Could not save votes into the repo.";
    }
    return res.ok;
  } catch {
    if (meta) meta.textContent = "Could not save votes into the repo. Run python whiteboard/serve.py.";
    return false;
  }
}

function commentsStore() {
  try {
    return JSON.parse(localStorage.getItem(COMMENTS_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveCommentsStore(obj) {
  localStorage.setItem(COMMENTS_KEY, JSON.stringify(obj));
  state.comments = obj;
}

function commentsForFile(name) {
  const file = fileKey(name || state.current?.name || "");
  return Object.values(state.comments).filter((c) => c && fileKey(c.file) === file);
}

function isDoneComment(c) {
  return (c?.status || "open") === "resolved";
}

function openCommentsForFile(name) {
  return commentsForFile(name).filter((c) => !isDoneComment(c));
}

function doneCommentsForFile(name) {
  return commentsForFile(name)
    .filter(isDoneComment)
    .sort((a, b) => String(a.created || "").localeCompare(String(b.created || "")));
}

async function loadCommentsFromRepo() {
  try {
    const res = await fetch("/whiteboard/api/comments", { cache: "no-store" });
    if (!res.ok) return;
    const data = await res.json();
    if (data.comments && typeof data.comments === "object") {
      saveCommentsStore({ ...commentsStore(), ...data.comments });
    }
  } catch {
    state.comments = commentsStore();
  }
}

async function persistCommentToRepo(rec) {
  const meta = $("comments-meta");
  const body = rec ? { comment: rec, comments: commentsStore() } : { comments: commentsStore() };
  try {
    const res = await fetch("/whiteboard/api/comment", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (res.ok) {
      if (meta) meta.textContent = "Saved to reviews/draft-comments.md";
      return true;
    }
  } catch {
    /* fall through to the votes endpoint, which also writes comments */
  }
  const ok = await persistDecisionsToRepo();
  if (meta) {
    meta.textContent = ok
      ? "Saved to reviews/draft-comments.md"
      : "Could not save comments. Run python whiteboard/serve.py and hard-refresh.";
  }
  return ok;
}

async function deleteCommentFromRepo(id) {
  const meta = $("comments-meta");
  try {
    const res = await fetch("/whiteboard/api/comment", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ delete: id }),
    });
    if (meta) {
      meta.textContent = res.ok
        ? "Removed from reviews/draft-comments.md"
        : "Could not update comments in the repo.";
    }
    return res.ok;
  } catch {
    if (meta) meta.textContent = "Could not save comments. Run python whiteboard/serve.py.";
    return false;
  }
}

function hideCommentPop() {
  const pop = $("comment-pop");
  if (pop) pop.hidden = true;
  state.pendingQuote = "";
  state.pendingHeading = "";
  state.pendingAt = null;
}

function headingText(el) {
  if (!el) return "";
  const clone = el.cloneNode(true);
  clone.querySelectorAll(".draft-tag, .draft-ghosts").forEach((n) => n.remove());
  return (clone.textContent || "").replace(/[✓✔]/g, "").replace(/\s+/g, " ").trim();
}

function nearestHeading(node) {
  let el = node && node.nodeType === 1 ? node : node?.parentElement;
  const paper = $("paper");
  while (el && el !== paper) {
    let prev = el;
    while (prev) {
      if (/^H[1-4]$/.test(prev.tagName)) return headingText(prev);
      prev = prev.previousElementSibling;
    }
    el = el.parentElement;
  }
  return "";
}

function snippet(s, n) {
  const t = String(s || "").replace(/\s+/g, " ").trim();
  if (t.length <= n) return t;
  return t.slice(0, n - 1) + "…";
}

function cleanQuote(s) {
  return String(s || "")
    .replace(/[✓✔]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function collectQuoteNodes(root) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      const p = node.parentElement;
      if (!p || p.closest(".katex, .empty, script, .draft-tag, .draft-ghosts")) return NodeFilter.FILTER_REJECT;
      if (!node.nodeValue) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    },
  });
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  return nodes;
}

function rangeFromOffsets(nodes, start, end) {
  let pos = 0;
  let startNode;
  let startOff;
  let endNode;
  let endOff;
  for (const node of nodes) {
    const len = node.nodeValue.length;
    if (startNode == null && start < pos + len) {
      startNode = node;
      startOff = start - pos;
    }
    if (end <= pos + len) {
      endNode = node;
      endOff = end - pos;
      break;
    }
    pos += len;
  }
  if (!startNode || !endNode) return null;
  const range = document.createRange();
  range.setStart(startNode, Math.max(0, startOff));
  range.setEnd(endNode, Math.min(endNode.nodeValue.length, endOff));
  return range;
}

function quoteOffsetFromPoint(root, container, offset) {
  const nodes = collectQuoteNodes(root);
  let pos = 0;
  for (const node of nodes) {
    if (node === container) return pos + Math.max(0, Math.min(offset, node.nodeValue.length));
    pos += node.nodeValue.length;
  }
  if (container && container.nodeType === 1) {
    pos = 0;
    for (const node of nodes) {
      if (container.contains(node)) return pos;
      pos += node.nodeValue.length;
    }
  }
  return 0;
}

function phraseRegex(phrase) {
  const words = cleanQuote(phrase).split(/\s+/).filter(Boolean);
  if (!words.length) return null;
  const inner = words.map((w) => w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("\\s+");
  return new RegExp(`(?<![A-Za-z0-9])${inner}(?![A-Za-z0-9])`, "g");
}

function findPhraseRange(nodes, phrase, preferAt) {
  const re = phraseRegex(phrase);
  if (!re) return null;
  const full = nodes.map((n) => n.nodeValue).join("");
  let best = null;
  let bestDist = Infinity;
  let m;
  while ((m = re.exec(full))) {
    if (preferAt == null) {
      return rangeFromOffsets(nodes, m.index, m.index + m[0].length);
    }
    const dist = Math.abs(m.index - preferAt);
    if (dist < bestDist) {
      best = m;
      bestDist = dist;
    }
  }
  if (!best) return null;
  return rangeFromOffsets(nodes, best.index, best.index + best[0].length);
}

function findQuoteRange(root, quote, preferAt) {
  const nodes = collectQuoteNodes(root);
  const cleaned = cleanQuote(quote);
  const exact = findPhraseRange(nodes, cleaned, preferAt);
  if (exact) return exact;
  const words = cleaned.split(/\s+/).filter(Boolean);
  if (!words.length) return null;
  const minLen = words.length === 1 ? 1 : Math.min(4, words.length);
  for (let len = words.length; len >= minLen; len--) {
    for (let i = 0; i + len <= words.length; i++) {
      const range = findPhraseRange(nodes, words.slice(i, i + len).join(" "), preferAt);
      if (range) return range;
    }
  }
  return null;
}

function wrapTextRange(range, id, extraClass) {
  if (!range || range.collapsed) return null;
  const ancestor = range.commonAncestorContainer;
  const root = ancestor.nodeType === 1 ? ancestor : ancestor.parentElement;
  if (!root) return null;
  const nodes = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (!node.nodeValue) return NodeFilter.FILTER_REJECT;
      if (node.parentElement?.closest(".katex, .draft-tag, .draft-ghosts, .empty")) return NodeFilter.FILTER_REJECT;
      return range.intersectsNode(node) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    },
  });
  while (walker.nextNode()) nodes.push(walker.currentNode);
  let lastMark = null;
  for (let i = nodes.length - 1; i >= 0; i--) {
    const node = nodes[i];
    let from = 0;
    let to = node.nodeValue.length;
    if (node === range.startContainer) from = range.startOffset;
    if (node === range.endContainer) to = range.endOffset;
    if (from > to) [from, to] = [to, from];
    if (from === to) continue;
    let piece = node;
    if (to < piece.nodeValue.length) piece.splitText(to);
    if (from > 0) piece = piece.splitText(from);
    if (piece.parentElement?.closest(".draft-tag, .draft-ghosts, .katex")) continue;
    const mark = document.createElement("mark");
    mark.className = extraClass ? `draft-hl ${extraClass}` : "draft-hl";
    mark.dataset.commentId = id;
    piece.parentNode.insertBefore(mark, piece);
    mark.appendChild(piece);
    lastMark = mark;
  }
  return lastMark;
}

function wrapQuote(root, rec, extraClass) {
  const range = findQuoteRange(root, rec.quote, rec.at);
  if (!range) return false;
  return !!wrapTextRange(range, rec.id, extraClass);
}

function findHeadingEl(root, heading) {
  const want = cleanQuote(heading);
  if (!want) return null;
  const heads = [...root.querySelectorAll("h1, h2, h3, h4")];
  const exact = heads.find((h) => headingText(h) === want);
  if (exact) return exact;
  return (
    heads.find((h) => {
      const t = headingText(h);
      return t.includes(want) || want.includes(t);
    }) || null
  );
}

function makeCommentTag(rec, label, extraClass) {
  const tag = document.createElement("button");
  tag.type = "button";
  tag.className = extraClass ? `draft-tag ${extraClass}` : "draft-tag";
  tag.dataset.commentId = rec.id;
  tag.textContent = label;
  const where = rec.heading ? `Under “${snippet(rec.heading, 60)}”` : "";
  tag.title = [isDoneComment(rec) ? "Done" : "Comment", `Originally: “${snippet(rec.quote, 90)}”`, rec.note, where]
    .filter(Boolean)
    .join("\n");
  return tag;
}

function clearHighlights(paper) {
  paper.querySelectorAll(".draft-tag, .draft-ghosts").forEach((el) => el.remove());
  paper.querySelectorAll("mark.draft-hl").forEach((el) => {
    const parent = el.parentNode;
    if (!parent) return;
    while (el.firstChild) parent.insertBefore(el.firstChild, el);
    parent.removeChild(el);
    parent.normalize();
  });
}

function orderedComments() {
  if (!state.current) return [];
  const recs = openCommentsForFile(state.current.name);
  const byId = Object.fromEntries(recs.map((r) => [r.id, r]));
  const seen = [];
  $("paper")
    ?.querySelectorAll("mark.draft-hl:not(.done)")
    .forEach((m) => {
      const id = m.dataset.commentId;
      if (id && byId[id] && !seen.includes(id)) seen.push(id);
    });
  return [...seen.map((id) => byId[id]), ...recs.filter((r) => !seen.includes(r.id))];
}

function placeCommentTags() {
  const paper = $("paper");
  if (!paper) return;
  paper.querySelectorAll(".draft-tag, .draft-ghosts").forEach((el) => el.remove());
  orderedComments().forEach((rec, i) => {
    const marks = paper.querySelectorAll(`mark.draft-hl:not(.done)[data-comment-id="${rec.id}"]`);
    const last = marks[marks.length - 1];
    if (!last) return;
    last.after(makeCommentTag(rec, String(i + 1)));
  });
  doneCommentsForFile(state.current?.name).forEach((rec) => {
    const marks = paper.querySelectorAll(`mark.draft-hl.done[data-comment-id="${rec.id}"]`);
    const last = marks[marks.length - 1];
    if (!last) return;
    last.after(makeCommentTag(rec, "✓", "done"));
  });
}

function placeDoneGhosts() {
  const paper = $("paper");
  if (!paper || !state.current) return;
  const grouped = new Map();
  doneCommentsForFile(state.current.name).forEach((rec) => {
    if (paper.querySelector(`mark.draft-hl[data-comment-id="${rec.id}"]`)) return;
    const host = findHeadingEl(paper, rec.heading) || paper.querySelector("h1, h2, h3");
    if (!host) return;
    const list = grouped.get(host) || [];
    list.push(rec);
    grouped.set(host, list);
  });
  grouped.forEach((recs, host) => {
    const wrap = document.createElement("span");
    wrap.className = "draft-ghosts";
    wrap.setAttribute("aria-label", "Completed comments that applied near this heading");
    recs.forEach((rec) => wrap.appendChild(makeCommentTag(rec, "✓", "done ghost")));
    host.insertAdjacentElement("afterend", wrap);
  });
}

function applyCommentHighlights() {
  const paper = $("paper");
  if (!paper || !state.current || state.mode === "review") return;
  clearHighlights(paper);
  openCommentsForFile(state.current.name).forEach((rec) => wrapQuote(paper, rec));
  doneCommentsForFile(state.current.name).forEach((rec) => wrapQuote(paper, rec, "done"));
  placeCommentTags();
  placeDoneGhosts();
  if (state.activeCommentId) {
    paper.querySelectorAll(`[data-comment-id="${state.activeCommentId}"]`).forEach((el) => el.classList.add("on"));
  }
}

function commentLocationKind(id) {
  const paper = $("paper");
  if (paper?.querySelector(`mark.draft-hl[data-comment-id="${id}"]`)) return "quote";
  if (paper?.querySelector(`.draft-tag[data-comment-id="${id}"]`)) return "heading";
  return "none";
}

function commentCardHtml(rec, i, { done = false } = {}) {
  const on = rec.id === state.activeCommentId ? "on" : "";
  const loc = commentLocationKind(rec.id);
  const locLabel =
    loc === "quote"
      ? rec.heading || ""
      : loc === "heading"
        ? `${rec.heading || "This section"} · wording moved`
        : rec.heading || "";
  const note =
    !done || rec.id === state.activeCommentId
      ? `<p class="note">${escapeHtml(rec.note || "")}</p>`
      : "";
  const actions = done
    ? `<button type="button" class="act" data-reopen="${escapeHtml(rec.id)}">Reopen</button>
       <button type="button" class="del" data-del="${escapeHtml(rec.id)}">Remove</button>`
    : `<button type="button" class="act" data-done="${escapeHtml(rec.id)}">Done</button>
       <button type="button" class="del" data-del="${escapeHtml(rec.id)}">Remove</button>`;
  const num = done ? "✓" : String(i + 1);
  return `<div class="comment-card ${done ? "done" : ""} ${on}" data-cid="${escapeHtml(rec.id)}">
    <p class="quote"><span class="num${done ? " done" : ""}">${num}</span>${escapeHtml(snippet(rec.quote, 110))}</p>
    ${note}
    <div class="row">
      <span class="quiet">${escapeHtml(locLabel)}</span>
      <span class="card-actions">${actions}</span>
    </div>
  </div>`;
}

function bindCommentCards(root) {
  root.querySelectorAll(".comment-card").forEach((card) => {
    card.addEventListener("click", (e) => {
      if (e.target.closest("[data-del], [data-done], [data-reopen]")) return;
      focusComment(card.dataset.cid);
    });
  });
  root.querySelectorAll("[data-del]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      removeComment(btn.dataset.del);
    });
  });
  root.querySelectorAll("[data-done]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      setCommentStatus(btn.dataset.done, "resolved");
    });
  });
  root.querySelectorAll("[data-reopen]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      setCommentStatus(btn.dataset.reopen, "open");
    });
  });
}

function paintComments() {
  const list = $("comments-list");
  const meta = $("comments-meta");
  if (!list) return;
  if (!state.current) {
    list.innerHTML = "";
    if (meta) meta.textContent = "Select a passage in the article to comment.";
    return;
  }
  const recs = orderedComments();
  const done = doneCommentsForFile(state.current.name);
  if (!recs.length && !done.length) {
    list.innerHTML = `<p class="quiet">None yet. Highlight text in the article.</p>`;
    if (meta) meta.textContent = "Select a passage in the article to comment.";
    return;
  }
  const openBit = recs.length ? `${recs.length} open` : "0 open";
  const doneBit = done.length ? `${done.length} done` : "";
  if (meta) {
    meta.textContent = [openBit, doneBit, "saved to reviews/draft-comments.md"].filter(Boolean).join(" · ");
  }
  const openHtml = recs.length
    ? recs.map((rec, i) => commentCardHtml(rec, i)).join("")
    : `<p class="quiet">No open comments. Highlight text to add one.</p>`;
  const doneOpen = state.showDone || (state.activeCommentId && done.some((c) => c.id === state.activeCommentId));
  const doneHtml = done.length
    ? `<details class="done-block" ${doneOpen ? "open" : ""}>
        <summary>Done · ${done.length}</summary>
        ${done.map((rec, i) => commentCardHtml(rec, i, { done: true })).join("")}
      </details>`
    : "";
  list.innerHTML = openHtml + doneHtml;
  const details = list.querySelector(".done-block");
  details?.addEventListener("toggle", () => {
    state.showDone = details.open;
  });
  bindCommentCards(list);
}

function focusComment(id) {
  const rec = state.comments[id];
  if (rec && isDoneComment(rec)) state.showDone = true;
  state.activeCommentId = id;
  paintComments();
  const paper = $("paper");
  paper?.querySelectorAll("mark.draft-hl, .draft-tag").forEach((el) => {
    el.classList.toggle("on", el.dataset.commentId === id);
  });
  const mark = paper?.querySelector(`mark.draft-hl[data-comment-id="${id}"]`);
  const tag = paper?.querySelector(`.draft-tag[data-comment-id="${id}"]`);
  (mark || tag)?.scrollIntoView({
    behavior: "smooth",
    block: "center",
  });
}

async function setCommentStatus(id, status) {
  const all = { ...state.comments };
  const rec = all[id];
  if (!rec) return;
  rec.status = status;
  if (status === "resolved") rec.resolvedAt = stamp();
  else delete rec.resolvedAt;
  saveCommentsStore(all);
  if (status === "resolved") state.showDone = true;
  await persistCommentToRepo(rec);
  applyCommentHighlights();
  paintComments();
}

async function removeComment(id) {
  const all = { ...state.comments };
  delete all[id];
  saveCommentsStore(all);
  if (state.activeCommentId === id) state.activeCommentId = "";
  await deleteCommentFromRepo(id);
  applyCommentHighlights();
  paintComments();
}

function placeCommentPop(range) {
  const pop = $("comment-pop");
  if (!pop) return;
  const rects = range.getClientRects();
  const rect = rects[rects.length - 1] || range.getBoundingClientRect();
  pop.hidden = false;
  const w = pop.offsetWidth || 360;
  const h = pop.offsetHeight || 220;
  let left = rect.left;
  let top = rect.bottom + 8;
  if (left + w > window.innerWidth - 12) left = window.innerWidth - w - 12;
  if (left < 12) left = 12;
  if (top + h > window.innerHeight - 12) top = Math.max(12, rect.top - h - 8);
  pop.style.left = `${left}px`;
  pop.style.top = `${top}px`;
}

function openCommentComposer() {
  if (state.mode === "review" || !state.current) return;
  const sel = window.getSelection();
  if (!sel || sel.isCollapsed || !sel.rangeCount) return;
  const range = sel.getRangeAt(0);
  const paper = $("paper");
  if (!paper || !paper.contains(range.commonAncestorContainer)) return;
  const quote = cleanQuote(sel.toString());
  if (quote.length < 2) return;
  state.pendingQuote = quote;
  state.pendingHeading = nearestHeading(range.startContainer);
  state.pendingAt = quoteOffsetFromPoint(paper, range.startContainer, range.startOffset);
  $("comment-quote").textContent = snippet(quote, 280);
  $("comment-body").value = "";
  const popMeta = $("comment-pop-meta");
  if (popMeta) popMeta.textContent = state.pendingHeading || "";
  placeCommentPop(range);
  $("comment-body")?.focus();
}

async function saveCommentFromPop() {
  const note = ($("comment-body")?.value || "").trim();
  const quote = state.pendingQuote;
  if (!quote || !state.current) return;
  if (!note) {
    $("comment-body")?.focus();
    return;
  }
  const rec = {
    id: hashId([state.current.name, quote, stamp(), String(Math.random())]),
    file: fileKey(state.current.name),
    quote,
    heading: state.pendingHeading,
    at: state.pendingAt,
    note,
    created: stamp(),
    status: "open",
  };
  const all = { ...state.comments, [rec.id]: rec };
  saveCommentsStore(all);
  await persistCommentToRepo(rec);
  hideCommentPop();
  window.getSelection()?.removeAllRanges();
  state.activeCommentId = rec.id;
  if (state.current) showFile(state.current);
  else {
    applyCommentHighlights();
    paintComments();
  }
}

function bindCommentUi() {
  const drop = $("drop");
  drop?.addEventListener("mouseup", (e) => {
    if (state.mode === "review") return;
    if (e.target.closest?.("#comment-pop, #term-pop, textarea, input, button, mark.draft-hl, .draft-tag, .draft-ghosts")) return;
    window.setTimeout(openCommentComposer, 0);
  });
  $("comment-save")?.addEventListener("click", () => saveCommentFromPop());
  $("comment-cancel")?.addEventListener("click", hideCommentPop);
  $("comment-body")?.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      saveCommentFromPop();
    }
    if (e.key === "Escape") hideCommentPop();
  });
  document.addEventListener("mousedown", (e) => {
    const pop = $("comment-pop");
    if (!pop || pop.hidden) return;
    if (pop.contains(e.target)) return;
    if ($("paper")?.contains(e.target) && window.getSelection() && !window.getSelection().isCollapsed) return;
    hideCommentPop();
  });
  $("paper")?.addEventListener("click", (e) => {
    const hit = e.target.closest?.("mark.draft-hl, .draft-tag");
    if (!hit) return;
    e.preventDefault();
    focusComment(hit.dataset.commentId);
  });
}

function hashId(parts) {
  const s = parts.join("|");
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return (h >>> 0).toString(36);
}

function fileKey(name) {
  return name.replace(/\\/g, "/");
}

function protectFences(md, fn) {
  const fences = [];
  const masked = md.replace(/```[\s\S]*?```/g, (m) => {
    fences.push(m);
    return `\0FENCE${fences.length - 1}\0`;
  });
  return fn(masked).replace(/\0FENCE(\d+)\0/g, (_, n) => fences[Number(n)]);
}

function protectImages(md, fn) {
  const imgs = [];
  const masked = md.replace(/!\[[^\]]*\]\([^)]+\)/g, (m) => {
    imgs.push(m);
    return `\0IMG${imgs.length - 1}\0`;
  });
  return fn(masked).replace(/\0IMG(\d+)\0/g, (_, n) => imgs[Number(n)]);
}

function latexToDollar(md) {
  return protectImages(md, (s) =>
    protectFences(s, (t) =>
      t
        .replace(/\\\[([\s\S]*?)\\\]/g, (_, body) => `\n\n$$\n${body.trim()}\n$$\n\n`)
        .replace(/\\\(([\s\S]*?)\\\)/g, (_, body) => `$${body}$`)
    )
  );
}

function repoAssetUrl(src) {
  if (/^(https?:|data:|\/|#)/i.test(src)) return src;
  const rel = src.replace(/^\.\//, "").replace(/^\/+/, "");
  return "/" + rel.split("/").map(encodeURIComponent).join("/");
}

function renderMarkdown(md) {
  const prepared = latexToDollar(md);
  const math = [];
  const masked = prepared.replace(/\$\$[\s\S]+?\$\$|\$[^$]+\$/g, (m) => {
    math.push(m);
    return `@@MATH${math.length - 1}@@`;
  });
  let html = marked.parse(masked, { gfm: true, breaks: false });
  html = html.replace(/@@MATH(\d+)@@/g, (_, n) => math[Number(n)]);
  html = html.replace(/<img([^>]*?)src="([^"]+)"([^>]*)>/g, (_, pre, src, post) => {
    const url = repoAssetUrl(src);
    return `<img${pre}src="${url}"${post}>`;
  });
  html = html.replace(/<p>(<img\b[\s\S]*?>)<\/p>/g, `<figure class="board-fig">$1</figure>`);
  return html;
}

function extractDisplayMath(md) {
  const out = [];
  const src = latexToDollar(md);
  const re = /\$\$([\s\S]*?)\$\$/g;
  let m;
  while ((m = re.exec(src))) {
    const tex = m[1].trim();
    if (tex) out.push(tex);
  }
  return out;
}

function typeset(el) {
  if (window.renderMathInElement) renderMathInElement(el, KATEX_OPTS);
}

function decorateTerms(root) {
  if (!root) return;
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      const p = node.parentElement;
      if (!p) return NodeFilter.FILTER_REJECT;
      if (p.closest(".katex, .term, a, code, pre, script, button, textarea")) {
        return NodeFilter.FILTER_REJECT;
      }
      if (!node.nodeValue || !TERM_RE.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
      TERM_RE.lastIndex = 0;
      return NodeFilter.FILTER_ACCEPT;
    },
  });
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  for (const node of nodes) {
    const text = node.nodeValue;
    TERM_RE.lastIndex = 0;
    const frag = document.createDocumentFragment();
    let last = 0;
    let m;
    while ((m = TERM_RE.exec(text))) {
      if (m.index > last) frag.appendChild(document.createTextNode(text.slice(last, m.index)));
      const span = document.createElement("span");
      span.className = "term";
      span.dataset.term = TERM_ID_FOR[m[0].toLowerCase()] || "";
      span.textContent = m[0];
      frag.appendChild(span);
      last = m.index + m[0].length;
    }
    if (last < text.length) frag.appendChild(document.createTextNode(text.slice(last)));
    node.parentNode.replaceChild(frag, node);
  }
}

let termHideTimer = 0;
function bindTermPop() {
  const pop = $("term-pop");
  if (!pop) return;
  document.body.addEventListener("mouseover", (e) => {
    const el = e.target.closest?.(".term");
    if (!el || !el.dataset.term) return;
    if (window.getSelection() && !window.getSelection().isCollapsed) return;
    const t = TERM_BY_ID[el.dataset.term];
    if (!t) return;
    clearTimeout(termHideTimer);
    $("term-pop-word").textContent = t.aliases[0];
    $("term-pop-def").textContent = t.def;
    const a = $("term-pop-wiki");
    if (t.wiki) {
      a.href = t.wiki;
      a.hidden = false;
    } else {
      a.hidden = true;
    }
    pop.hidden = false;
    const r = el.getBoundingClientRect();
    let left = r.left;
    let top = r.bottom + 8;
    pop.style.left = `${Math.min(left, window.innerWidth - 360)}px`;
    pop.style.top = `${top}px`;
    requestAnimationFrame(() => {
      const box = pop.getBoundingClientRect();
      if (box.bottom > window.innerHeight - 8) {
        pop.style.top = `${Math.max(8, r.top - box.height - 8)}px`;
      }
    });
  });
  document.body.addEventListener("mouseout", (e) => {
    const el = e.target.closest?.(".term");
    if (!el) return;
    if (window.getSelection() && !window.getSelection().isCollapsed) return;
    const to = e.relatedTarget;
    if (to && (pop.contains(to) || to.closest?.(".term"))) return;
    termHideTimer = setTimeout(() => {
      pop.hidden = true;
    }, 180);
  });
  pop.addEventListener("mouseenter", () => clearTimeout(termHideTimer));
  pop.addEventListener("mouseleave", () => {
    pop.hidden = true;
  });
}

function splitSections(md) {
  const lines = md.replace(/\r\n/g, "\n").split("\n");
  const sections = [];
  let current = { title: "Preamble", level: 1, body: [] };
  for (const line of lines) {
    const h = /^(#{1,3})\s+(.+?)\s*$/.exec(line);
    if (h) {
      if (current.body.length || sections.length) sections.push(current);
      current = { title: h[2].replace(/\\/g, ""), level: h[1].length, body: [] };
    } else {
      current.body.push(line);
    }
  }
  sections.push(current);
  return sections.filter((s) => s.body.join("\n").trim() || s.title !== "Preamble");
}

function plainFromTex(tex) {
  return tex
    .replace(/\\mathrm\{([^}]+)\}/g, "$1")
    .replace(/\\text\{([^}]+)\}/g, "$1")
    .replace(/\\mathrm/g, "")
    .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, "($1)/($2)")
    .replace(/\\qquad/g, "    ")
    .replace(/\\,|\\;|\\!/g, " ")
    .replace(/\\left|\\right|\\!|\\,/g, "")
    .replace(/\\arccos/g, "arccos")
    .replace(/\\cos/g, "cos")
    .replace(/\\sin/g, "sin")
    .replace(/\\pi/g, "pi")
    .replace(/\\mu/g, "mu")
    .replace(/\\eta/g, "eta")
    .replace(/\\gamma/g, "gamma")
    .replace(/\\varepsilon/g, "epsilon")
    .replace(/\\alpha/g, "alpha")
    .replace(/\\theta/g, "theta")
    .replace(/_\{([^}]+)\}/g, "_$1")
    .replace(/\^{([^}]+)}/g, "^$1")
    .replace(/\\sqrt\{([^}]+)\}/g, "sqrt($1)")
    .replace(/\\big|\\!/g, "")
    .replace(/[{}]/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function extOf(name) {
  const i = name.lastIndexOf(".");
  return i >= 0 ? name.slice(i + 1).toLowerCase() : "";
}

function renderYaml(text) {
  try {
    const data = jsyaml.load(text);
    if (data && typeof data === "object" && !Array.isArray(data)) {
      const rows = Object.entries(data)
        .map(([k, v]) => {
          if (v && typeof v === "object" && "value" in v) {
            return `<tr><td><code>${k}</code></td><td>${v.value}</td><td>${v.unit || ""}</td><td>${v.class || ""}</td><td>${v.source || ""}</td></tr>`;
          }
          return `<tr><td><code>${k}</code></td><td colspan="4">${JSON.stringify(v)}</td></tr>`;
        })
        .join("");
      return `<h1>Constants</h1><table><thead><tr><th>Key</th><th>Value</th><th>Unit</th><th>Class</th><th>Source</th></tr></thead><tbody>${rows}</tbody></table><h2>Source</h2><pre>${escapeHtml(text)}</pre>`;
    }
  } catch {
    /* fall through */
  }
  return `<pre>${escapeHtml(text)}</pre>`;
}

function escapeHtml(s) {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderSource(name, text) {
  const ext = extOf(name);
  if (ext === "md" || ext === "markdown" || ext === "txt") return renderMarkdown(text);
  if (ext === "yaml" || ext === "yml") return renderYaml(text);
  if (ext === "html" || ext === "htm") {
    if (state.served && name.includes("/")) {
      return `<iframe title="${escapeHtml(name)}" src="../${encodeURI(name)}" style="width:100%;min-height:70vh;border:1px solid var(--rule);background:#fff"></iframe>`;
    }
    return `<p class="quiet">HTML file. For the typeset model note, run the local server and pick it from the library.</p>
      <iframe title="${escapeHtml(name)}" srcdoc="${escapeHtml(text).replace(/"/g, "&quot;")}" style="width:100%;min-height:70vh;border:1px solid var(--rule);background:#fff"></iframe>`;
  }
  return `<h1>${escapeHtml(name)}</h1><pre>${escapeHtml(text)}</pre>`;
}

function logicHtml(name, text) {
  const ext = extOf(name);
  if (ext !== "md" && ext !== "markdown") {
    return `<p class="quiet">Logic view is for markdown notes. Switch to Read for this file.</p>${renderSource(name, text)}`;
  }
  const sections = splitSections(text);
  return sections
    .map((sec, i) => {
      const body = sec.body.join("\n");
      const eqs = extractDisplayMath(body);
      const prose = body
        .replace(/\$\$[\s\S]*?\$\$/g, "")
        .replace(/\\\[[\s\S]*?\\\]/g, "");
      const eqBlocks = eqs
        .map(
          (tex) =>
            `<div class="eq">$$${tex}$$</div><p class="plain">${escapeHtml(plainFromTex(tex))}</p>`
        )
        .join("");
      return `<article class="logic-card" id="sec-${i}">
        <div class="step">Step ${i + 1}</div>
        <h3>${escapeHtml(sec.title)}</h3>
        ${eqBlocks}
        <div class="prose">${renderMarkdown(prose)}</div>
      </article>`;
    })
    .join("");
}

function stripInline(s) {
  return String(s || "")
    .replace(/\$\$[\s\S]*?\$\$/g, "")
    .replace(/\$[^$]+\$/g, "")
    .replace(/\\\([^)]*\\\)/g, "")
    .replace(/[*_`]/g, "")
    .replace(/\\[a-zA-Z]+\{([^}]*)\}/g, "$1")
    .replace(/\\/g, "")
    .replace(/\s+/g, " ")
    .trim();
}

function normHead(s) {
  return stripInline(s)
    .toLowerCase()
    .replace(/^\d+\.\s*/, "")
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function sectionText(md, headingHint) {
  const want = normHead(String(headingHint).replace(/^#+\s*/, ""));
  const sections = splitSections(md);
  const hit = sections.find((s) => {
    const have = normHead(s.title);
    return have === want || have.includes(want) || want.includes(have);
  });
  if (!hit) return md.trim().slice(0, 4000);
  return `## ${hit.title}\n\n${hit.body.join("\n")}`;
}

function generateItems(file, text) {
  const named = CONCEPTS.filter((c) => fileKey(c.file) === fileKey(file)).map((c) => ({
    id: `concept:${c.id}`,
    file,
    kind: "concept",
    title: c.title,
    decide: c.decide,
    recommend: c.recommend,
    simple: c.simple,
    body: sectionText(text, c.heading),
    tex: "",
  }));
  if (named.length) return named;

  const ext = extOf(file);
  if (ext === "yaml" || ext === "yml") {
    return [
      {
        id: `concept:${file}:constants`,
        file,
        kind: "concept",
        title: "Constants",
        decide: "Are these values the right freeze for this file?",
        recommend: "Keep these constants as written.",
        body: text,
        tex: "",
      },
    ];
  }
  if (ext !== "md" && ext !== "markdown" && ext !== "txt") return [];
  return generateMdItems(file, String(text).replace(/\r\n/g, "\n"));
}

function generateMdItems(file, md) {
  return splitSections(md)
    .filter((s) => {
      const t = normHead(s.title);
      if (/readable formulas|status|preamble/.test(t)) return false;
      return s.body.join("\n").trim().length > 80;
    })
    .map((s) => ({
      id: `concept:${file}:${hashId([file, s.title])}`,
      file,
      kind: "concept",
      title: stripInline(s.title),
      decide: "Does this section belong in the freeze as written?",
      recommend: "Keep this section as written.",
      simple: "",
      body: `## ${s.title}\n\n${s.body.join("\n")}`,
      tex: "",
    }));
}

function setQueue(items, packMode) {
  state.queue = items;
  state.packMode = !!packMode;
  const dec = itemDecisions();
  const pending = items.findIndex((it) => !dec[it.id]?.verdict);
  state.qi = pending >= 0 ? pending : 0;
}

function currentItem() {
  return state.queue[state.qi] || null;
}

function queueStats() {
  const dec = itemDecisions();
  const done = state.queue.filter((it) => dec[it.id]?.verdict).length;
  return { done, total: state.queue.length };
}

function stamp() {
  return new Date().toISOString().slice(0, 16).replace("T", " ");
}

function setVerdict(verdict, advance) {
  const it = currentItem();
  if (!it) return;
  const all = itemDecisions();
  const note = $("item-note")?.value || "";
  if (verdict === "disagree" && !note.trim() && !(all[it.id] && all[it.id].note)) {
    all[it.id] = {
      verdict: "disagree",
      note: "",
      updated: stamp(),
      title: it.title,
      file: it.file,
      kind: it.kind,
      recommend: it.recommend || "",
    };
    saveItemDecisions(all);
    persistDecisionsToRepo();
    renderReview();
    $("item-note")?.focus();
    return;
  }
  all[it.id] = {
    verdict,
    note,
    updated: stamp(),
    title: it.title,
    file: it.file,
    kind: it.kind,
    recommend: it.recommend || "",
  };
  saveItemDecisions(all);
  persistDecisionsToRepo();
  if (advance !== false) goNextPending();
  else renderReview();
}

function goNextPending() {
  const dec = itemDecisions();
  for (let i = state.qi + 1; i < state.queue.length; i++) {
    if (!state.pendingOnly || !dec[state.queue[i].id]?.verdict) {
      state.qi = i;
      renderReview();
      return;
    }
  }
  for (let i = 0; i < state.queue.length; i++) {
    if (!dec[state.queue[i].id]?.verdict) {
      state.qi = i;
      renderReview();
      return;
    }
  }
  renderReview();
}

function goPrev() {
  if (state.qi > 0) state.qi -= 1;
  renderReview();
}

function goNext() {
  if (state.qi < state.queue.length - 1) state.qi += 1;
  renderReview();
}

function setReviewChrome(on) {
  document.querySelector(".desk")?.classList.toggle("reviewing", on);
  $("outline").classList.toggle("hidden", on);
  $("item-list").classList.toggle("hidden", !on);
  $("rail-read").classList.toggle("hidden", on);
  $("rail-review").classList.toggle("hidden", !on);
  $("list-heading").textContent = on ? "Concepts" : "On this page";
  if (on) hideCommentPop();
}

function renderReview() {
  setReviewChrome(true);
  const it = currentItem();
  const { done, total } = queueStats();
  $("queue-progress").textContent = total
    ? `${done} of ${total} decided · item ${state.qi + 1}`
    : "No key items in this file.";
  const dec = itemDecisions();

  $("item-list").innerHTML =
    `<label class="filter-row"><input type="checkbox" id="pending-only" ${state.pendingOnly ? "checked" : ""}> Pending first</label>` +
    state.queue
      .map((item, i) => {
        const v = dec[item.id]?.verdict || "";
        if (state.pendingOnly && v && item !== it) return "";
        const on = i === state.qi ? "on" : "";
        return `<button type="button" class="item-btn ${on} ${v ? "v-" + v : ""}" data-i="${i}">${escapeHtml(item.title)}</button>`;
      })
      .join("") || `<p class="quiet">Nothing to review.</p>`;

  $("item-list").querySelectorAll("button[data-i]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.qi = Number(btn.dataset.i);
      renderReview();
    });
  });
  $("pending-only")?.addEventListener("change", (e) => {
    state.pendingOnly = e.target.checked;
    renderReview();
  });

  if (!it) {
    $("paper").innerHTML = `<div class="empty"><h2>No key items</h2><p>Open a markdown file, or click Review framework.</p></div>`;
    $("item-note").value = "";
    return;
  }

  const rec = dec[it.id] || {};
  $("item-note").value = rec.note || "";
  const v = rec.verdict || "";
  const decide = `${
    it.simple
      ? `<div class="simple"><div class="kind">In plain language</div><p>${escapeHtml(it.simple)}</p></div>`
      : ""
  }${
    it.recommend
      ? `<div class="decide">
        <div class="kind">Recommended action</div>
        <p>${escapeHtml(it.recommend)}</p>
      </div>`
      : it.decide
        ? `<div class="decide"><div class="kind">You are deciding</div><p>${escapeHtml(it.decide)}</p></div>`
        : ""
  }`;
  const context = `<div class="context"><div class="kind">From the note</div>${renderMarkdown(it.body || "")}</div>`;
  const doneMsg =
    done === total && total
      ? `<div class="done-banner">All ${total} concepts decided. Export decisions, or uncheck Pending first to revisit.</div>`
      : "";

  $("paper").innerHTML = `${doneMsg}
    <div class="queue-card">
      <div class="queue-bar"><span>${escapeHtml(it.file)}</span><strong>${done}/${total} concepts</strong></div>
      <h1>${escapeHtml(it.title)}</h1>
      ${decide}
      ${context}
      <div class="verdict-row">
        <button type="button" class="verdict ${v === "agree" ? "approve" : ""}" data-v="agree">Agree</button>
        <button type="button" class="verdict ${v === "disagree" ? "decline" : ""}" data-v="disagree">Disagree</button>
      </div>
      <div class="nav-row">
        <button type="button" class="verdict ghost" id="q-prev">Previous</button>
        <button type="button" class="verdict ghost" id="q-next">Next</button>
        <button type="button" class="verdict ghost" id="q-skip">Skip</button>
      </div>
    </div>`;
  typeset($("paper"));
  decorateTerms($("paper"));
  $("paper").querySelectorAll("button[data-v]").forEach((btn) => {
    btn.addEventListener("click", () => setVerdict(btn.dataset.v, true));
  });
  $("q-prev")?.addEventListener("click", goPrev);
  $("q-next")?.addEventListener("click", goNext);
  $("q-skip")?.addEventListener("click", goNextPending);
}

function buildQueueFromCurrent() {
  if (!state.current) {
    setQueue([]);
    return;
  }
  setQueue(generateItems(state.current.name, state.current.text), false);
}

async function loadFrameworkPack() {
  if (!PACK.length) {
    alert("No pack listed in board.config.json. Open files from the library, then use Review.");
    return;
  }
  const items = [];
  for (const [path] of PACK) {
    try {
      const text = await fetchRepoFile(path);
      state.opened.set(path, { name: path, text });
      items.push(...generateItems(path, text));
    } catch {
      $("serve-hint").classList.remove("hidden");
      alert(
        PACK.length
          ? `Could not load the review pack. Run python whiteboard/serve.py, or open the files listed in board.config.json yourself, then use Review.`
          : "No pack listed in board.config.json. Open files, then use Review."
      );
      return;
    }
  }
  setQueue(items, true);
  state.current = state.opened.get(PACK[0][0]);
  state.mode = "review";
  document.querySelectorAll(".mode").forEach((b) => b.classList.toggle("on", b.dataset.mode === "review"));
  paintOpened();
  paintLibrary();
  renderReview();
}

function setFormulaRail(text) {
  const eqs = extractDisplayMath(text);
  const rail = $("formula-rail");
  if (!eqs.length) {
    rail.innerHTML = `<p class="quiet">No display equations in this file.</p>`;
    return;
  }
  rail.innerHTML = eqs
    .map((tex) => `<div class="eq">$$${tex}$$</div><p class="plain quiet">${escapeHtml(plainFromTex(tex))}</p>`)
    .join("");
  typeset(rail);
}

function loadReview(name) {
  const rec = notesStore()[fileKey(name)] || {};
  $("status").value = rec.status || "";
  $("notes").value = rec.notes || "";
  $("notes-meta").textContent = rec.updated ? `Saved ${rec.updated}` : "Notes stay in this browser.";
}

function persistReview() {
  if (!state.current) return;
  const all = notesStore();
  all[fileKey(state.current.name)] = {
    status: $("status").value,
    notes: $("notes").value,
    updated: new Date().toISOString().slice(0, 16).replace("T", " "),
  };
  saveNotesStore(all);
  $("notes-meta").textContent = `Saved ${all[fileKey(state.current.name)].updated}`;
  persistDecisionsToRepo();
  paintLibrary();
  paintOpened();
}

function showFile(rec) {
  state.current = rec;
  if (state.mode === "review") {
    if (!state.packMode) buildQueueFromCurrent();
    renderReview();
    loadReview(rec.name);
    paintLibrary();
    paintOpened();
    return;
  }
  setReviewChrome(false);
  const html =
    state.mode === "logic" ? logicHtml(rec.name, rec.text) : renderSource(rec.name, rec.text);
  $("paper").innerHTML = html;
  typeset($("paper"));
  decorateTerms($("paper"));
  $("paper")
    .querySelectorAll("h1, h2, h3")
    .forEach((h, i) => {
      if (!h.id) h.id = `h-${i}`;
    });
  $("outline").innerHTML = [...$("paper").querySelectorAll("h1, h2, h3")]
    .map((h) => `<a href="#${h.id}">${escapeHtml(h.textContent)}</a>`)
    .join("") || `<p class="quiet">No headings.</p>`;
  $("outline").querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      document.getElementById(a.getAttribute("href").slice(1))?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
  setFormulaRail(rec.text);
  loadReview(rec.name);
  applyCommentHighlights();
  paintComments();
  paintLibrary();
  paintOpened();
}

function remember(name, text) {
  const rec = { name: fileKey(name), text };
  state.opened.set(rec.name, rec);
  if (state.mode === "review") state.packMode = false;
  showFile(rec);
}

async function fetchRepoFile(path) {
  const url = new URL("../" + path, window.location.href);
  url.searchParams.set("v", String(Date.now()));
  const res = await fetch(url, { cache: "no-store" });
  if (!res.ok) throw new Error(`${res.status} ${path}`);
  return res.text();
}

function firstLibraryPath() {
  return LIBRARY.flatMap((g) => g.files || []).map(([path]) => path)[0] || PACK[0]?.[0] || "";
}

async function probeServer() {
  const sample = firstLibraryPath();
  if (!sample) {
    state.served = false;
    $("serve-hint").classList.add("hidden");
    return;
  }
  try {
    const res = await fetch("../" + sample, { method: "HEAD" });
    state.served = res.ok;
  } catch {
    state.served = false;
  }
  $("serve-hint").classList.toggle("hidden", state.served);
}

function statusTag(name) {
  const st = notesStore()[fileKey(name)]?.status;
  return st ? `<span class="tag">${st}</span>` : "";
}

function paintLibrary() {
  $("library").innerHTML = LIBRARY.map((g) => {
    const items = g.files
      .map(([path, label]) => {
        const on = state.current?.name === path ? "on" : "";
        const st = notesStore()[path]?.status;
        const stc = st ? `on-${st}` : "";
        return `<button type="button" class="file-btn ${on} ${stc}" data-path="${path}">${label}${statusTag(path)}</button>`;
      })
      .join("");
    return `<div class="group-label">${g.group}</div>${items}`;
  }).join("");
  $("library").querySelectorAll("button[data-path]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const path = btn.dataset.path;
      try {
        const text = await fetchRepoFile(path);
        remember(path, text);
      } catch {
        $("serve-hint").classList.remove("hidden");
        alert("Could not load from the project. Run python whiteboard/serve.py, or use Open files.");
      }
    });
  });
}

function paintOpened() {
  if (!state.opened.size) {
    $("opened").innerHTML = `<p class="quiet">None yet.</p>`;
    return;
  }
  $("opened").innerHTML = [...state.opened.values()]
    .map((rec) => {
      const on = state.current?.name === rec.name ? "on" : "";
      const st = notesStore()[rec.name]?.status;
      return `<button type="button" class="file-btn ${on} ${st ? "on-" + st : ""}" data-open="${rec.name}">${rec.name}${statusTag(rec.name)}</button>`;
    })
    .join("");
  $("opened").querySelectorAll("button[data-open]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const path = btn.dataset.open;
      try {
        const text = await fetchRepoFile(path);
        remember(path, text);
      } catch {
        showFile(state.opened.get(path));
      }
    });
  });
}

function readFiles(fileList) {
  [...fileList].forEach((file) => {
    const reader = new FileReader();
    reader.onload = () => remember(file.name, String(reader.result));
    reader.readAsText(file);
  });
}

$("file-input").addEventListener("change", (e) => {
  readFiles(e.target.files);
  e.target.value = "";
});

$("btn-folder").addEventListener("click", async () => {
  if (!window.showDirectoryPicker) {
    alert("This browser cannot open a folder. Use Open files, or Chrome/Edge on localhost.");
    return;
  }
  try {
    const dir = await window.showDirectoryPicker();
    for await (const [name, handle] of dir.entries()) {
      if (handle.kind !== "file") continue;
      if (!/\.(md|markdown|txt|ya?ml|py|html?|csv|json)$/i.test(name)) continue;
      const file = await handle.getFile();
      const text = await file.text();
      remember(name, text);
    }
  } catch (err) {
    if (err && err.name !== "AbortError") console.warn(err);
  }
});

document.querySelectorAll(".mode").forEach((btn) => {
  btn.addEventListener("click", () => {
    state.mode = btn.dataset.mode;
    if (state.mode !== "review") state.packMode = false;
    document.querySelectorAll(".mode").forEach((b) => b.classList.toggle("on", b === btn));
    if (state.mode === "review") {
      if (state.current && !state.packMode) buildQueueFromCurrent();
      if (state.queue.length) renderReview();
      else if (state.current) showFile(state.current);
      else renderReview();
    } else if (state.current) {
      showFile(state.current);
    } else {
      setReviewChrome(false);
    }
  });
});

$("notes").addEventListener("input", persistReview);
$("status").addEventListener("change", persistReview);
$("item-note")?.addEventListener("input", () => {
  const it = currentItem();
  if (!it) return;
  const all = itemDecisions();
  all[it.id] = {
    ...(all[it.id] || {}),
    note: $("item-note").value,
    title: it.title,
    file: it.file,
    kind: it.kind,
    recommend: it.recommend || "",
    updated: stamp(),
  };
  saveItemDecisions(all);
});

$("btn-pack")?.addEventListener("click", () => loadFrameworkPack());

$("btn-export").addEventListener("click", () => {
  const all = notesStore();
  const items = itemDecisions();
  const md = ["# Drafting board decisions", ""];
  const byFile = {};
  for (const rec of Object.values(items)) {
    if (!rec.file) continue;
    (byFile[rec.file] ||= []).push(rec);
  }
  for (const [file, recs] of Object.entries(byFile)) {
    md.push(`## ${file}`, "");
    for (const rec of recs) {
      md.push(`- **${rec.verdict || "open"}** ${rec.title || ""}`);
      if (rec.recommend) md.push(`  - Recommended: ${rec.recommend}`);
      if (rec.note) md.push(`  - Comment: ${rec.note.replace(/\n/g, "\n    ")}`);
    }
    md.push("");
  }
  for (const [file, rec] of Object.entries(all)) {
    if (!rec.notes && !rec.status) continue;
    md.push(`## File notes — ${file}`, "", `- Status: ${rec.status || "—"}`, "", rec.notes || "", "");
  }
  const byCommentFile = {};
  for (const rec of Object.values(state.comments)) {
    if (!rec?.file) continue;
    (byCommentFile[rec.file] ||= []).push(rec);
  }
  for (const [file, recs] of Object.entries(byCommentFile)) {
    md.push(`## Inline comments — ${file}`, "");
    for (const rec of recs) {
      const done = (rec.status || "open") === "resolved" ? "done · " : "";
      md.push(`> ${String(rec.quote || "").replace(/\n/g, " ")}`, "", `${done}${rec.note || ""}`, "");
    }
  }
  const blob = new Blob([md.join("\n")], { type: "text/markdown" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "board-decisions.md";
  a.click();
  URL.revokeObjectURL(a.href);
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") hideCommentPop();
  if (state.mode !== "review") {
    if (e.key === "c" || e.key === "C") {
      const tag = (e.target && e.target.tagName) || "";
      if (tag === "TEXTAREA" || tag === "INPUT") return;
      if (window.getSelection() && !window.getSelection().isCollapsed) {
        e.preventDefault();
        openCommentComposer();
      }
    }
    return;
  }
  const tag = (e.target && e.target.tagName) || "";
  if (tag === "TEXTAREA" || tag === "INPUT") return;
  if (e.key === "a" || e.key === "A") {
    e.preventDefault();
    setVerdict("agree", true);
  } else if (e.key === "x" || e.key === "X" || e.key === "d" || e.key === "D") {
    e.preventDefault();
    setVerdict("disagree", true);
  } else if (e.key === "m" || e.key === "M") {
    e.preventDefault();
    $("item-note")?.focus();
  } else if (e.key === "ArrowLeft") {
    e.preventDefault();
    goPrev();
  } else if (e.key === "ArrowRight") {
    e.preventDefault();
    goNext();
  }
});

const drop = $("drop");
["dragenter", "dragover"].forEach((ev) => {
  drop.addEventListener(ev, (e) => {
    e.preventDefault();
    drop.classList.add("over");
  });
});
["dragleave", "drop"].forEach((ev) => {
  drop.addEventListener(ev, (e) => {
    e.preventDefault();
    drop.classList.remove("over");
  });
});
drop.addEventListener("drop", (e) => {
  if (e.dataTransfer?.files?.length) readFiles(e.dataTransfer.files);
});

async function applyConfig(cfg) {
  const id = cfg.id || "default";
  if (id === "solar-reflect") {
    NOTES_KEY = "solar-reflect-board-notes-v1";
    ITEMS_KEY = "solar-reflect-board-items-v3";
    COMMENTS_KEY = "solar-reflect-board-comments-v1";
  } else {
    NOTES_KEY = `drafting-board-notes:${id}`;
    ITEMS_KEY = `drafting-board-items:${id}`;
    COMMENTS_KEY = `drafting-board-comments:${id}`;
  }
  if (Array.isArray(cfg.library)) LIBRARY = cfg.library;
  if (Array.isArray(cfg.pack)) PACK = cfg.pack;
  if (Array.isArray(cfg.concepts)) CONCEPTS = cfg.concepts;
  PACK_LABEL = cfg.packLabel || PACK_LABEL;
  TERMS = cfg.terms?.length ? BUILTIN_TERMS.concat(cfg.terms) : BUILTIN_TERMS;
  rebuildTermIndex();

  if (cfg.title) {
    const h1 = document.querySelector(".brand h1");
    if (h1) h1.textContent = cfg.title;
    document.title = cfg.title;
  }
  if (cfg.subtitle) {
    const p = document.querySelector(".brand p");
    if (p) p.textContent = cfg.subtitle;
  }
  if ($("btn-pack")) $("btn-pack").textContent = PACK_LABEL;
  const emptyOpen = $("empty-open");
  const names = LIBRARY.flatMap((g) => g.files || []).slice(0, 3).map(([, label]) => label);
  if (emptyOpen && names.length) {
    emptyOpen.innerHTML = `Open <strong>${names.join("</strong>, <strong>")}</strong> from the library (if the server is running), or use <strong>Open files</strong>.`;
  }
  const emptyPack = $("empty-pack");
  if (emptyPack) {
    emptyPack.innerHTML = PACK.length
      ? `<strong>${PACK_LABEL}</strong> loads ${PACK.map(([path, label]) => label || path).join(", ")} into one queue.`
      : `Add a <code>pack</code> in <code>board.config.json</code>, or open files and use <strong>Review</strong>.`;
  }
}

async function loadConfig() {
  try {
    const res = await fetch("board.config.json", { cache: "no-store" });
    if (!res.ok) return;
    await applyConfig(await res.json());
  } catch {
    /* generic mode: Open files still works */
  }
}

async function boot() {
  await loadConfig();
  await loadDecisionsFromRepo();
  await loadCommentsFromRepo();
  state.comments = { ...commentsStore(), ...state.comments };
  saveCommentsStore(state.comments);
  if (Object.keys(state.comments).length) await persistCommentToRepo(null);
  paintLibrary();
  paintOpened();
  paintComments();
  probeServer();
  bindTermPop();
  bindCommentUi();
}

boot();
