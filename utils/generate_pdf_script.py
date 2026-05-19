import os
import subprocess
import sys

def get_script_html():
    return """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Сценарий защиты проекта Foundation of Code</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

@page {
    size: A4 portrait;
    margin: 20mm 15mm;
}
* {
    box-sizing: border-box;
}
body {
    margin: 0;
    padding: 0;
    font-family: 'Inter', sans-serif;
    color: #0f172a;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 13.5px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* Header & Footer */
.doc-header {
    border-bottom: 2px solid #0284c7;
    padding-bottom: 10px;
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}
.doc-title-main {
    font-size: 18px;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
    letter-spacing: -0.5px;
}
.doc-subtitle {
    font-size: 11px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Intro Section */
.intro-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 15px 20px;
    margin-bottom: 25px;
}
.intro-title {
    font-size: 14px;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 10px;
    color: #0284c7;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.team-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}
.member {
    font-size: 11px;
    line-height: 1.4;
}
.member-name {
    font-weight: 700;
    color: #0f172a;
}
.member-role {
    color: #64748b;
}

/* Slide Script Item */
.slide-item {
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 20px;
    page-break-inside: avoid;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
}
.slide-header-box {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 8px;
    margin-bottom: 12px;
}
.slide-num-title {
    display: flex;
    align-items: center;
    gap: 10px;
}
.slide-number {
    background-color: #0f172a;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 8px;
    border-radius: 6px;
}
.slide-name {
    font-size: 14px;
    font-weight: 700;
    color: #0f172a;
}
.speaker-badge {
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.speaker-egor { background-color: #e0f2fe; color: #0369a1; }
.speaker-slava { background-color: #e0e7ff; color: #4338ca; }
.speaker-sasha { background-color: #d1fae5; color: #047857; }
.speaker-gosha { background-color: #f3e8ff; color: #6b21a8; }
.speaker-none { background-color: #f1f5f9; color: #475569; }

/* Actions & Speech */
.action-box {
    background-color: #fffbeb;
    border-left: 3px solid #d97706;
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    font-size: 12px;
    font-weight: 600;
    color: #b45309;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.action-box strong {
    text-transform: uppercase;
    font-size: 10px;
    background: #d97706;
    color: #ffffff;
    padding: 1px 5px;
    border-radius: 4px;
}
.speech-title {
    font-size: 11px;
    color: #64748b;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 4px;
    letter-spacing: 0.5px;
}
.speech-content {
    font-size: 13px;
    color: #1e293b;
    margin: 0;
    text-align: justify;
    line-height: 1.55;
}
</style>
</head>
<body>

<div class="doc-header">
  <div>
    <h1 class="doc-title-main">FOUNDATION OF CODE</h1>
    <div class="doc-subtitle">Технический сценарий защиты проекта / SPA Web-Platform</div>
  </div>
  <div style="text-align: right;">
    <div class="doc-subtitle">Группа 25ВТ–09.03.03.01–о1</div>
    <div style="font-size: 11px; color: #64748b; font-weight: 500; margin-top: 2px;">ЮФУ • ИВТиПТ • 2026</div>
  </div>
</div>

<div class="intro-card">
  <div class="intro-title">Действующие лица и распределение ролей:</div>
  <div class="team-grid">
    <div class="member">
      <div class="member-name" style="color: #0369a1;">Егор Бобровских</div>
      <div class="member-role">Тимлид, Product Owner, UX/UI</div>
      <div style="font-size: 9.5px; color: #64748b; margin-top: 4px;">Координатор доклада, Agile-планирование, дизайн-система, заключение.</div>
    </div>
    <div class="member">
      <div class="member-name" style="color: #4338ca;">Вячеслав Федоренко</div>
      <div class="member-role">Fullstack Developer</div>
      <div style="font-size: 9.5px; color: #64748b; margin-top: 4px;">Докладывает техническую реализацию: HTML, CSS, JS, LocalStorage, SPA-архитектуру.</div>
    </div>
    <div class="member">
      <div class="member-name" style="color: #047857;">Александр Владимиров</div>
      <div class="member-role">Content Product Manager</div>
      <div style="font-size: 9.5px; color: #64748b; margin-top: 4px;">Обоснование актуальности, бенчмаркинг рынка, анализ ЦА и Content Engineering.</div>
    </div>
    <div class="member">
      <div class="member-name" style="color: #6b21a8;">Георгий Литвиненко</div>
      <div class="member-role">QA & Release Engineer</div>
      <div style="font-size: 9.5px; color: #64748b; margin-top: 4px;">Quality Assurance, валидация стейта, регрессионное тестирование и бэклог развития.</div>
    </div>
  </div>
</div>

<!-- Слайд 1 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 01</span>
      <span class="slide-name">Титульный слайд</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Запустить презентацию на полный экран, проверить работоспособность кликера. Приветственно улыбнуться преподавателю.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Здравствуйте, я рад приветствовать вас! Мы представляем проект масштабируемой интерактивной SPA-платформы "Foundation of Code". Продукт разработан для декомпозиции фундаментальных концепций Computer Science и кросс-языкового анализа. Позвольте представить нашу проектную команду: Александр Владимиров — Content Product Manager, Вячеслав Федоренко — Fullstack Developer, Георгий Литвиненко — QA и Release Engineer, и я, Егор Бобровских — тимлид и UX/UI-архитектор. Переходим к защите концепции.»
  </p>
</div>

<!-- Слайд 2 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 02</span>
      <span class="slide-name">Проблема и актуальность</span>
    </div>
    <span class="speaker-badge speaker-sasha">Александр</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Нажать кнопку перехода на кликере. Установить визуальный контакт с преподавателем.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Начальный этап вхождения в разработку сопряжен со значительным синтаксическим диссонансом. Пользователи изучают синтаксические конструкции высокоуровневых абстракций без глубокого понимания физической архитектуры памяти, компиляции и жизненного цикла Runtime. Дополнительным негативным фактором является информационный хаос — отсутствие единой точки входа и четкого User Flow. Наш продукт фасилитирует процесс онбординга в Computer Science с помощью сквозного сопоставления концепций.»
  </p>
</div>

<!-- Слайд 3 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 03</span>
      <span class="slide-name">Наше решение: Foundation of Code</span>
    </div>
    <span class="speaker-badge speaker-sasha">Александр</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Нашим решением является интерактивный SPA-хаб. Мы спроектировали централизованную базу с модульной архитектурой образовательного контента. Обучение базируется на принципе декомпозиции абстракций: от низкоуровневой работы с железом и аллокации памяти (стек, куча) к высокоуровневому коду. Платформа предлагает интерактивный стейт-трекинг — геймифицированные дорожные карты с сохранением прогресса на клиенте через LocalStorage API.»
  </p>
</div>

<!-- Слайд 4 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 04</span>
      <span class="slide-name">Цели и задачи проекта</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд. Сказать уверенным тоном, выделяя интонацией ключевую цель MVP.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Главная цель нашего MVP — проектирование и разработка адаптивного одностраничного веб-приложения с интерактивным кросс-языковым модулем. Для достижения этой цели мы решили четыре ключевые задачи: провели глубокий бенчмаркинг и конкурентный анализ существующих платформ, спроектировали User Flow и дизайн-систему с полноценным UI Kit в Figma, реализовали семантическую верстку и клиентский роутинг, а также внедрили персистентность данных через LocalStorage API с последующим QA-тестированием.»
  </p>
</div>

<!-- Слайд 5 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 05</span>
      <span class="slide-name">Разработчики и распределение обязанностей</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Указать жестом руки на команду, упоминая роли каждого участника.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Команда работала по гибкой методологии с четким распределением зон ответственности. Я, как Product Owner, отвечал за Scrum-планирование, проектирование дизайн-системы и варфреймов в Figma, а также проведение Design Review на соответствие Pixel Perfect. Вячеслав отвечал за SPA-архитектуру, клиентский роутинг, кроссбраузерную Flexbox/Grid разметку и асинхронное манипулирование DOM. Александр взял на себя Information Architecture, бенчмаркинг рынка и Content Engineering. Георгий курировал Quality Assurance, регрессионное тестирование и валидацию персистентного стейта.»
  </p>
</div>

<!-- Слайд 6 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 06</span>
      <span class="slide-name">Раздел 2: Реализация проекта (Разделитель)</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд. Передать слово Вячеславу.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Переходим ко второму разделу нашего доклада — технической реализации продукта, описанию архитектурных решений, технологического стека и демонстрации ключевых интерфейсов. Передаю слово нашему Fullstack-разработчику Вячеславу.»
  </p>
</div>

<!-- Слайд 7 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 07</span>
      <span class="slide-name">Анализ предметной области и целевой аудитории</span>
    </div>
    <span class="speaker-badge speaker-sasha">Александр</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Сделать полшага вперед. Обратиться к слайду.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «В рамках предпроектного анализа мы провели сегментацию целевой аудитории. Мы выделили три ключевых кластера пользователей: Junior-разработчики, требующие систематизации знаний, студенты профильных IT-специальностей и свитчеры, проходящие интенсивную переквалификацию. Главные боли аудитории — фрагментированность восприятия Computer Science, парадигмальный барьер при переходе между ООП и функциональным стилем, а также низкая интерактивность классических текстовых учебников.»
  </p>
</div>

<!-- Слайд 8 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 08</span>
      <span class="slide-name">Визуальная концепция и дизайн-система</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Сделать жест в сторону слайда, подчеркивая архитектуру интерфейса.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «При проектировании UI/UX мы внедрили темную схему Dark Mode для снижения зрительного утомления и адаптации под стандарты IDE. Мы применили модульную сетку Component-Based Layout для повышения скандируемости материалов и разработали уникальное HSL-цветовое кодирование для каждого языкового стека. Проектирование User Flow в Figma позволило экспортировать дизайн-токены напрямую в CSS Custom Properties.»
  </p>
</div>

<!-- Слайд 9 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 09</span>
      <span class="slide-name">Бенчмаркинг и конкурентные преимущества</span>
    </div>
    <span class="speaker-badge speaker-sasha">Александр</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «В ходе бенчмаркинга мы проанализировали MDN, W3Schools и Stepik. Наше ключевое конкурентное преимущество — реактивный синтаксический модуль. Платформа не просто выводит текст, она сопоставляет выполнение одной и той же концепции на C, Python и JS в единой плоскости экрана. Также мы визуализируем Memory Representation — схемы выделения ресурсов под капотом выполнения кода.»
  </p>
</div>

<!-- Слайд 10 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 10</span>
      <span class="slide-name">Технологический стек проекта</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Сделать шаг вперед. Говорить четко, делая акцент на технических деталях.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Наш технологический стек ориентирован на высокую производительность без лишнего сетевого оверхеда. Мы использовали HTML5 для создания семантического DOM-дерева, CSS3 с Custom Properties и Grid Layout для построения адаптивного интерфейса, чистый JavaScript для реализации логики маршрутизации SPA без тяжелых фреймворков, и LocalStorage API для персистентного хранения сессий и прогресса обучения непосредственно в браузере пользователя.»
  </p>
</div>

<!-- Слайд 11 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 11</span>
      <span class="slide-name">Реализация структуры: HTML5</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Повернуть голову к экрану, указав рукой на скриншот исходного кода index.html справа.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «На слайде представлен фрагмент кода index.html. Мы реализовали чистую семантическую разметку. SPA-архитектура построена на динамическом рендеринге представлений (views) внутри единого центрального контейнера. Весь контент подгружается асинхронно через JS, что минимизирует задержки и полностью исключает перезагрузку страниц, повышая показатель Performance.»
  </p>
</div>

<!-- Слайд 12 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 12</span>
      <span class="slide-name">Таблицы стилей: CSS3</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд. Указать на фрагмент стилей справа, где объявлены дизайн-токены.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Стилистическое оформление вынесено в изолированную таблицу стилей. Мы внедрили CSS Custom Properties для управления глобальными дизайн-токенами и темизацией. Адаптивность реализована через гибридное использование Flexbox и CSS Grid. Все микровзаимодействия — ховеры, переходы, свечения карточек — снабжены плавными эффектами перехода для улучшения UX.»
  </p>
</div>

<!-- Слайд 13 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 13</span>
      <span class="slide-name">Главная страница платформы</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Продемонстрировать скриншот главной страницы на экране.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Интерфейс главной страницы встречает пользователя минималистичным баннером в стиле Slate-Dark. Для повышения юзабилити спроектирована Sidebar-навигация, обеспечивающая мгновенный переход по модулям SPA. Для мобильных вьюпортов сайдбар автоматически сворачивается в адаптивное бургер-меню, соответствуя паттернам отзывчивого дизайна.»
  </p>
</div>

<!-- Слайд 14 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 14</span>
      <span class="slide-name">Раздел сравнения концепций</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Акцентировать внимание на вкладках переключения C / Python / JS на изображении справа.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Наш центральный модуль — реактивный синтаксический экран. При клике на вкладку C, Python или JavaScript логика JS мгновенно перерисовывает правый вьюпорт, подставляя соответствующий синтаксис без отправки HTTP-запросов на сервер. Это обеспечивает мгновенный визуальный отклик и позволяет изучать темы Computer Science в реальном времени.»
  </p>
</div>

<!-- Слайд 15 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 15</span>
      <span class="slide-name">Регистрация и тарифные планы</span>
    </div>
    <span class="speaker-badge speaker-slava">Вячеслав</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Показать на скриншот формы авторизации. Передать слово Георгию.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «Мы внедрили клиентскую валидацию форм авторизации с помощью регулярных выражений. Тарифная сетка реализована в виде интерактивных Flex-карточек. Стейт-менеджмент сессии и прогресс обучения пользователя сохраняются в LocalStorage, эмулируя полноценное клиент-серверное взаимодействие на стороне браузера. Я передаю слово нашему инженеру по качеству Георгию.»
  </p>
</div>

<!-- Слайд 16 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 16</span>
      <span class="slide-name">Итоги работы и перспективы</span>
    </div>
    <span class="speaker-badge speaker-gosha">Георгий</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Сделать шаг вперед, говорить громко и уверенно. Переключить слайд.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «В результате проведенных спринтов мы получили полностью функционирующий MVP интерактивной SPA-платформы. Проведено ручное функциональное и регрессионное тестирование вьюпортов и LocalStorage. В нашем бэклоге развития: интеграция браузерной песочницы Sandbox для компиляции кода, развертывание REST API бэкенда на Node.js и Express, а также подключение СУБД PostgreSQL для серверной персистентности. Передаю слово Егору для завершения доклада.»
  </p>
</div>

<!-- Слайд 17 -->
<div class="slide-item">
  <div class="slide-header-box">
    <div class="slide-num-title">
      <span class="slide-number">СЛАЙД 17</span>
      <span class="slide-name">Спасибо за внимание!</span>
    </div>
    <span class="speaker-badge speaker-egor">Егор</span>
  </div>
  <div class="action-box">
    <strong>Инструкция</strong> Переключить слайд на финальный. Вежливо улыбнуться преподавателю. Приготовиться координировать ответы команды на вопросы.
  </div>
  <div class="speech-title">Речь спикера:</div>
  <p class="speech-content">
    «В заключение хочу поблагодарить Южный федеральный университет за поддержку. Наш проект Foundation of Code доказывает, что системное понимание фундаментальных принципов Computer Science можно сделать доступным и интерактивным. Спасибо за внимание! Мы готовы ответить на ваши вопросы и обсудить технические аспекты реализации.»
  </p>
</div>

<!-- Page break for Glossary -->
<div style="page-break-before: always; margin-top: 30px;">
  <div class="doc-header">
    <div>
      <h1 class="doc-title-main">FOUNDATION OF CODE</h1>
      <div class="doc-subtitle">Технический глоссарий проекта (Шпаргалка для команды)</div>
    </div>
    <div style="text-align: right;">
      <div class="doc-subtitle">Глоссарий терминов</div>
      <div style="font-size: 11px; color: #64748b; font-weight: 500; margin-top: 2px;">ЮФУ • ИВТиПТ • 2026</div>
    </div>
  </div>
  
  <div class="intro-card" style="margin-bottom: 20px;">
    <strong>Зачем это нужно:</strong> Если преподаватель спросит значение какого-то слова из выступления, используйте эту таблицу для быстрого и уверенного ответа.
  </div>

  <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 12px;">
    <thead>
      <tr style="background-color: #0284c7; color: #ffffff; text-align: left;">
        <th style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; width: 30%;">Термин / Баззворд</th>
        <th style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; width: 70%;">Что это означает простыми словами и как связано с нашим проектом</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">SPA (Single Page Application)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Одностраничное приложение. Сайт загружается один раз, а разделы переключаются мгновенно без перезагрузки всей страницы. У нас это реализовано на чистом JavaScript.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">MVP (Minimum Viable Product)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Минимально жизнеспособный продукт. Первая рабочая версия сайта с базовыми функциями, готовая к показу пользователям (в нашем случае — прототип энциклопедии).</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">User Flow</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Путь пользователя. Логический маршрут переходов человека по сайту: от входа на главную до изучения концепций или авторизации.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">UI Kit и Дизайн-система</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Набор готовых графических элементов (кнопки, карточки, шрифты, цвета), созданный в Figma для обеспечения единого визуального стиля при верстке.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Pixel Perfect</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Верстка «пиксель-в-пиксель». Максимально точный перенос дизайнерского макета из Figma в рабочий HTML/CSS код.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">DOM (Document Object Model)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Объектная модель документа. Структура элементов страницы (тегов HTML), которой мы динамически управляем (перерисовываем разделы) с помощью JavaScript.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Runtime (Среда выполнения)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Среда, в которой выполняется программа во время работы. Влияет на скорость выполнения кода и управление ресурсами компьютера.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">LocalStorage API</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Локальное хранилище в браузере пользователя. Позволяет сайту сохранять информацию (например, прогресс обучения или статус входа) даже после закрытия вкладки.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Data Persistence (Персистентность)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Сохраняемость данных. Свойство информации оставаться доступной между сеансами работы (у нас это обеспечивается записью в LocalStorage).</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Computer Science</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Компьютерные науки. Теоретические основы вычислений, архитектуры систем, алгоритмов и управления памятью.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Декомпозиция</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Разделение большой сложной темы (или задачи) на мелкие и понятные части. На этом принципе построена наша энциклопедия.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Аллокация памяти</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Процесс выделения оперативной памяти компьютера под переменные и объекты во время выполнения программы.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Стек и Куча (Stack & Heap)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Две основные области оперативной памяти: Стек — быстрый, для простых переменных; Куча — большая и динамическая, для сложных объектов. Разницу между ними мы объясняем на платформе.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Бенчмаркинг</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Сравнительный анализ. Процесс изучения конкурентов и их лучших практик для внедрения в свой собственный продукт.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">QA (Quality Assurance)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Обеспечение качества. Процесс тестирования сайта на ошибки, кроссбраузерность и адаптивность под различные экраны.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Регрессионное тестирование</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Повторная проверка сайта после внесения изменений, чтобы убедиться, что старый функционал работает без сбоев.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">REST API</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Архитектурный стиль взаимодействия клиента и сервера через HTTP-запросы. Запланирован в бэклоге развития нашего бэкенда.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Sandbox (Песочница)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Безопасная изолированная среда, в которой пользователь может писать и запускать код прямо в браузере.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Регулярные выражения (RegExp)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Шаблоны поиска и проверки текста. У нас используются для валидации корректности ввода email-адреса.</td>
      </tr>
      <tr style="background-color: #f8fafc;">
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f1f5f9;">Линтер (Линтинг)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Инструмент автоматической проверки исходного кода на соответствие стандартам форматирования и наличие потенциальных багов.</td>
      </tr>
      <tr>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1; font-weight: 700; background-color: #f8fafc;">Вьюпорт (Viewport)</td>
        <td style="padding: 8px 10px; border: 1px solid #cbd5e1;">Область экрана устройства, на которой отображается сайт. Наша верстка адаптируется под размер любого вьюпорта.</td>
      </tr>
    </tbody>
  </table>
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
    html_path = os.path.join(repo_root, "script_temp.html")
    pdf_path = os.path.join(repo_root, "Foundation_of_Code_Presentation_Script.pdf")
    
    # Save HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(get_script_html())
        
    print(f"Temporary HTML saved: {html_path}")
    print(f"Generating PDF Script: {pdf_path}")
    
    # Run Edge headless print-to-pdf
    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--force-device-scale-factor=2",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("PDF Script successfully generated.")
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
