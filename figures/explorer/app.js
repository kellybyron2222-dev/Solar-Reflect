import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const KM = 0.01;
const R = 6371 * KM;
const THETA = (6 * Math.PI) / 180;
const DRAW_T = 14;
const DRAW_I = 6;
const MU = 3.986004418e14;
const OMEGA_E = 7.2921159e-5;
const DAY_URLS = [
  "https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-blue-marble.jpg",
  "https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg",
];
const NIGHT_URLS = [
  "https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-night.jpg",
  "https://unpkg.com/three-globe/example/img/earth-night.jpg",
];

const $ = (id) => document.getElementById(id);

let data;
try {
  const res = await fetch("./cases.json");
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  data = await res.json();
} catch (err) {
  $("stats").innerHTML = `<dt>Load</dt><dd class="warn">Could not read cases.json. Serve the repo (not file://).</dd>`;
  throw err;
}

const view = $("view");
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(view.clientWidth, view.clientHeight);
renderer.setClearColor(0x020308, 1);
renderer.toneMapping = THREE.NoToneMapping;
renderer.outputColorSpace = THREE.SRGBColorSpace;
view.appendChild(renderer.domElement);
renderer.domElement.style.touchAction = "none";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(42, view.clientWidth / view.clientHeight, 0.08, 4000);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.1;
controls.enablePan = false;
controls.enableZoom = false;
controls.rotateSpeed = 0.85;
controls.minPolarAngle = 0.08;
controls.maxPolarAngle = Math.PI - 0.08;

scene.add(new THREE.AmbientLight(0xffffff, 0.35));
const sunLight = new THREE.DirectionalLight(0xfff6e8, 1.65);
sunLight.position.set(400, 0, 0);
scene.add(sunLight);

function makeSunSprite() {
  const s = 512;
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = s;
  const ctx = canvas.getContext("2d");
  const cx = s / 2;
  const cy = s / 2;
  ctx.clearRect(0, 0, s, s);
  const glow = ctx.createRadialGradient(cx, cy, 0, cx, cy, cx);
  glow.addColorStop(0, "rgba(255,255,255,1)");
  glow.addColorStop(0.06, "rgba(255,252,240,1)");
  glow.addColorStop(0.1, "rgba(255,236,170,0.95)");
  glow.addColorStop(0.16, "rgba(255,200,70,0.45)");
  glow.addColorStop(0.28, "rgba(255,150,30,0.12)");
  glow.addColorStop(0.5, "rgba(255,110,20,0.04)");
  glow.addColorStop(1, "rgba(255,90,0,0)");
  ctx.fillStyle = glow;
  ctx.fillRect(0, 0, s, s);
  const tex = new THREE.CanvasTexture(canvas);
  tex.colorSpace = THREE.NoColorSpace;
  const mat = new THREE.SpriteMaterial({
    map: tex,
    transparent: true,
    depthWrite: false,
    blending: THREE.AdditiveBlending,
  });
  const sprite = new THREE.Sprite(mat);
  sprite.position.set(260, 0, 0);
  sprite.scale.set(22, 22, 1);
  return sprite;
}
const sunSprite = makeSunSprite();
scene.add(sunSprite);

function makeStarTexture() {
  const s = 64;
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = s;
  const ctx = canvas.getContext("2d");
  const g = ctx.createRadialGradient(s / 2, s / 2, 0, s / 2, s / 2, s / 2);
  g.addColorStop(0, "rgba(255,255,255,1)");
  g.addColorStop(0.18, "rgba(230,236,245,0.85)");
  g.addColorStop(0.4, "rgba(200,210,230,0.25)");
  g.addColorStop(1, "rgba(0,0,0,0)");
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, s, s);
  const tex = new THREE.CanvasTexture(canvas);
  tex.colorSpace = THREE.NoColorSpace;
  return tex;
}

const stars = new THREE.Points(
  (() => {
    const n = 1600;
    const pos = new Float32Array(n * 3);
    for (let i = 0; i < n; i += 1) {
      const v = new THREE.Vector3().randomDirection().multiplyScalar(900 + Math.random() * 500);
      pos[i * 3] = v.x;
      pos[i * 3 + 1] = v.y;
      pos[i * 3 + 2] = v.z;
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    return g;
  })(),
  new THREE.PointsMaterial({
    map: makeStarTexture(),
    color: 0xe8eef6,
    size: 2.2,
    sizeAttenuation: false,
    transparent: true,
    depthWrite: false,
    blending: THREE.AdditiveBlending,
    alphaTest: 0.05,
  })
);
scene.add(stars);

function satPosition(a, psi) {
  return new THREE.Vector3(0, a * Math.sin(psi), a * Math.cos(psi));
}

function sunDirEcef(t) {
  const w = OMEGA_E * t;
  return new THREE.Vector3(Math.cos(w), 0, Math.sin(w));
}

function toEcef(p, t) {
  const w = OMEGA_E * t;
  const c = Math.cos(-w);
  const s = Math.sin(-w);
  return new THREE.Vector3(p.x * c + p.z * s, p.y, -p.x * s + p.z * c);
}

function nightSite(psi) {
  const ct = Math.cos(THETA);
  const st = Math.sin(THETA);
  return new THREE.Vector3(-R * st, R * ct * Math.sin(psi), R * ct * Math.cos(psi));
}

function foilVisualSide(A_m2) {
  const sideM = Math.sqrt(Math.max(A_m2, 1));
  const trueUnits = sideM / 1e5;
  return Math.min(trueUnits * 900, 5);
}

function fract(x) {
  return x - Math.floor(x);
}

function formatEST(simTime) {
  const uOffset = (OMEGA_E * simTime) / (Math.PI * 2);
  const uSun = fract(0.5 - uOffset);
  const uEst = (-75 + 180) / 360;
  const hours = fract(0.5 + (uEst - uSun)) * 24;
  const h24 = Math.floor(hours) % 24;
  const minutes = Math.floor((hours * 60) % 60);
  const seconds = Math.floor((hours * 3600) % 60);
  const ampm = h24 >= 12 ? "PM" : "AM";
  const h12 = h24 % 12 === 0 ? 12 : h24 % 12;
  const pad = (n) => String(n).padStart(2, "0");
  return `${h12}:${pad(minutes)}:${pad(seconds)} ${ampm} EST`;
}

function fallbackMaps() {
  const w = 1024;
  const h = 512;
  const day = document.createElement("canvas");
  day.width = w;
  day.height = h;
  const ctx = day.getContext("2d");
  const g = ctx.createLinearGradient(0, 0, 0, h);
  g.addColorStop(0, "#dbe7f0");
  g.addColorStop(0.15, "#1a5f8a");
  g.addColorStop(0.5, "#0c4a72");
  g.addColorStop(0.85, "#1a5f8a");
  g.addColorStop(1, "#dbe7f0");
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, w, h);
  ctx.fillStyle = "#3a6b3e";
  const blob = (cx, cy, rx, ry) => {
    ctx.beginPath();
    ctx.ellipse(cx * w, cy * h, rx * w, ry * h, 0, 0, Math.PI * 2);
    ctx.fill();
  };
  blob(0.54, 0.5, 0.06, 0.14);
  blob(0.64, 0.32, 0.16, 0.08);
  blob(0.22, 0.42, 0.07, 0.12);
  blob(0.25, 0.62, 0.05, 0.12);
  blob(0.82, 0.66, 0.05, 0.04);
  ctx.fillStyle = "#e8eef4";
  ctx.fillRect(0, 0, w, h * 0.08);
  ctx.fillRect(0, h * 0.92, w, h * 0.08);
  const night = document.createElement("canvas");
  night.width = w;
  night.height = h;
  night.getContext("2d").fillRect(0, 0, w, h);
  const dayTex = new THREE.CanvasTexture(day);
  const nightTex = new THREE.CanvasTexture(night);
  dayTex.colorSpace = THREE.NoColorSpace;
  nightTex.colorSpace = THREE.NoColorSpace;
  return { dayTex, nightTex };
}

function loadTex(url) {
  return new Promise((resolve, reject) => {
    const loader = new THREE.TextureLoader();
    loader.setCrossOrigin("anonymous");
    loader.load(
      url,
      (tex) => {
        tex.colorSpace = THREE.NoColorSpace;
        tex.anisotropy = 8;
        resolve(tex);
      },
      undefined,
      reject
    );
  });
}

async function loadFirst(urls) {
  for (const url of urls) {
    try {
      return await loadTex(url);
    } catch {
      /* try next mirror */
    }
  }
  throw new Error("texture");
}

const fallback = fallbackMaps();
const earthUniforms = {
  dayMap: { value: fallback.dayTex },
  nightMap: { value: fallback.nightTex },
  sunDir: { value: new THREE.Vector3(1, 0, 0) },
  siteDir: { value: new THREE.Vector3(-Math.sin(THETA), 0, Math.cos(THETA)) },
  axisU: { value: new THREE.Vector3(0, 1, 0) },
  axisV: { value: new THREE.Vector3(0, 0, 1) },
  patchMaj: { value: 0.001 },
  patchMin: { value: 0.001 },
  strength: { value: 0.0 },
  cityLights: { value: 1.0 },
};

const earthMat = new THREE.ShaderMaterial({
  uniforms: earthUniforms,
  vertexShader: `
    varying vec3 vObj;
    varying vec2 vUv;
    void main() {
      vUv = uv;
      vObj = normalize(position);
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    uniform sampler2D dayMap;
    uniform sampler2D nightMap;
    uniform vec3 sunDir;
    uniform vec3 siteDir;
    uniform vec3 axisU;
    uniform vec3 axisV;
    uniform float patchMaj;
    uniform float patchMin;
    uniform float strength;
    uniform float cityLights;
    varying vec3 vObj;
    varying vec2 vUv;

    void main() {
      vec3 p = normalize(vObj);
      vec2 uv = vUv;
      float ndl = dot(p, normalize(sunDir));
      float day = smoothstep(-0.03, 0.14, ndl);
      vec3 dayCol = pow(texture2D(dayMap, uv).rgb, vec3(2.2));
      vec3 lights = pow(texture2D(nightMap, uv).rgb, vec3(2.2));
      float wrap = max(ndl, 0.0);
      vec3 sunlit = dayCol * mix(0.72, 1.25, wrap);
      vec3 nightTerrain = dayCol * 0.045;
      vec3 night = nightTerrain + lights * cityLights;
      vec3 base = mix(night, sunlit, day);

      vec3 S = normalize(siteDir);
      float u = dot(p, normalize(axisU));
      float v = dot(p, normalize(axisV));
      float q = (u * u) / max(patchMaj * patchMaj, 1e-12) + (v * v) / max(patchMin * patchMin, 1e-12);
      float face = smoothstep(0.86, 0.98, dot(p, S));
      float core = 1.0 - smoothstep(0.55, 1.12, q);
      float penumbra = 1.0 - smoothstep(1.0, 2.4, q);
      float spot = (0.7 * core + 0.22 * penumbra) * face * strength;
      vec3 duskFill = dayCol * 0.42;
      base = mix(base, duskFill, clamp(spot, 0.0, 0.85));
      gl_FragColor = vec4(base, 1.0);
    }
  `,
});

const earth = new THREE.Mesh(new THREE.SphereGeometry(R, 128, 96), earthMat);
earthMat.toneMapped = false;
scene.add(earth);

const atmosphere = new THREE.Mesh(
  new THREE.SphereGeometry(R * 1.03, 64, 48),
  new THREE.ShaderMaterial({
    transparent: true,
    depthWrite: false,
    side: THREE.BackSide,
    uniforms: { sunDir: { value: new THREE.Vector3(1, 0, 0) } },
    vertexShader: `
      varying vec3 vN;
      varying vec3 vW;
      void main() {
        vN = normalize((modelMatrix * vec4(normal, 0.0)).xyz);
        vec4 w = modelViewMatrix * vec4(position, 1.0);
        vW = w.xyz;
        gl_Position = projectionMatrix * w;
      }
    `,
    fragmentShader: `
      uniform vec3 sunDir;
      varying vec3 vN;
      varying vec3 vW;
      void main() {
        vec3 view = normalize(-vW);
        float fres = pow(1.0 - abs(dot(view, normalize(vN))), 2.4);
        float day = smoothstep(-0.25, 0.55, dot(normalize(vN), normalize(sunDir)));
        vec3 col = mix(vec3(0.12, 0.16, 0.28), vec3(0.4, 0.65, 1.0), day);
        gl_FragColor = vec4(col, fres * 0.5);
      }
    `,
  })
);
scene.add(atmosphere);

const TRAIL_MAX = 2400;
const trailPos = new Float32Array(TRAIL_MAX * 3);
const trailCol = new Float32Array(TRAIL_MAX * 3);
const trailGeo = new THREE.BufferGeometry();
trailGeo.setAttribute("position", new THREE.BufferAttribute(trailPos, 3));
trailGeo.setAttribute("color", new THREE.BufferAttribute(trailCol, 3));
trailGeo.setDrawRange(0, 0);
const trailMat = new THREE.LineBasicMaterial({
  vertexColors: true,
  transparent: true,
  opacity: 0.95,
  depthWrite: false,
});
const trailGroup = new THREE.Group();
trailGroup.renderOrder = 2;
scene.add(trailGroup);
const trailLine = new THREE.Line(trailGeo, trailMat);
trailGroup.add(trailLine);

const trailPts = [];
let trailA = -1;
let lastTrailPhase = null;
let trailIStar = null;
let trailDrawnN = null;

function paintTrailStroke() {
  const n = trailPts.length;
  for (let i = 0; i < n; i += 1) {
    trailPos[i * 3] = trailPts[i].x;
    trailPos[i * 3 + 1] = trailPts[i].y;
    trailPos[i * 3 + 2] = trailPts[i].z;
    const age = n === 1 ? 1 : i / (n - 1);
    const fade = 0.28 + 0.72 * age;
    trailCol[i * 3] = 0.55 * fade;
    trailCol[i * 3 + 1] = 0.72 * fade;
    trailCol[i * 3 + 2] = 0.88 * fade;
  }
  trailGeo.attributes.position.needsUpdate = true;
  trailGeo.attributes.color.needsUpdate = true;
  trailGeo.setDrawRange(0, n);
  trailGeo.computeBoundingSphere();
}

function commitTrailStroke() {
  if (trailPts.length >= 2) {
    const n = trailPts.length;
    const pos = trailPos.slice(0, n * 3);
    const col = trailCol.slice(0, n * 3);
    const g = new THREE.BufferGeometry();
    g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    g.setAttribute("color", new THREE.BufferAttribute(col, 3));
    trailGroup.add(new THREE.Line(g, trailMat));
    const frozen = trailGroup.children.filter((ch) => ch !== trailLine);
    while (frozen.length > 8) {
      const ch = frozen.shift();
      trailGroup.remove(ch);
      ch.geometry.dispose();
    }
  }
  trailPts.length = 0;
  lastTrailPhase = null;
  trailGeo.setDrawRange(0, 0);
}

function resetTrail() {
  for (const ch of [...trailGroup.children]) {
    if (ch === trailLine) continue;
    trailGroup.remove(ch);
    ch.geometry.dispose();
  }
  trailPts.length = 0;
  lastTrailPhase = null;
  trailA = -1;
  trailGeo.setDrawRange(0, 0);
}

function pushTrail(a, phase, t) {
  if (trailA >= 0 && Math.abs(a - trailA) > 0.02) commitTrailStroke();
  trailA = a;
  if (lastTrailPhase != null && Math.abs(phase - lastTrailPhase) < 0.012) return;
  lastTrailPhase = phase;
  trailPts.push(toEcef(satPosition(a, phase), t));
  if (trailPts.length > TRAIL_MAX) trailPts.shift();
  paintTrailStroke();
}

function noteTrailFleet(iStar, nDrawn) {
  if (trailIStar != null && iStar !== trailIStar && nDrawn !== trailDrawnN) {
    resetTrail();
  }
  trailIStar = iStar;
  trailDrawnN = nDrawn;
}

const satGroup = new THREE.Group();
scene.add(satGroup);
const beamGroup = new THREE.Group();
scene.add(beamGroup);

const groundPool = new THREE.Mesh(
  new THREE.CircleGeometry(1, 48),
  new THREE.MeshBasicMaterial({
    color: 0xcfc8b4,
    transparent: true,
    opacity: 0.12,
    side: THREE.DoubleSide,
    depthWrite: false,
  })
);
groundPool.visible = false;
scene.add(groundPool);

function patchFrame(psi) {
  const S = nightSite(psi).normalize();
  const pole = Math.abs(S.y) > 0.92 ? new THREE.Vector3(0, 0, 1) : new THREE.Vector3(0, 1, 0);
  const U = new THREE.Vector3().crossVectors(pole, S).normalize();
  const V = new THREE.Vector3().crossVectors(S, U).normalize();
  return { S, U, V, aim: nightSite(psi) };
}

function foilNormal(pos, aim, sun) {
  const toSun = sun.clone().normalize();
  const toSite = aim.clone().sub(pos).normalize();
  return toSun.add(toSite).normalize();
}

function clearGroup(g) {
  while (g.children.length) {
    const ch = g.children[0];
    g.remove(ch);
    if (ch.geometry) ch.geometry.dispose();
    if (ch.material) ch.material.dispose();
  }
}

function findCase() {
  const key = {
    h_km: Number($("h").value),
    class_id: $("class").value,
    foil_id: $("foil").value,
    eta_id: $("eta").value,
  };
  return data.cases.find(
    (c) =>
      c.h_km === key.h_km &&
      c.class_id === key.class_id &&
      c.foil_id === key.foil_id &&
      c.eta_id === key.eta_id
  );
}

function fmt(n, digits = 3) {
  if (n == null || !Number.isFinite(n)) return "—";
  if (Math.abs(n) >= 1000) return n.toExponential(3);
  return n.toPrecision(digits);
}

function bar(frac) {
  const p = Math.max(0, Math.min(1, frac));
  return `<span class="bar"><i style="width:${(p * 100).toFixed(1)}%"></i></span>`;
}

function renderStats(c, drawnT, drawnI) {
  const no = c.no_pass;
  const iFrac = !no && c.I > 0 ? c.I / c.I_star : 0;
  const tFrac = !no && c.T_star_min ? c.T_useful_min / c.T_star_min : no ? 0 : 1;
  const nNote =
    no || c.N == null
      ? "—"
      : drawnT < Math.round(c.N)
        ? `drawn ${drawnT} of ${fmt(c.N, 4)}`
        : fmt(c.N, 4);
  const rows = [
    ["Altitude", `${c.h_km} km`],
    [
      "Useful dwell",
      no
        ? "no pass — orbit below the 30° night floor"
        : `${fmt(c.T_useful_min, 4)} min · set by altitude, not foil or class`,
    ],
    ["Required T*", c.T_star_min == null ? "1 pass · C-moon" : `${fmt(c.T_star_min, 3)} min · set by use class`],
    ["Required I*", `${c.I_star} W/m² · set by use class`],
    ["This foil I", no ? "—" : `${fmt(c.I)} W/m²`],
    ["I / I*", no ? bar(0) : bar(iFrac)],
    ["T_u / T*", no ? bar(0) : c.T_star_min == null ? "1 pass" : bar(tFrac)],
    ["Foil area", `${fmt(c.A_m2, 4)} m²`],
    ["True patch", `${fmt(c.D_minor_km, 3)} × ${fmt(c.D_major_km, 3)} km`],
    ["Drawn foil", `${fmt(Math.sqrt(c.A_m2), 4)} m square · ${fmt(motion.foilVis / KM, 3)} km on screen (size from A only)`],
    ["Elevation", `${fmt(c.eps_deg, 3)}°`],
    ["N_I (brightness)", no ? "—" : `${fmt(c.N_I, 4)}${motion.layout === "cluster" ? " · drawn as a tight co-aimed cluster" : " · not drawn (would overlap; F18)"}`],
    [
      "Drawn count",
      no
        ? "1 (no pass)"
        : motion.layout === "cluster"
          ? `${drawnT} of N_I=${fmt(c.N_I, 4)} clustered (cap ${DRAW_I})`
          : `${drawnT} of N_T=${fmt(c.N_T, 4)} train, spaced by T_useful (cap ${DRAW_T})`,
    ],
    ["N (one site)", no ? "impossible" : nNote],
  ];
  $("stats").innerHTML = rows
    .map(([k, v]) => `<dt>${k}</dt><dd class="${no && k.startsWith("N") ? "warn" : ""}">${v}</dd>`)
    .join("");
}

const motion = {
  a: (6371 + 625) * KM,
  nT: 1,
  nI: 1,
  half: 0,
  dpsi: 0,
  layout: "train",
  noPass: false,
  foilVis: 0.5,
  patchMajU: 0.05,
  patchMinU: 0.05,
  slots: [],
  beams: [],
};

function meanMotion(hKm) {
  const a = (6371 + hKm) * 1000;
  return Math.sqrt(MU / (a * a * a));
}

function rebuildSats(c) {
  const a = (6371 + c.h_km) * KM;
  const nTround = c.no_pass || c.N_T == null ? 1 : Math.max(1, Math.round(c.N_T));
  const nIround = c.no_pass || c.N_I == null ? 1 : Math.max(1, Math.round(c.N_I));
  const cluster = !c.no_pass && nTround <= 1 && nIround > 1;
  const nDraw = c.no_pass
    ? 1
    : cluster
      ? Math.min(DRAW_I, nIround)
      : Math.min(DRAW_T, nTround);
  const period = (2 * Math.PI) / meanMotion(c.h_km);
  const dpsiTrain = c.no_pass || !(c.T_useful_min > 0) ? 0 : (2 * Math.PI * c.T_useful_min * 60) / period;
  const dpsiCluster = Math.max(0.012, (foilVisualSide(c.A_m2) * 1.35) / a);
  const dpsi = cluster ? dpsiCluster : dpsiTrain;

  motion.a = a;
  motion.nT = nDraw;
  motion.nI = nIround;
  motion.layout = cluster ? "cluster" : "train";
  motion.dpsi = dpsi;
  motion.noPass = c.no_pass;
  motion.foilVis = foilVisualSide(c.A_m2);
  motion.half = nDraw <= 1 ? 0 : (dpsi * (nDraw - 1)) / 2;
  const trueMaj = Math.max((c.D_major_km / 2) / 6371, 1e-6);
  const trueMin = Math.max((c.D_minor_km / 2) / 6371, 1e-6);
  motion.patchMajU = trueMaj * R;
  motion.patchMinU = trueMin * R;

  earthUniforms.patchMaj.value = trueMaj;
  earthUniforms.patchMin.value = trueMin;
  const iFrac = c.no_pass || !(c.I > 0) ? 0 : Math.min(1, c.I / c.I_star);
  earthUniforms.strength.value = !$("show-patch").checked || c.no_pass ? 0 : 0.55 + 0.35 * iFrac;

  clearGroup(satGroup);
  clearGroup(beamGroup);
  motion.slots = [];
  motion.beams = [];
  const mat = new THREE.MeshPhongMaterial({
    color: c.no_pass ? 0x666666 : 0xd5dee6,
    emissive: c.no_pass ? 0x111111 : 0x3a4a58,
    shininess: 110,
    specular: 0xffffff,
  });
  const thick = Math.max(0.01, motion.foilVis * 0.025);
  for (let s = 0; s < nDraw; s += 1) {
    const psi0 = nDraw === 1 ? 0 : -motion.half + dpsi * s;
    const foil = new THREE.Mesh(new THREE.BoxGeometry(motion.foilVis, motion.foilVis, thick), mat);
    satGroup.add(foil);
    motion.slots.push({ mesh: foil, psi0 });
    if (!c.no_pass && $("show-patch").checked) {
      const beam = new THREE.Line(
        new THREE.BufferGeometry(),
        new THREE.LineBasicMaterial({
          color: 0xb9b3a4,
          transparent: true,
          opacity: 0.45,
          depthWrite: false,
        })
      );
      beamGroup.add(beam);
      motion.beams.push({ mesh: beam, psi0 });
    }
  }
  groundPool.visible = $("show-patch").checked && !c.no_pass;
  return { nT: c.no_pass ? 0 : nDraw, nI: cluster ? nDraw : 1 };
}

function placeSats(phase, t) {
  const sun = sunDirEcef(t);
  const sat0 = toEcef(satPosition(motion.a, phase), t);
  const aim = toEcef(nightSite(phase), t);
  const S = aim.clone().normalize();
  const look = sat0.clone().sub(aim);
  const major = look.clone().addScaledVector(S, -look.dot(S));
  if (major.lengthSq() < 1e-12) {
    major.copy(Math.abs(S.y) > 0.92 ? new THREE.Vector3(0, 0, 1) : new THREE.Vector3(0, 1, 0));
  }
  major.normalize();
  const minor = new THREE.Vector3().crossVectors(S, major).normalize();
  earthUniforms.siteDir.value.copy(S);
  earthUniforms.axisU.value.copy(major);
  earthUniforms.axisV.value.copy(minor);
  earthUniforms.sunDir.value.copy(sun);
  atmosphere.material.uniforms.sunDir.value.copy(sun);
  sunLight.position.copy(sun.clone().multiplyScalar(400));
  sunSprite.position.copy(sun.clone().multiplyScalar(260));

  groundPool.visible = $("show-patch").checked && !motion.noPass;
  groundPool.position.copy(aim).multiplyScalar(1.003);
  const basis = new THREE.Matrix4().makeBasis(major, minor, S);
  groundPool.quaternion.setFromRotationMatrix(basis);
  groundPool.scale.set(motion.patchMajU, motion.patchMinU, 1);
  groundPool.material.opacity = 0.1 * earthUniforms.strength.value;

  for (const slot of motion.slots) {
    const p = toEcef(satPosition(motion.a, slot.psi0 + phase), t);
    slot.mesh.position.copy(p);
    slot.mesh.lookAt(p.clone().add(foilNormal(p, aim, sun)));
  }
  for (const beam of motion.beams) {
    const from = toEcef(satPosition(motion.a, beam.psi0 + phase), t);
    beam.mesh.geometry.dispose();
    beam.mesh.geometry = new THREE.BufferGeometry().setFromPoints([from, aim]);
    beam.mesh.visible = $("show-patch").checked && !motion.noPass;
  }
}

function limits(earthView) {
  controls.minDistance = earthView ? R * 1.28 : 2.8;
  controls.maxDistance = 420;
}

function frameCamera(earthView) {
  limits(earthView);
  if (earthView) {
    camera.position.set(0, 55, 200);
    controls.target.set(0, 0, 0);
  } else {
    controls.target.copy(toEcef(nightSite(orbitPhase), simTime));
    camera.position.copy(toEcef(nightSite(orbitPhase), simTime)).add(new THREE.Vector3(-16, 10, 12));
  }
  controls.update();
}

function dolly(factor) {
  const offset = camera.position.clone().sub(controls.target);
  const next = THREE.MathUtils.clamp(offset.length() * factor, controls.minDistance, controls.maxDistance);
  offset.setLength(next);
  camera.position.copy(controls.target).add(offset);
}

function orbitBy(dx, dy) {
  const offset = camera.position.clone().sub(controls.target);
  const sph = new THREE.Spherical().setFromVector3(offset);
  sph.theta -= dx;
  sph.phi = THREE.MathUtils.clamp(sph.phi + dy, 0.08, Math.PI - 0.08);
  sph.makeSafe();
  camera.position.copy(controls.target).add(new THREE.Vector3().setFromSpherical(sph));
}

renderer.domElement.addEventListener(
  "wheel",
  (e) => {
    e.preventDefault();
    const unit = e.deltaMode === 1 ? 16 : e.deltaMode === 2 ? view.clientHeight : 1;
    const dx = THREE.MathUtils.clamp(e.deltaX * unit, -90, 90);
    const dy = THREE.MathUtils.clamp(e.deltaY * unit, -90, 90);
    if (e.ctrlKey) {
      dolly(Math.exp(dy * 0.012));
      return;
    }
    orbitBy(dx * 0.0042, dy * 0.0042);
  },
  { passive: false }
);

let pinch0 = 0;
function pinchGap(ev) {
  return Math.hypot(
    ev.touches[0].clientX - ev.touches[1].clientX,
    ev.touches[0].clientY - ev.touches[1].clientY
  );
}
renderer.domElement.addEventListener("touchstart", (e) => {
  if (e.touches.length === 2) pinch0 = pinchGap(e);
}, { passive: true });
renderer.domElement.addEventListener("touchmove", (e) => {
  if (e.touches.length !== 2 || !pinch0) return;
  e.preventDefault();
  const gap = pinchGap(e);
  dolly(pinch0 / gap);
  pinch0 = gap;
}, { passive: false });

let lastEarth = true;
function apply(resetCam) {
  const c = findCase();
  if (!c) return;
  const drawn = rebuildSats(c);
  noteTrailFleet(c.I_star, motion.nT);
  renderStats(c, drawn.nT, drawn.nI);
  const earthView = $("earth-view").checked;
  limits(earthView);
  if (resetCam || earthView !== lastEarth) frameCamera(earthView);
  lastEarth = earthView;
  placeSats(orbitPhase, simTime);
}

["class", "foil", "eta"].forEach((id) => $(id).addEventListener("change", () => apply(false)));
$("h").addEventListener("change", () => apply(false));
$("earth-view").addEventListener("change", () => apply(false));
$("city-lights").addEventListener("change", () => {
  earthUniforms.cityLights.value = $("city-lights").checked ? 1 : 0;
});
$("show-patch").addEventListener("change", () => apply(false));
$("zoom-in").addEventListener("click", () => dolly(0.72));
$("zoom-out").addEventListener("click", () => dolly(1.38));
$("view-patch").addEventListener("click", () => {
  $("earth-view").checked = false;
  apply(true);
});
$("view-earth").addEventListener("click", () => {
  $("earth-view").checked = true;
  apply(true);
});

let playing = true;
let orbitPhase = 0;
let simTime = 0;
$("play").addEventListener("click", () => {
  playing = !playing;
  $("play").textContent = playing ? "Pause" : "Play";
});
$("speed").addEventListener("input", () => {
  $("speed-read").textContent = `${$("speed").value}×`;
});

window.addEventListener("keydown", (e) => {
  if (e.key === "+" || e.key === "=") dolly(0.72);
  if (e.key === "-" || e.key === "_") dolly(1.38);
  if (e.key === " ") {
    e.preventDefault();
    $("play").click();
  }
});
window.addEventListener("resize", () => {
  camera.aspect = view.clientWidth / view.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(view.clientWidth, view.clientHeight);
});

apply(true);

let lastWall = performance.now();
(function tick(now) {
  const dt = Math.min(0.05, (now - lastWall) / 1000);
  lastWall = now;
  const speed = Number($("speed").value);
  const c = findCase();
  const n = c ? meanMotion(c.h_km) : meanMotion(625);
  if (playing) {
    simTime += dt * speed;
    orbitPhase += n * dt * speed;
  }
  earthUniforms.sunDir.value.copy(sunDirEcef(simTime));
  placeSats(orbitPhase, simTime);
  pushTrail(motion.a, orbitPhase, simTime);
  if (!$("earth-view").checked) {
    controls.target.copy(toEcef(nightSite(orbitPhase), simTime));
  }
  const periodMin = ((2 * Math.PI) / n) / 60;
  const westDeg = ((OMEGA_E * (2 * Math.PI) / n) * 180) / Math.PI;
  $("sim-read").textContent = `Sim ${(simTime / 3600).toFixed(2)} h · Earth ${(((OMEGA_E * simTime * 180) / Math.PI) % 360).toFixed(1)}° · orbit ${periodMin.toFixed(1)} min · ${westDeg.toFixed(1)}° west/rev`;
  $("tod-time").textContent = formatEST(simTime);
  $("tod-day").textContent = `Day ${Math.floor(simTime / 86400) + 1} · solar time at 75°W (not the walking patch)`;
  if (c) {
    $("hud").textContent = `${c.class_id} · ${c.h_km} km · ${c.foil_id} · ${speed}×`;
  }
  controls.update();
  renderer.render(scene, camera);
  requestAnimationFrame(tick);
})(performance.now());

try {
  const [dayTex, nightTex] = await Promise.all([loadFirst(DAY_URLS), loadFirst(NIGHT_URLS)]);
  earthUniforms.dayMap.value = dayTex;
  earthUniforms.nightMap.value = nightTex;
} catch {
  $("hud").textContent = "Globe textures unavailable — using fallback map";
}
