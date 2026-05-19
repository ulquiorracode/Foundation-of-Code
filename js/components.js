// ─── SHARED COMPONENTS ────────────────────────────────────────────────────────

function makeTag(label, color) {
  const c = color || '#6366f1';
  return `<span class="tag" style="background:${c}22;color:${c};border-color:${c}44">${label}</span>`;
}

function makeDifficulty(level) {
  const dots = [1, 2, 3].map(n => `<span class="${n <= level ? 'on' : 'off'}"></span>`).join('');
  return `<span class="difficulty">${dots}</span>`;
}

function makeConceptCard(concept, base) {
  const b = base || 'pages/';
  const langs = concept.langs.map(l => `<span class="lang-tag">${l}</span>`).join('');
  return `
  <a href="${b}concepts.html" class="concept-card">
    <div class="card-top">
      <span class="icon">${concept.icon}</span>
      ${makeDifficulty(concept.difficulty)}
    </div>
    <div class="tag-row">${makeTag(concept.tag)}</div>
    <h3>${concept.title}</h3>
    <p>${concept.desc}</p>
    <div class="lang-tags">${langs}</div>
  </a>`;
}

function makeRoadmapCard(roadmap, base) {
  const b = base || 'pages/';
  const steps = roadmap.steps.slice(0, 3).map((s, i) =>
    `<div class="step-row">
       <span class="step-num" style="background:${roadmap.color}22;color:${roadmap.color}">${i + 1}</span>
       <span class="step-title">${s.title}</span>
     </div>`
  ).join('');
  const more = roadmap.steps.length > 3
    ? `<div class="step-title" style="margin-left:30px;font-size:12px">+ ещё ${roadmap.steps.length - 3} шага</div>` : '';
  return `
  <a href="${b}roadmaps.html" class="roadmap-card"
     onmouseenter="this.style.background='${roadmap.color}10';this.style.borderColor='${roadmap.color}44'"
     onmouseleave="this.style.background='';this.style.borderColor=''">
    <div class="ricon">${roadmap.icon}</div>
    <h3>${roadmap.title}</h3>
    <div class="meta">${makeTag(roadmap.level, roadmap.color)}<span class="duration">⏱ ${roadmap.duration}</span></div>
    <div class="steps-preview">${steps}${more}</div>
  </a>`;
}

function makeArticleCard(article, base) {
  const b = base || 'pages/';
  return `
  <a href="${b}articles.html?id=${article.id}" class="article-card">
    <div class="card-top">${makeTag(article.tag)}<span class="read-time">${article.readTime}</span></div>
    <h3>${article.title}</h3>
    <p>${article.excerpt}</p>
    <div class="footer-row"><span class="author">${article.author}</span><span class="date">${article.date}</span></div>
  </a>`;
}

// ─── NAVBAR ────────────────────────────────────────────────────────────────────

function _buildNavbar(links, logoHref, ctaHref) {
  const lis = links.map(l =>
    `<li><a href="${l.href}" class="${l.active ? 'active' : ''}">${l.label}</a></li>`
  ).join('');
  // Auth-aware CTA
  const _navUser = typeof Auth !== 'undefined' ? Auth.current() : null;
  const _ctaHtml = _navUser
    ? `<a href="${ctaHref.replace('register.html', 'profile.html').replace('pages/register.html', 'pages/profile.html')}" class="nav-cta" style="display:flex;align-items:center;gap:7px">
         <span style="width:24px;height:24px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;color:#fff;flex-shrink:0">${Auth.avatarLetter(_navUser)}</span>
         ${_navUser.firstName}
       </a>`
    : `<a href="${ctaHref}" class="nav-cta">Войти</a>`;
  document.getElementById('navbar').innerHTML = `
    <div class="container">
      <a href="${logoHref}" class="nav-logo">
        <div class="logo-icon">F</div>
        Foundation<span class="dot">.</span>of<span class="dot">.</span>Code
      </a>
      <ul class="nav-links">${lis}</ul>
      ${_ctaHtml}
    </div>`;
}

function renderNavbar(activePage) {
  _buildNavbar([
    { href: '../index.html', label: 'Главная', active: activePage === 'home' },
    { href: 'concepts.html', label: 'Концепции', active: activePage === 'concepts' },
    { href: 'roadmaps.html', label: 'Роудмапы', active: activePage === 'roadmaps' },
    { href: 'languages.html', label: 'Языки', active: activePage === 'languages' },
    { href: 'articles.html', label: 'Статьи', active: activePage === 'articles' },
    { href: 'pricing.html', label: 'Цены', active: activePage === 'pricing' },
    { href: '../pages/about.html', label: 'О нас', active: activePage === 'about' },
  ], '../index.html', 'register.html');
}

function renderNavbarRoot(activePage) {
  _buildNavbar([
    { href: 'index.html', label: 'Главная', active: activePage === 'home' },
    { href: 'pages/concepts.html', label: 'Концепции', active: activePage === 'concepts' },
    { href: 'pages/roadmaps.html', label: 'Роудмапы', active: activePage === 'roadmaps' },
    { href: 'pages/languages.html', label: 'Языки', active: activePage === 'languages' },
    { href: 'pages/articles.html', label: 'Статьи', active: activePage === 'articles' },
    { href: 'pages/pricing.html', label: 'Цены', active: activePage === 'pricing' },
    { href: 'pages/about.html', label: 'О нас', active: activePage === 'about' },
  ], 'index.html', 'pages/register.html');
}

// ─── FOOTER ────────────────────────────────────────────────────────────────────

function renderFooter(isRoot) {
  const b = isRoot ? '' : '../';
  document.getElementById('footer').innerHTML = `
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="nav-logo" style="margin-bottom:0">
            <div class="logo-icon">F</div>
            Foundation of Code
          </div>
          <p>Централизованная образовательная платформа для изучения фундаментальных концепций программирования.</p>
        </div>
        <div class="footer-col">
          <h4>Учёба</h4>
          <a href="${b}pages/concepts.html">Концепции</a>
          <a href="${b}pages/roadmaps.html">Роудмапы</a>
          <a href="${b}pages/articles.html">Статьи</a>
        </div>
        <div class="footer-col">
          <h4>Платформа</h4>
          <a href="${b}pages/pricing.html">Цены</a>
          <a href="${b}pages/about.html">О нас</a>
          <a href="${b}pages/team.html">Команда</a>
          <a href="${b}pages/register.html">Регистрация</a>
        </div>
        <div class="footer-col">
          <h4>Языки</h4>
          <a href="${b}pages/languages.html">Python</a>
          <a href="${b}pages/languages.html">C</a>
          <a href="${b}pages/languages.html">JavaScript</a>
          <a href="${b}pages/languages.html">C#</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 Foundation of Code · Университетский проект</span>
        <div style="display:flex;gap:16px;">
          <a href="${b}pages/terms.html" style="color:rgba(255,255,255,0.25);text-decoration:none;font-size:13px;transition:color 0.15s" onmouseenter="this.style.color='#a5b4fc'" onmouseleave="this.style.color='rgba(255,255,255,0.25)'">Условия использования</a>
          <a href="${b}pages/privacy.html" style="color:rgba(255,255,255,0.25);text-decoration:none;font-size:13px;transition:color 0.15s" onmouseenter="this.style.color='#a5b4fc'" onmouseleave="this.style.color='rgba(255,255,255,0.25)'">Конфиденциальность</a>
        </div>
        <span class="version">MVP v0.1.0</span>
      </div>
    </div>`;
}
