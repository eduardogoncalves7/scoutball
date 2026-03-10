// ============================================================
//  ScoutBall — Lógica principal
//  Série A Brasileirão 2025 · FBRef Data
// ============================================================

// ── CÁLCULOS ──────────────────────────────────────────────────
function getG90(p)      { return p.g90 ?? 0; }
function getMatches(p)  { return p.minutes > 0 ? (p.minutes / 90).toFixed(1) : "0.0"; }

function getRating(g90) {
  if (g90 >= 0.65) return { label: "ELITE", cls: "rating-elite" };
  if (g90 >= 0.25) return { label: "SOLID", cls: "rating-good"  };
  return               { label: "AVG",   cls: "rating-avg"   };
}

// ── POPULA FILTROS DINÂMICOS ────────────────────────────────────
function populateFilters() {
  const clubs = [...new Set(PLAYERS.map(p => p.club))].sort();
  const sel   = document.getElementById('filter-club');
  clubs.forEach(c => {
    const o = document.createElement('option');
    o.value = o.textContent = c;
    sel.appendChild(o);
  });
}

// ── FILTROS ─────────────────────────────────────────────────────
function getFilters() {
  return {
    pos:    document.getElementById('filter-pos').value,
    club:   document.getElementById('filter-club').value,
    maxAge: +document.getElementById('filter-age').value,
    minG90: +document.getElementById('filter-g90').value,
    minMin: +document.getElementById('filter-min').value,
    sort:   document.getElementById('filter-sort').value,
  };
}

function filterAndSort(players, f) {
  const result = players.filter(p =>
    (!f.pos  || p.pos  === f.pos)  &&
    (!f.club || p.club === f.club) &&
    p.age     <= f.maxAge &&
    getG90(p) >= f.minG90 &&
    p.minutes >= f.minMin
  );
  result.sort((a, b) => {
    if (f.sort === 'g90')     return getG90(b)   - getG90(a);
    if (f.sort === 'goals')   return b.goals      - a.goals;
    if (f.sort === 'shots')   return b.shots      - a.shots;
    if (f.sort === 'shot_acc')return b.shot_acc   - a.shot_acc;
    if (f.sort === 'age')     return a.age        - b.age;
    if (f.sort === 'minutes') return b.minutes    - a.minutes;
    return 0;
  });
  return result;
}

// ── RENDER ───────────────────────────────────────────────────────
function renderGrid(filtered) {
  const grid  = document.getElementById('players-grid');
  const badge = document.getElementById('count-badge');
  badge.textContent = `${filtered.length} resultado${filtered.length !== 1 ? 's' : ''}`;

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div class="icon">⚽</div>
        <p>NENHUM JOGADOR ENCONTRADO COM ESSES FILTROS</p>
      </div>`;
    return;
  }

  const maxG90 = Math.max(...filtered.map(getG90), 0.01);

  grid.innerHTML = filtered.map((p, i) => {
    const val   = getG90(p);
    const r     = getRating(val);
    const pct   = Math.min((val / maxG90) * 100, 100).toFixed(1);
    const delay = Math.min(i * 0.04, 0.8);
    const idx   = PLAYERS.indexOf(p);
    const shotPct = p.shot_acc ? `${p.shot_acc}%` : '—';

    return `
      <div class="player-card" style="animation-delay:${delay}s" onclick="openModal(${idx})">
        <div class="card-top">
          <div class="player-name">${p.name}</div>
          <span class="rating-badge ${r.cls}">${r.label}</span>
        </div>
        <div class="card-meta">
          <span class="meta-tag">${p.pos}</span>
          <span class="meta-tag">${p.age} anos</span>
          <span class="meta-tag">${p.country}</span>
          <span class="meta-tag">${p.club}</span>
        </div>
        <div class="stats-row">
          <div class="stat-box">
            <span class="stat-value highlight">${val.toFixed(2)}</span>
            <span class="stat-label">G/90</span>
          </div>
          <div class="stat-box">
            <span class="stat-value">${p.goals}</span>
            <span class="stat-label">Gols</span>
          </div>
          <div class="stat-box">
            <span class="stat-value">${p.shots}</span>
            <span class="stat-label">Chutes</span>
          </div>
        </div>
        <div class="g90-bar-wrap">
          <div class="bar-label">
            <span>EFICIÊNCIA G/90</span>
            <span style="color:var(--green)">${val.toFixed(2)}</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill" style="width:${pct}%"></div>
          </div>
        </div>
      </div>`;
  }).join('');
}

// ── MODAL ────────────────────────────────────────────────────────
function openModal(idx) {
  const p   = PLAYERS[idx];
  const val = getG90(p);
  const r   = getRating(val);
  const shotPct = p.shot_acc ? `${p.shot_acc}%` : '—';

  document.getElementById('modal-body').innerHTML = `
    <div class="modal-name">${p.name}</div>
    <div class="modal-sub">${p.pos.toUpperCase()} · ${p.club} · ${p.league}</div>
    <div class="modal-stats">
      <div class="modal-stat">
        <div class="modal-stat-value">${val.toFixed(2)}</div>
        <div class="modal-stat-label">Gols por 90 min</div>
      </div>
      <div class="modal-stat">
        <div class="modal-stat-value">${p.goals}</div>
        <div class="modal-stat-label">Gols totais</div>
      </div>
      <div class="modal-stat">
        <div class="modal-stat-value">${p.shots}</div>
        <div class="modal-stat-label">Chutes totais</div>
      </div>
      <div class="modal-stat">
        <div class="modal-stat-value">${p.shots_ot}</div>
        <div class="modal-stat-label">Chutes no gol</div>
      </div>
    </div>
    <div class="modal-info-grid">
      <div class="info-row">
        <span>Idade</span><span>${p.age} anos</span>
      </div>
      <div class="info-row">
        <span>País</span><span>${p.country}</span>
      </div>
      <div class="info-row">
        <span>Minutos jogados</span><span>${p.minutes.toLocaleString('pt-BR')}</span>
      </div>
      <div class="info-row">
        <span>Partidas estimadas</span><span>${getMatches(p)}</span>
      </div>
      <div class="info-row">
        <span>Precisão de chutes</span><span>${shotPct}</span>
      </div>
      <div class="info-row">
        <span>Rating</span>
        <span class="rating-badge ${r.cls}" style="font-size:0.7rem">${r.label}</span>
      </div>
    </div>`;

  document.getElementById('modal').classList.add('open');
}

function closeModal(e) {
  if (e.target === document.getElementById('modal')) closeModalBtn();
}
function closeModalBtn() {
  document.getElementById('modal').classList.remove('open');
}

// ── EVENTOS ──────────────────────────────────────────────────────
document.getElementById('filter-age').addEventListener('input', function () {
  document.getElementById('age-val').textContent = this.value;
});
document.getElementById('filter-g90').addEventListener('input', function () {
  document.getElementById('g90-val').textContent = (+this.value).toFixed(2);
});
document.getElementById('filter-min').addEventListener('input', function () {
  document.getElementById('min-val').textContent = this.value;
});

function applyFilters() {
  const filtered = filterAndSort(PLAYERS, getFilters());
  renderGrid(filtered);
}

// ── INIT ─────────────────────────────────────────────────────────
populateFilters();
applyFilters();
