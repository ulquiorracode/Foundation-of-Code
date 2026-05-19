import os
import subprocess
import sys

def get_html_content():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Foundation of Code Presentation</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

@page {
    size: 297mm 167.0625mm;
    margin: 0;
}
* {
    box-sizing: border-box;
}
html, body {
    margin: 0;
    padding: 0;
    background-color: #0b0f19;
    font-family: 'Outfit', sans-serif;
    color: #f8fafc;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
.slide {
    width: 297mm;
    height: 167.0625mm;
    padding: 12mm 18mm;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    page-break-after: always;
    break-after: page;
    
    /* Premium background grid + glows */
    background-color: #0b0f19;
    background-image: 
        radial-gradient(at 0% 0%, rgba(129, 140, 248, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 0%, rgba(56, 189, 248, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(167, 139, 250, 0.08) 0px, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.007) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.007) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 100% 100%, 30px 30px, 30px 30px;
}
.slide:last-child {
    page-break-after: avoid;
    break-after: avoid;
}

/* Slide Header */
.slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 8px;
    margin-bottom: 18px;
    width: 100%;
}
.header-project {
    font-size: 12px;
    font-weight: 800;
    color: #38bdf8;
    letter-spacing: 2px;
}
.header-section {
    font-size: 12px;
    font-weight: 600;
    color: #64748b;
    letter-spacing: 1px;
}

/* Slide Title */
.slide-title {
    font-size: 34px;
    font-weight: 700;
    color: #ffffff;
    margin-top: 0;
    margin-bottom: 22px;
    letter-spacing: -0.8px;
}

/* Slide Title Layout */
.slide-title-layout {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    padding: 0 10mm;
}
.title-container {
    max-width: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.project-tag {
    font-size: 13px;
    font-weight: 800;
    color: #38bdf8;
    letter-spacing: 3px;
    margin-bottom: 16px;
}
.main-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 18px 0;
    letter-spacing: -2px;
    background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 18px;
    line-height: 1.5;
    color: #94a3b8;
    margin: 0 0 35px 0;
}
.group-info {
    font-size: 15px;
    font-weight: 600;
    color: #64748b;
    letter-spacing: 1px;
}
.title-decor {
    width: 35%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.decor-card {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 16px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
    width: 100%;
    max-width: 320px;
}
.decor-accent {
    font-family: 'JetBrains Mono', monospace;
    font-size: 40px;
    font-weight: bold;
    color: #38bdf8;
    display: block;
    margin-bottom: 12px;
}
.decor-text {
    font-size: 16px;
    color: #cbd5e1;
    margin: 0;
}

/* Grid Layouts */
.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}
.grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
}
.grid-5 {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
}

/* Card Styling */
.card {
    background: rgba(30, 41, 59, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.card-title {
    font-size: 20px;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 12px;
    letter-spacing: -0.3px;
}
.card-body {
    font-size: 15px;
    line-height: 1.55;
    color: #cbd5e1;
    margin: 0;
}

/* Bullets */
.bullets {
    margin: 0;
    padding: 0 0 0 18px;
    font-size: 14.5px;
    line-height: 1.55;
    color: #cbd5e1;
}
.bullets li {
    margin-bottom: 8px;
}
.bullets li strong {
    color: #ffffff;
}

/* Border styles */
.border-sky { border-left: 4px solid #38bdf8; }
.border-indigo { border-left: 4px solid #818cf8; }
.border-emerald { border-left: 4px solid #34d399; }
.border-violet { border-left: 4px solid #a78bfa; }
.border-amber { border-left: 4px solid #f59e0b; }
.border-slate { border: 1px solid rgba(255, 255, 255, 0.08); }

.text-sky { color: #38bdf8; }
.text-indigo { color: #818cf8; }
.text-emerald { color: #34d399; }
.text-violet { color: #a78bfa; }
.text-amber { color: #f59e0b; }

/* Goal layout (Slide 4) */
.grid-goals {
    display: grid;
    grid-template-columns: 4.8fr 7.2fr;
    gap: 24px;
    align-items: stretch;
}
.goal-left-card {
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.12) 0%, rgba(129, 140, 248, 0.12) 100%);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 14px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.goal-badge {
    background: #38bdf8;
    color: #0f172a;
    font-weight: 800;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 20px;
    align-self: flex-start;
    margin-bottom: 16px;
    letter-spacing: 1.5px;
}
.goal-text {
    font-size: 21px;
    line-height: 1.55;
    margin: 0;
    color: #ffffff;
    font-weight: 500;
}
.tasks-right-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.task-item {
    background: rgba(30, 41, 59, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.04);
    border-radius: 10px;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 18px;
}
.task-num {
    font-size: 26px;
    font-weight: 800;
    color: #818cf8;
}
.task-desc {
    font-size: 14.5px;
    line-height: 1.5;
    color: #cbd5e1;
}

/* Team layout (Slide 5) */
.team-card {
    background: rgba(30, 41, 59, 0.35);
    border-radius: 12px;
    padding: 18px;
    display: flex;
    flex-direction: column;
}
.team-name {
    font-size: 17px;
    font-weight: bold;
    margin-bottom: 4px;
}
.team-role {
    font-size: 11px;
    color: #94a3b8;
    margin-bottom: 14px;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.team-bullets {
    margin: 0;
    padding: 0 0 0 12px;
    font-size: 12.5px;
    line-height: 1.5;
    color: #cbd5e1;
}
.team-bullets li {
    margin-bottom: 8px;
}

/* Section Divider Slide (Slide 6) */
.slide-divider {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 0 20mm;
}
.divider-left {
    font-size: 140px;
    font-weight: 800;
    color: #38bdf8;
    line-height: 1;
    margin-right: 35px;
    letter-spacing: -4px;
}
.divider-line {
    width: 3px;
    height: 100px;
    background: linear-gradient(180deg, #38bdf8 0%, #818cf8 100%);
    margin-right: 35px;
}
.divider-right {
    display: flex;
    flex-direction: column;
    max-width: 60%;
}
.divider-title {
    font-size: 42px;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: 1px;
}
.divider-subtitle {
    font-size: 16px;
    line-height: 1.55;
    color: #94a3b8;
    margin: 0;
}

/* Tech Stack (Slide 10) */
.tech-card {
    background: rgba(30, 41, 59, 0.35);
    border-radius: 12px;
    padding: 22px 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    justify-content: center;
}
.tech-icon {
    font-size: 20px;
    font-weight: 800;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
}
.tech-desc {
    font-size: 13px;
    line-height: 1.5;
    color: #cbd5e1;
}

/* Universal Showcase Layout (Slides 11-15) */
.slide-showcase {
    display: grid;
    grid-template-columns: 4.8fr 7.2fr;
    gap: 24px;
    align-items: stretch;
    height: 400px;
}
.showcase-image-box {
    background: rgba(15, 23, 42, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: stretch;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    height: 100%;
}
.showcase-image-box img {
    width: 100%;
    height: 330px;
    object-fit: fill;
    border-radius: 10px;
    image-rendering: -webkit-optimize-contrast;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}
.showcase-caption {
    font-size: 13px;
    color: #64748b;
    text-align: center;
    margin-top: 10px;
    font-weight: 600;
    letter-spacing: 0.2px;
}

/* Slide 17: Outro Slide */
.slide-outro {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.outro-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.outro-tag {
    font-size: 18px;
    font-weight: 800;
    color: #38bdf8;
    letter-spacing: 4px;
    margin-bottom: 18px;
}
.outro-main {
    font-size: 60px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 15px 0;
    letter-spacing: 0.5px;
    background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.outro-sub {
    font-size: 22px;
    color: #94a3b8;
    margin: 0 0 35px 0;
}
.outro-logo-box {
    width: 150px;
}
.outro-logo-box img {
    width: 100%;
    height: auto;
}
</style>
</head>
<body>

<!-- Slide 1: Title -->
<div class="slide slide-title-layout">
  <div class="title-container">
    <div class="project-tag">ПРОЕКТНАЯ ДЕЯТЕЛЬНОСТЬ &nbsp;•&nbsp; ЮЖНЫЙ ФЕДЕРАЛЬНЫЙ УНИВЕРСИТЕТ</div>
    <h1 class="main-title">FOUNDATION OF CODE</h1>
    <p class="subtitle">Интерактивная SPA-платформа для декомпозиции фундаментальных концепций программирования и кросс-языкового анализа</p>
    <div class="group-info">Группа 25ВТ–09.03.03.01–о1</div>
  </div>
  <div class="title-decor">
     <div class="decor-card">
       <span class="decor-accent">&lt;code&gt;</span>
       <p class="decor-text">Декомпозиция абстракций</p>
     </div>
  </div>
</div>

<!-- Slide 2: Problem & Relevance -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">01 / ВВЕДЕНИЕ</span>
  </div>
  <h2 class="slide-title">Проблема и актуальность</h2>
  <div class="grid-2">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Синтаксический диссонанс</h3>
      <p class="card-body">Изучение синтаксиса высокоуровневых языков программирования без понимания физической архитектуры памяти и компиляции.</p>
    </div>
    <div class="card border-indigo">
      <h3 class="card-title text-indigo">Информационный хаос</h3>
      <p class="card-body">Отсутствие структурированного User Flow и единой точки входа для агрегации и декомпозиции сложных обучающих материалов.</p>
    </div>
    <div class="card border-emerald">
      <h3 class="card-title text-emerald">Изолированность контекстов</h3>
      <p class="card-body">Изучение современных фреймворков и библиотек в отрыве от низкоуровневого выполнения (Runtime) и распределения памяти.</p>
    </div>
    <div class="card border-violet">
      <h3 class="card-title text-violet">Актуальность</h3>
      <p class="card-body">Необходимость в платформе с интегрированными Roadmaps для фасилитации процесса онбординга в Computer Science.</p>
    </div>
  </div>
</div>

<!-- Slide 3: Our Solution -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">01 / ВВЕДЕНИЕ</span>
  </div>
  <h2 class="slide-title">Наше решение: Foundation of Code</h2>
  <div class="grid-2">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Интегрированный SPA-хаб</h3>
      <p class="card-body">Централизованная интерактивная база с модульной архитектурой образовательного контента.</p>
    </div>
    <div class="card border-indigo">
      <h3 class="card-title text-indigo">Низкоуровневая декомпозиция</h3>
      <p class="card-body">Пошаговое объяснение алгоритмов через призму аллокации памяти, указателей и физического устройства железа.</p>
    </div>
    <div class="card border-emerald">
      <h3 class="card-title text-emerald">Кросс-языковой анализ</h3>
      <p class="card-body">Сравнительное сопоставление синтаксических конструкций C, Python и JS в рамках одного экрана в реальном времени.</p>
    </div>
    <div class="card border-violet">
      <h3 class="card-title text-violet">Интерактивный стейт-трекинг</h3>
      <p class="card-body">Геймифицированные дорожные карты с сохранением стейта (прогресса) пользователя через LocalStorage API.</p>
    </div>
  </div>
</div>

<!-- Slide 4: Goals & Objectives -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">01 / ВВЕДЕНИЕ</span>
  </div>
  <h2 class="slide-title">Цели и задачи проекта</h2>
  <div class="grid-goals">
    <div class="goal-left-card">
      <div class="goal-badge">ЦЕЛЬ MVP</div>
      <p class="goal-text">Проектирование и разработка масштабируемого SPA-приложения с интерактивным кросс-языковым модулем и сохранением клиентского стейта.</p>
    </div>
    <div class="tasks-right-container">
      <div class="task-item">
        <div class="task-num">01</div>
        <div class="task-desc">Провести системный бенчмаркинг и конкурентный анализ образовательных платформ (MDN, W3Schools, Stepik).</div>
      </div>
      <div class="task-item">
        <div class="task-num">02</div>
        <div class="task-desc">Разработать информационную архитектуру, User Flow и дизайн-систему (UI Kit) в Figma.</div>
      </div>
      <div class="task-item">
        <div class="task-num">03</div>
        <div class="task-desc">Реализовать адаптивную верстку по методологии Mobile First, SPA-роутинг и динамический рендеринг представлений.</div>
      </div>
      <div class="task-item">
        <div class="task-num">04</div>
        <div class="task-desc">Интегрировать механизм персистентности данных (LocalStorage API) и провести комплексный QA-аудит.</div>
      </div>
    </div>
  </div>
</div>

<!-- Slide 5: Developers -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">01 / ВВЕДЕНИЕ</span>
  </div>
  <h2 class="slide-title">Разработчики и распределение обязанностей</h2>
  <div class="grid-4">
    <!-- Col 1 -->
    <div class="team-card border-sky">
      <div class="team-name text-sky">Егор Бобровских</div>
      <div class="team-role">Тимлид, Product Owner, UX/UI</div>
      <ul class="team-bullets">
        <li><strong>Product Management:</strong> фасилитация процессов, Scrum-планирование спринтов.</li>
        <li><strong>UX/UI Prototyping:</strong> создание дизайн-системы, UI Kit и интерактивных варфреймов в Figma.</li>
        <li><strong>Design Review:</strong> валидация верстки на соответствие Pixel Perfect макетам.</li>
      </ul>
    </div>
    <!-- Col 2 -->
    <div class="team-card border-indigo">
      <div class="team-name text-indigo">Вячеслав Федоренко</div>
      <div class="team-role">Fullstack Developer</div>
      <ul class="team-bullets">
        <li><strong>SPA Architecture:</strong> реализация клиентского роутинга и логики управления стейтом.</li>
        <li><strong>Front-end Development:</strong> семантическая верстка, CSS Flexbox/Grid разметка.</li>
        <li><strong>DOM Manipulation:</strong> написание асинхронных обработчиков событий для переключения синтаксиса.</li>
      </ul>
    </div>
    <!-- Col 3 -->
    <div class="team-card border-emerald">
      <div class="team-name text-emerald">Александр Владимиров</div>
      <div class="team-role">Content Product Manager</div>
      <ul class="team-bullets">
        <li><strong>Market Research:</strong> бенчмаркинг образовательных платформ и анализ болей целевой аудитории.</li>
        <li><strong>Information Architecture:</strong> проектирование контент-структуры и дорожных карт.</li>
        <li><strong>Content Engineering:</strong> декомпозиция тем и составление кросс-языковых примеров.</li>
      </ul>
    </div>
    <!-- Col 4 -->
    <div class="team-card border-amber">
      <div class="team-name text-amber">Георгий Литвиненко</div>
      <div class="team-role">QA / Release Engineer</div>
      <ul class="team-bullets">
        <li><strong>Quality Assurance:</strong> проведение функционального, регрессионного и кроссбраузерного тестирования.</li>
        <li><strong>State Testing:</strong> валидация персистентности данных в LocalStorage.</li>
        <li><strong>Bug Tracking:</strong> документирование дефектов, ведение логов ошибок и контроль фиксов.</li>
      </ul>
    </div>
  </div>
</div>

<!-- Slide 6: Section Divider -->
<div class="slide slide-divider">
  <div class="divider-left">02</div>
  <div class="divider-line"></div>
  <div class="divider-right">
    <h1 class="divider-title">РЕАЛИЗАЦИЯ ПРОЕКТА</h1>
    <p class="divider-subtitle">Архитектура решения, технологический стек, дизайн-система и техническая реализация</p>
  </div>
</div>

<!-- Slide 7: Subject Area & Target Audience -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Анализ предметной области и целевой аудитории</h2>
  <div class="grid-2">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Сегментация целевой аудитории</h3>
      <ul class="bullets">
        <li><strong>Junior-разработчики:</strong> начинающие специалисты, требующие систематизации знаний и понимания Runtime.</li>
        <li><strong>Студенты профильных IT-направлений:</strong> обучающиеся по программам Computer Science и инженерии данных.</li>
        <li><strong>Свитчеры (Self-taught):</strong> пользователи, проходящие интенсивную переквалификацию из других отраслей.</li>
      </ul>
    </div>
    <div class="card border-indigo">
      <h3 class="card-title text-indigo">Ключевые боли и запросы аудитории</h3>
      <ul class="bullets">
        <li><strong>Фрагментированность восприятия:</strong> отсутствие понимания связи между кодом и физической памятью.</li>
        <li><strong>Парадигмальный барьер:</strong> сложность сопоставления подходов ООП, процедурного и функционального программирования.</li>
        <li><strong>Низкая интерактивность:</strong> сухая подача материалов без мгновенной визуализации выполнения.</li>
      </ul>
    </div>
  </div>
</div>

<!-- Slide 8: Design and Visuals -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Визуальная концепция и дизайн-система</h2>
  <div class="grid-2">
    <div class="card border-sky">
      <h3 class="card-title text-sky">UI/UX решения</h3>
      <ul class="bullets">
        <li><strong>Схема Dark Mode:</strong> снижение зрительной нагрузки (Eye Strain), адаптация под стандарты сред разработки (IDE).</li>
        <li><strong>Component-Based Layout:</strong> модульная сетка для структурирования информации, повышающая скандируемость контента.</li>
        <li><strong>Responsive Grid:</strong> кросс-девайсная верстка под вьюпорты смартфонов, планшетов и настольных компьютеров.</li>
      </ul>
    </div>
    <div class="card border-indigo">
      <h3 class="card-title text-indigo">Прототипирование в Figma</h3>
      <ul class="bullets">
        <li><strong>Картирование User Flow:</strong> детальная разработка путей перемещения пользователя по разделам SPA.</li>
        <li><strong>Цветовое кодирование:</strong> закрепление HSL-акцентов за языками программирования (C, Python, JS).</li>
        <li><strong>Design-to-Code:</strong> прямой экспорт стилей, сеток и шрифтов в глобальные CSS Custom Properties.</li>
      </ul>
    </div>
  </div>
</div>

<!-- Slide 9: Competitor Analysis -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Бенчмаркинг и конкурентные преимущества</h2>
  <div class="grid-2">
    <div class="card border-emerald">
      <h3 class="card-title text-emerald">Анализ рынка (Бенчмаркинг)</h3>
      <ul class="bullets">
        <li><strong>MDN & W3Schools:</strong> качественная справочная документация, лишенная сквозной методологии обучения.</li>
        <li><strong>Stepik & Codecademy:</strong> изолированные курсы без возможности синхронного кросс-языкового сопоставления.</li>
        <li><strong>Видеоресурсы:</strong> исключительно пассивный контент без практики и контроля состояния прогресса.</li>
      </ul>
    </div>
    <div class="card border-sky">
      <h3 class="card-title text-sky">Наши преимущества</h3>
      <ul class="bullets">
        <li><strong>Синхронный кросс-языковой блок:</strong> сопоставление синтаксиса языков в единой плоскости DOM на лету.</li>
        <li><strong>Низкоуровневая визуализация:</strong> наглядные схемы выделения памяти (стек, куча) под капотом выполнения.</li>
        <li><strong>Персистентный роадмап:</strong> интерактивные дорожные карты с игровыми элементами трекинга стейта.</li>
      </ul>
    </div>
  </div>
</div>

<!-- Slide 10: Tech Stack -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Технологический стек проекта</h2>
  <div class="grid-5">
    <!-- Col 1 -->
    <div class="tech-card border-sky">
      <div class="tech-icon text-sky">HTML5</div>
      <div class="tech-desc">Semantic Markup. Структурирование DOM-дерева, семантическая верстка, оптимизация SEO.</div>
    </div>
    <!-- Col 2 -->
    <div class="tech-card border-indigo">
      <div class="tech-icon text-indigo">CSS3</div>
      <div class="tech-desc">Design Tokens & Grids. Flexbox/Grid разметка, CSS Custom Properties, адаптивные переходы.</div>
    </div>
    <!-- Col 3 -->
    <div class="tech-card border-emerald">
      <div class="tech-icon text-emerald">JavaScript</div>
      <div class="tech-desc">Client-side Routing. Логика SPA-маршрутизации, динамическое обновление DOM, асинхронные события.</div>
    </div>
    <!-- Col 4 -->
    <div class="tech-card border-violet">
      <div class="tech-icon text-violet">LocalStorage</div>
      <div class="tech-desc">Data Persistence. Локальное хранение сессии, стейта и прогресса обучения без оверхеда на БД.</div>
    </div>
    <!-- Col 5 -->
    <div class="tech-card border-sky">
      <div class="tech-icon text-sky">VS Code</div>
      <div class="tech-desc">IDE & Tooling. Интегрированная среда разработки, линтинг кода, отладка и версионирование.</div>
    </div>
  </div>
</div>

<!-- Slide 11: HTML Structure Showcase -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Реализация структуры: HTML5</h2>
  <div class="slide-showcase">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Семантика и архитектура DOM</h3>
      <ul class="bullets">
        <li><strong>Семантические теги:</strong> строгое использование разметки W3C для логической декомпозиции блоков.</li>
        <li><strong>SPA-архитектура:</strong> единая точка входа index.html с динамическим рендерингом представлений (views) через JS.</li>
        <li><strong>Модульность DOM:</strong> отсутствие лишней вложенности, поддержка стандартов чистой разметки и доступности (Accessibility).</li>
      </ul>
    </div>
    <div class="showcase-image-box">
      <img src="docs/media/word/media/Index_Файл.png" alt="Структура HTML">
      <div class="showcase-caption">Архитектура index.html и структура модульных секций</div>
    </div>
  </div>
</div>

<!-- Slide 12: CSS Styling Showcase -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Таблицы стилей: CSS3</h2>
  <div class="slide-showcase">
    <div class="card border-indigo">
      <h3 class="card-title text-indigo">Дизайн-система и темизация</h3>
      <ul class="bullets">
        <li><strong>Дизайн-токены:</strong> применение CSS Custom Properties (переменных) для централизованной темизации.</li>
        <li><strong>Адаптивные сетки:</strong> гибридная верстка CSS Grid + Flexbox для стабильности интерфейса на любых дисплеях.</li>
        <li><strong>Микроанимации:</strong> плавные переходы (transition), эффекты свечения и ховер-состояния карточек.</li>
      </ul>
    </div>
    <div class="showcase-image-box">
      <img src="docs/media/word/media/Css_Файл.png" alt="Таблица стилей CSS">
      <div class="showcase-caption">Глобальные стили css/style.css и конфигурация CSS-переменных</div>
    </div>
  </div>
</div>

<!-- Slide 13: Demo Main Page -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Главная страница платформы</h2>
  <div class="slide-showcase">
    <div class="card border-emerald">
      <h3 class="card-title text-emerald">Интерфейс и навигация</h3>
      <ul class="bullets">
        <li><strong>Премиальный UI:</strong> темно-грифельная тема Slate-Dark с неоновыми цветовыми акцентами для улучшения UX.</li>
        <li><strong>Sidebar Navigation:</strong> боковая панель для бесшовной маршрутизации между модулями платформы.</li>
        <li><strong>Адаптивный вьюпорт:</strong> динамически скрывающийся сайдбар для мобильных девайсов.</li>
      </ul>
    </div>
    <div class="showcase-image-box">
      <img src="docs/media/word/media/Главная_Страница.png" alt="Главная страница">
      <div class="showcase-caption">Интерфейс главной страницы и структура бокового меню</div>
    </div>
  </div>
</div>

<!-- Slide 14: Demo Concepts Page -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Раздел сравнения концепций</h2>
  <div class="slide-showcase">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Реактивный синтаксический модуль</h3>
      <ul class="bullets">
        <li><strong>Таб-контроллеры:</strong> мгновенное переключение синтаксиса (C, Python, JS) без выполнения HTTP-запросов к серверу.</li>
        <li><strong>Двухпанельный вьюпорт:</strong> синхронизация теоретической декомпозиции (слева) с блоком кода (справа).</li>
        <li><strong>Специфика Runtime:</strong> фокус на фундаментальных темах (аллокация памяти, стек, сборка мусора).</li>
      </ul>
    </div>
    <div class="showcase-image-box">
      <img src="docs/media/word/media/Языки_Программирования.png" alt="Сравнение языков">
      <div class="showcase-caption">Интерактивная панель сопоставления кода и переключатель вкладок</div>
    </div>
  </div>
</div>

<!-- Slide 15: Demo Auth & Tariffs Page -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">02 / РЕАЛИЗАЦИЯ</span>
  </div>
  <h2 class="slide-title">Регистрация и тарифные планы</h2>
  <div class="slide-showcase">
    <div class="card border-violet">
      <h3 class="card-title text-violet">Управление доступом и сессией</h3>
      <ul class="bullets">
        <li><strong>Клиентская валидация:</strong> проверка корректности ввода на лету с помощью регулярных выражений (RegExp).</li>
        <li><strong>Сетка подписок:</strong> интерактивные тарифные карты, реализованные через Flex-контейнеры.</li>
        <li><strong>Стейт-менеджмент:</strong> сохранение токена сессии и прогресса обучения пользователя в LocalStorage.</li>
      </ul>
    </div>
    <div class="showcase-image-box">
      <img src="docs/media/word/media/Регистрация_Страница.png" alt="Страница регистрации">
      <div class="showcase-caption">Экран авторизации и карточки тарифных планов</div>
    </div>
  </div>
</div>

<!-- Slide 16: Conclusion -->
<div class="slide">
  <div class="slide-header">
    <span class="header-project">FOUNDATION OF CODE</span>
    <span class="header-section">03 / ЗАКЛЮЧЕНИЕ</span>
  </div>
  <h2 class="slide-title">Итоги работы и перспективы</h2>
  <div class="grid-2">
    <div class="card border-sky">
      <h3 class="card-title text-sky">Результаты спринта</h3>
      <ul class="bullets">
        <li><strong>Рабочий прототип (MVP):</strong> успешная реализация веб-платформы с концепцией Single Page Application.</li>
        <li><strong>Данные на клиенте:</strong> отлажен механизм реактивного стейт-менеджмента через LocalStorage API.</li>
        <li><strong>Тестирование:</strong> проведено комплексное регрессионное и кроссбраузерное тестирование интерфейса.</li>
      </ul>
    </div>
    <div class="card border-emerald">
      <h3 class="card-title text-emerald">Бэклог развития</h3>
      <ul class="bullets">
        <li><strong>Интеграция Sandbox:</strong> подключение браузерного веб-компилятора для выполнения практических заданий.</li>
        <li><strong>Бэкенд-архитектура:</strong> создание серверной части платформы на Node.js / Express для развертывания REST API.</li>
        <li><strong>СУБД интеграция:</strong> подключение базы данных PostgreSQL для персистентного хранения данных на сервере.</li>
      </ul>
    </div>
  </div>
</div>

<!-- Slide 17: Outro -->
<div class="slide slide-outro">
  <div class="outro-container">
    <div class="outro-tag">FOUNDATION OF CODE</div>
    <h1 class="outro-main">СПАСИБО ЗА ВНИМАНИЕ!</h1>
    <p class="outro-sub">Мы готовы ответить на ваши вопросы и обсудить техническую реализацию</p>
    <div class="outro-logo-box">
      <img src="docs/media/word/media/ИВТиПТ_ЮФУ.png" alt="Логотип ЮФУ">
    </div>
  </div>
</div>

</body>
</html>
"""

def main():
    edge_paths = [
        r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
        r"C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
    ]
    edge_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            edge_exe = p
            break
            
    if not edge_exe:
        print("Error: Microsoft Edge executable not found at standard Windows paths.")
        sys.exit(1)
        
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(repo_root, "presentation_temp.html")
    pdf_path = os.path.join(repo_root, "Foundation_of_Code_Presentation.pdf")
    
    # Save HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(get_html_content())
        
    print(f"Temporary HTML saved: {html_path}")
    print(f"Generating PDF: {pdf_path}")
    
    # Run Edge headless print-to-pdf with device scale factor for high DPI
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--force-device-scale-factor=2",
        f"--print-to-pdf={pdf_path}",
        "--no-margins",
        html_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("PDF successfully generated.")
    except Exception as e:
        print(f"Error during Edge headless printing: {e}")
        # Clean up
        if os.path.exists(html_path):
            os.remove(html_path)
        sys.exit(1)
        
    # Clean up temp HTML
    if os.path.exists(html_path):
        os.remove(html_path)
        print("Temporary HTML cleaned up.")
        
if __name__ == '__main__':
    main()
