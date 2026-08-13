#!/usr/bin/env python3
"""
Builds _Meta/brain-map.html: a glowing constellation of the whole vault.

Re-run it whenever the vault has grown. The graph data is inlined into the
HTML, so the page works from file:// as well as over a local server.

    python3 _Meta/build-brain-map.py
"""
import os, re, json, glob, html

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT_NAME = os.path.basename(VAULT)
OUT = os.path.join(VAULT, "_Meta", "brain-map.html")

FOLDER_COLOR = {
    "00 Inbox": "#FB923C", "01 Daily": "#60A5FA", "02 Notes": "#FBBF24",
    "03 Sources": "#34D399", "04 Projects": "#22D3EE", "05 Areas": "#A78BFA",
    "06 Resources": "#94A3B8", "07 People": "#FB7185", "08 Archive": "#64748B",
    "09 Maps": "#E879F9", "_Meta": "#C4B5FD", "_Templates": "#475569",
    "root": "#FFFFFF",
}


def build():
    os.chdir(VAULT)
    files = sorted(glob.glob("**/*.md", recursive=True))

    nodes, index = [], {}
    for p in files:
        name = os.path.splitext(os.path.basename(p))[0]
        parts = p.split(os.sep)
        folder = parts[0] if len(parts) > 1 else "root"
        index[name] = len(nodes)
        nodes.append({
            "id": name,
            "path": os.path.splitext(p)[0],
            "folder": folder,
            "color": FOLDER_COLOR.get(folder, "#8B93B8"),
            "deg": 0,
        })

    edges, seen = [], set()
    for p in files:
        src = os.path.splitext(os.path.basename(p))[0]
        txt = open(p, encoding="utf-8").read().replace("\\|", "|")
        for m in re.findall(r"\[\[([^\]|#]+)", txt):
            t = m.strip()
            if t in index and t != src:
                key = tuple(sorted((src, t)))
                if key in seen:
                    continue
                seen.add(key)
                edges.append([index[src], index[t]])
                nodes[index[src]]["deg"] += 1
                nodes[index[t]]["deg"] += 1

    legend = sorted({n["folder"] for n in nodes})
    payload = {
        "nodes": nodes,
        "edges": edges,
        "vault": VAULT_NAME,
        "legend": [{"folder": f, "color": FOLDER_COLOR.get(f, "#8B93B8")} for f in legend],
    }

    page = TEMPLATE.replace("__DATA__", json.dumps(payload))
    page = page.replace("__STATS__", html.escape(
        f"{len(nodes)} notes · {len(edges)} links · "
        f"{sum(1 for n in nodes if n['deg'] == 0)} orphans"))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"wrote {OUT}")
    print(f"  {len(nodes)} nodes, {len(edges)} edges")


TEMPLATE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brain map</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --space-0:#050510; --violet:#A78BFA; --cyan:#22D3EE; --magenta:#E879F9;
    --text:#E0E0FF; --muted:#A2A6CC; --faint:#6E7398;
    --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
    --display:'Orbitron',sans-serif;
  }
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;overflow:hidden;background:var(--space-0)}
  body{font-family:var(--mono);color:var(--text)}
  #stage{position:fixed;inset:0}
  canvas{display:block;width:100%;height:100%;cursor:grab}
  canvas.dragging{cursor:grabbing}

  .hud{position:fixed;pointer-events:none;user-select:none}
  #title{top:26px;left:30px}
  #title h1{
    margin:0;font-family:var(--display);font-weight:900;font-size:30px;
    letter-spacing:.16em;text-transform:uppercase;
    background:linear-gradient(96deg,var(--cyan),var(--violet) 48%,var(--magenta));
    -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
    filter:drop-shadow(0 0 22px rgba(167,139,250,.5));
  }
  #title p{margin:6px 0 0;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--faint)}

  #legend{bottom:26px;left:30px;display:flex;flex-direction:column;gap:6px}
  .lg{display:flex;align-items:center;gap:9px;font-size:10.5px;letter-spacing:.07em;color:var(--muted)}
  .dot{width:8px;height:8px;border-radius:50%;flex:none}

  #hint{bottom:26px;right:30px;text-align:right;font-size:10.5px;letter-spacing:.07em;color:var(--faint);line-height:1.9}
  #hint b{color:var(--muted);font-weight:400}

  #tip{
    position:fixed;pointer-events:none;opacity:0;transform:translate(-50%,-100%);
    padding:9px 13px;border-radius:9px;white-space:nowrap;
    background:rgba(10,10,24,.9);border:1px solid rgba(167,139,250,.45);
    box-shadow:0 0 26px rgba(167,139,250,.3);backdrop-filter:blur(6px);
    transition:opacity .14s ease;z-index:5;
  }
  #tip .t{font-family:var(--display);font-size:12px;letter-spacing:.05em;text-transform:uppercase}
  #tip .s{font-size:10px;letter-spacing:.08em;color:var(--faint);margin-top:4px}
  @media (max-width:720px){ #legend{display:none} #title h1{font-size:20px} }
</style></head>
<body>
<div id="stage"><canvas id="c"></canvas></div>

<div class="hud" id="title">
  <h1>Brain</h1>
  <p>__STATS__</p>
</div>
<div class="hud" id="legend"></div>
<div class="hud" id="hint">
  <div><b>drag</b> pan &nbsp; <b>scroll</b> zoom</div>
  <div><b>hover</b> trace links &nbsp; <b>click</b> open in Obsidian</div>
</div>
<div id="tip"><div class="t"></div><div class="s"></div></div>

<script>
const DATA = __DATA__;
const cv = document.getElementById('c'), ctx = cv.getContext('2d', {alpha:false});
const tip = document.getElementById('tip');
let W=0, H=0, DPR=Math.min(window.devicePixelRatio||1, 2);

/* ---------- legend ---------- */
document.getElementById('legend').innerHTML = DATA.legend.filter(l=>l.folder!=='root')
  .map(l=>`<div class="lg"><span class="dot" style="background:${l.color};box-shadow:0 0 8px ${l.color}"></span>${l.folder}</div>`).join('');

/* ---------- model ---------- */
const N = DATA.nodes, E = DATA.edges;
const adj = N.map(()=>[]);
E.forEach(([s,t])=>{ adj[s].push(t); adj[t].push(s); });
N.forEach((n,i)=>{
  const a = Math.random()*Math.PI*2, r = 60 + Math.random()*260;
  n.x = Math.cos(a)*r; n.y = Math.sin(a)*r; n.vx = 0; n.vy = 0;
  n.r = 2.6 + Math.sqrt(n.deg)*1.9;            // radius by connectedness
  n.m = 1 + n.deg*0.16;                         // heavier hubs settle centrally
  n.orphan = n.deg === 0;                       // drifts to the rim as a far star
  if (n.orphan) n.r = 1.9;
});

/* ---------- halo sprites: pre-rendered so the bloom is cheap ---------- */
const SPRITE = {}, SPR = 128;
function sprite(color){
  if (SPRITE[color]) return SPRITE[color];
  const s = document.createElement('canvas'); s.width = s.height = SPR;
  const g = s.getContext('2d');
  const grd = g.createRadialGradient(SPR/2,SPR/2,0,SPR/2,SPR/2,SPR/2);
  grd.addColorStop(0,   color);
  grd.addColorStop(0.14, color + 'CC');
  grd.addColorStop(0.38, color + '3A');
  grd.addColorStop(1,   color + '00');
  g.fillStyle = grd; g.fillRect(0,0,SPR,SPR);
  SPRITE[color] = s; return s;
}
N.forEach(n=>sprite(n.color));

/* ---------- force simulation ---------- */
let alpha = 1;
function step(){
  const REP = 5600, SPRING = 0.027, REST = 88, CENTER = 0.0024;
  for (let i=0;i<N.length;i++){
    const a = N[i];
    for (let j=i+1;j<N.length;j++){
      const b = N[j];
      let dx = b.x-a.x, dy = b.y-a.y;
      let d2 = dx*dx + dy*dy;
      if (d2 < 1e-4){ dx = Math.random()-0.5; dy = Math.random()-0.5; d2 = 1e-4; }
      const d = Math.sqrt(d2);
      const f = Math.min(REP/d2, 40) / d;
      const fx = dx*f, fy = dy*f;
      a.vx -= fx/a.m; a.vy -= fy/a.m;
      b.vx += fx/b.m; b.vy += fy/b.m;
    }
  }
  for (const [s,t] of E){
    const a = N[s], b = N[t];
    const dx = b.x-a.x, dy = b.y-a.y;
    const d = Math.hypot(dx,dy) || 1e-4;
    const f = (d - REST) * SPRING;
    const fx = dx/d*f, fy = dy/d*f;
    a.vx += fx/a.m; a.vy += fy/a.m;
    b.vx -= fx/b.m; b.vy -= fy/b.m;
  }
  for (const n of N){
    n.vx -= n.x*CENTER; n.vy -= n.y*CENTER;
    n.vx *= 0.86; n.vy *= 0.86;
    n.x += n.vx*alpha; n.y += n.vy*alpha;
  }
  alpha *= 0.994;
}
for (let i=0;i<260;i++) step();   // settle before first paint

/* ---------- view ---------- */
let scale = 1, ox = 0, oy = 0, hover = -1, t0 = performance.now();
function fit(){
  // Frame the connected brain, not the orphan stars drifting at the rim.
  const core = N.filter(n=>!n.orphan);
  const set = core.length ? core : N;
  let minx=1e9,maxx=-1e9,miny=1e9,maxy=-1e9;
  for (const n of set){ minx=Math.min(minx,n.x); maxx=Math.max(maxx,n.x); miny=Math.min(miny,n.y); maxy=Math.max(maxy,n.y); }
  const w = maxx-minx || 1, h = maxy-miny || 1;
  scale = Math.min(W/(w+110), H/(h+110));
  ox = W/2 - (minx+maxx)/2*scale;
  oy = H/2 - (miny+maxy)/2*scale;
}
const sx = n => n.x*scale + ox, sy = n => n.y*scale + oy;

function resize(){
  W = cv.clientWidth; H = cv.clientHeight;
  cv.width = W*DPR; cv.height = H*DPR;
  ctx.setTransform(DPR,0,0,DPR,0,0);
  fit();
}
window.addEventListener('resize', resize);

/* ---------- render ---------- */
function draw(now){
  const t = (now - t0) / 1000;

  // deep space + nebula
  ctx.globalCompositeOperation = 'source-over';
  ctx.fillStyle = '#050510'; ctx.fillRect(0,0,W,H);
  const neb = [
    [0.16*W, 0.14*H, Math.max(W,H)*0.55, 'rgba(124,58,237,0.26)'],
    [0.85*W, 0.22*H, Math.max(W,H)*0.46, 'rgba(232,121,249,0.18)'],
    [0.52*W, 0.95*H, Math.max(W,H)*0.55, 'rgba(34,211,238,0.15)'],
    [0.78*W, 0.72*H, Math.max(W,H)*0.36, 'rgba(251,146,60,0.11)'],
  ];
  ctx.globalCompositeOperation = 'lighter';
  for (const [x,y,r,c] of neb){
    const g = ctx.createRadialGradient(x,y,0,x,y,r);
    g.addColorStop(0,c); g.addColorStop(1,'rgba(0,0,0,0)');
    ctx.fillStyle = g; ctx.fillRect(0,0,W,H);
  }

  const near = hover >= 0 ? new Set([hover, ...adj[hover]]) : null;

  // links
  ctx.lineCap = 'round';
  for (const [s,t2] of E){
    const a = N[s], b = N[t2];
    const lit = near && near.has(s) && near.has(t2);
    const dim = near && !lit;
    const g = ctx.createLinearGradient(sx(a),sy(a),sx(b),sy(b));
    const al = lit ? 'DD' : (dim ? '12' : '4A');
    g.addColorStop(0, a.color + al);
    g.addColorStop(1, b.color + al);
    ctx.strokeStyle = g;
    ctx.lineWidth = (lit ? 1.7 : 0.85) * Math.max(scale, 0.55);
    ctx.beginPath(); ctx.moveTo(sx(a),sy(a)); ctx.lineTo(sx(b),sy(b)); ctx.stroke();
  }

  // halos, then cores
  for (let i=0;i<N.length;i++){
    const n = N[i];
    const lit = near ? near.has(i) : true;
    const pulse = 1 + Math.sin(t*1.1 + i*0.7)*0.05;
    const rad = n.r * scale * pulse;
    const halo = rad * (lit ? 7.5 : 4.5) * (n.orphan ? 0.75 : 1);
    ctx.globalAlpha = (lit ? 0.95 : 0.22) * (n.orphan ? 0.5 : 1);
    ctx.drawImage(sprite(n.color), sx(n)-halo, sy(n)-halo, halo*2, halo*2);
  }
  ctx.globalAlpha = 1;
  ctx.globalCompositeOperation = 'lighter';
  for (let i=0;i<N.length;i++){
    const n = N[i];
    const lit = near ? near.has(i) : true;
    const pulse = 1 + Math.sin(t*1.1 + i*0.7)*0.05;
    ctx.beginPath();
    ctx.arc(sx(n), sy(n), Math.max(n.r*scale*pulse*0.62, 1.1), 0, Math.PI*2);
    ctx.fillStyle = lit ? '#FFFFFF' : n.color + '99';
    ctx.fill();
  }

  // labels: hubs when zoomed in, plus the hovered neighbourhood
  ctx.globalCompositeOperation = 'source-over';
  ctx.font = '500 10.5px "JetBrains Mono", monospace';
  ctx.textAlign = 'center';
  for (let i=0;i<N.length;i++){
    const n = N[i];
    const show = (near && near.has(i)) || (!near && scale > 2.2 && n.deg >= 8);
    if (!show) continue;
    const y = sy(n) - n.r*scale - 11;
    ctx.fillStyle = 'rgba(5,5,16,0.72)';
    const w = ctx.measureText(n.id).width;
    ctx.fillRect(sx(n)-w/2-5, y-10, w+10, 14);
    ctx.fillStyle = i === hover ? '#FFFFFF' : '#C4C8F0';
    ctx.fillText(n.id, sx(n), y);
  }

  requestAnimationFrame(draw);
}

/* ---------- interaction ---------- */
function pick(mx,my){
  let best = -1, bd = 20*20;
  for (let i=0;i<N.length;i++){
    const dx = mx-sx(N[i]), dy = my-sy(N[i]);
    const d = dx*dx+dy*dy;
    const rr = Math.max(N[i].r*scale + 7, 9);
    if (d < rr*rr && d < bd){ bd = d; best = i; }
  }
  return best;
}

let dragging = false, lastX = 0, lastY = 0, moved = 0;
cv.addEventListener('pointerdown', e=>{ dragging = true; moved = 0; lastX = e.clientX; lastY = e.clientY; cv.classList.add('dragging'); cv.setPointerCapture(e.pointerId); });
cv.addEventListener('pointerup', e=>{
  dragging = false; cv.classList.remove('dragging');
  if (moved < 5){
    const i = pick(e.clientX, e.clientY);
    if (i >= 0){
      const url = 'obsidian://open?vault=' + encodeURIComponent(DATA.vault) + '&file=' + encodeURIComponent(N[i].path);
      window.location.href = url;
    }
  }
});
cv.addEventListener('pointermove', e=>{
  if (dragging){
    const dx = e.clientX-lastX, dy = e.clientY-lastY;
    moved += Math.abs(dx)+Math.abs(dy);
    ox += dx; oy += dy; lastX = e.clientX; lastY = e.clientY;
    tip.style.opacity = 0; hover = -1;
    return;
  }
  const i = pick(e.clientX, e.clientY);
  hover = i;
  if (i >= 0){
    tip.querySelector('.t').textContent = N[i].id;
    tip.querySelector('.s').textContent = N[i].folder + '  ·  ' + N[i].deg + ' links';
    tip.style.left = sx(N[i]) + 'px';
    tip.style.top = (sy(N[i]) - N[i].r*scale - 16) + 'px';
    tip.style.opacity = 1;
    cv.style.cursor = 'pointer';
  } else {
    tip.style.opacity = 0;
    cv.style.cursor = 'grab';
  }
});
cv.addEventListener('wheel', e=>{
  e.preventDefault();
  const k = Math.exp(-e.deltaY * 0.0016);
  const nx = (e.clientX - ox)/scale, ny = (e.clientY - oy)/scale;
  scale = Math.min(Math.max(scale*k, 0.25), 6);
  ox = e.clientX - nx*scale; oy = e.clientY - ny*scale;
}, {passive:false});

resize();
requestAnimationFrame(draw);
</script>
</body></html>
"""

if __name__ == "__main__":
    build()
