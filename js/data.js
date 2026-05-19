const CONCEPTS = [
  {
    id: "memory", title: "Управление памятью", icon: "⚡", tag: "Основы", difficulty: 2,
    desc: "Stack, Heap, указатели и сборщик мусора. Как разные языки управляют памятью.",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Ручное управление памятью
int *ptr = malloc(sizeof(int));
*ptr = 42;
printf("%d\\n", *ptr);
free(ptr); // ОБЯЗАТЕЛЬНО освободить`,
      Python: `# Автоматический GC
nums = [1, 2, 3, 4, 5]
# Python сам управляет памятью
# Cyclic GC для циклических ссылок
import gc
gc.collect()`,
      JavaScript: `// V8 движок + Mark-and-Sweep
let obj = { data: new Array(1000) };
// Ссылка удалена → GC освободит
obj = null;
// WeakRef для слабых ссылок
const weak = new WeakRef(target);`
    }
  },
  {
    id: "types", title: "Типы данных", icon: "🔢", tag: "Основы", difficulty: 1,
    desc: "Статическая и динамическая типизация, примитивы, составные типы, boxing/unboxing.",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Статическая строгая типизация
int age = 25;          // 4 байта
float pi = 3.14f;      // 4 байта
double precise = 3.14159; // 8 байт
char letter = 'A';     // 1 байт`,
      Python: `# Динамическая типизация
age = 25           # int
name = "Alice"     # str
pi = 3.14          # float
items = [1, 2, 3]  # list
# type hints (опционально)
def greet(name: str) -> str: ...`,
      JavaScript: `// Слабая динамическая типизация
let age = 25;         // number
let name = "Alice";   // string
let active = true;    // boolean
// Coercion: "42" + 1 === "421"
// TypeScript исправляет это`
    }
  },
  {
    id: "loops", title: "Циклы и итерация", icon: "🔄", tag: "Управление", difficulty: 1,
    desc: "for, while, do-while, итераторы, генераторы. Разные парадигмы обхода данных.",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Классический for-цикл
for (int i = 0; i < 10; i++) {
    printf("%d\\n", i);
}
// while
while (condition) { /* ... */ }`,
      Python: `# Питоновский for-each
for item in collection:
    print(item)
# range() для числовых
for i in range(10):
    print(i)
# list comprehension
squares = [x**2 for x in range(10)]`,
      JavaScript: `// Несколько стилей
for (let i = 0; i < 10; i++) {}
for (const item of array) {}
for (const key in object) {}
// Функциональный стиль
[1,2,3].forEach(x => console.log(x))
[1,2,3].map(x => x * 2)`
    }
  },
  {
    id: "functions", title: "Функции и замыкания", icon: "λ", tag: "Абстракция", difficulty: 2,
    desc: "Первоклассные функции, замыкания, рекурсия, higher-order functions.",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Функции как указатели
int add(int a, int b) { return a + b; }
// Указатель на функцию
int (*op)(int, int) = add;
printf("%d\\n", op(3, 4));
// Нет замыканий в C!`,
      Python: `# Первоклассные функции
def make_adder(n):
    def adder(x):  # замыкание
        return x + n
    return adder

add5 = make_adder(5)
print(add5(3))  # 8
# lambda
square = lambda x: x**2`,
      JavaScript: `// Замыкания + стрелочные функции
const makeCounter = () => {
  let count = 0;
  return {
    inc: () => ++count,
    get: () => count
  };
};
const counter = makeCounter();
counter.inc(); counter.inc();
console.log(counter.get()); // 2`
    }
  },
  {
    id: "structs", title: "Структуры данных", icon: "🏗", tag: "Структуры", difficulty: 3,
    desc: "Массивы, связные списки, хэш-таблицы, деревья. Сложность операций O(n).",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Массив – непрерывная память
int arr[5] = {1, 2, 3, 4, 5};
// Структура
typedef struct {
    char name[50];
    int age;
} Person;
Person p = {"Alice", 25};`,
      Python: `# Встроенные структуры
lst = [1, 2, 3]       # list O(1) append
dct = {"key": "val"}  # dict O(1) lookup
st  = {1, 2, 3}       # set O(1) contains
tpl = (1, 2, 3)       # tuple immutable
from collections import deque, Counter`,
      JavaScript: `// Массивы и объекты
const arr = [1, 2, 3]; // динамический
const map = new Map(); // O(1) lookup
const set = new Set(); // уникальные
// Объект как словарь
const dict = { key: "value" };
// WeakMap для приватных данных`
    }
  },
  {
    id: "errors", title: "Обработка ошибок", icon: "🛡", tag: "Надёжность", difficulty: 2,
    desc: "Исключения, коды ошибок, Result-типы. Разные подходы к обработке сбоев.",
    langs: ["C", "Python", "JavaScript"],
    code: {
      C: `// Коды возврата + errno
FILE *f = fopen("file.txt", "r");
if (f == NULL) {
    perror("Ошибка открытия");
    return -1; // код ошибки
}`,
      Python: `# Исключения (EAFP стиль)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")
finally:
    print("Всегда выполнится")`,
      JavaScript: `// try/catch + Promise
try {
  JSON.parse("invalid");
} catch (e) {
  console.error(e.message);
}
// Async/await
const data = await fetch(url)
  .catch(err => console.error(err));`
    }
  }
];

const ROADMAPS = [
  {
    id: "zero-to-junior", title: "От нуля до Junior", icon: "🚀", color: "#6366f1", level: "Начинающий", duration: "6–9 мес",
    steps: [
      { title: "Основы CS", desc: "Алгоритмы, структуры данных, сложность" },
      { title: "Первый язык", desc: "Python или JavaScript – выбери один" },
      { title: "Базовые концепции", desc: "ООП, функции, модули, стандартная библиотека" },
      { title: "Инструменты", desc: "Git, терминал, редактор, отладчик" },
      { title: "Мини-проект", desc: "TODO-app, калькулятор, парсер" },
      { title: "Первое резюме", desc: "GitHub, LinkedIn, портфолио" }
    ]
  },
  {
    id: "low-level", title: "Низкоуровневые концепции", icon: "⚙️", color: "#f59e0b", level: "Средний", duration: "3–5 мес",
    steps: [
      { title: "Память", desc: "Stack vs Heap, указатели, выравнивание" },
      { title: "Язык C", desc: "Синтаксис, указатели, malloc/free" },
      { title: "Компилятор", desc: "Preprocessor, compilation, linking" },
      { title: "ОС и процессы", desc: "Системные вызовы, потоки, IPC" },
      { title: "Оптимизация", desc: "Cache, SIMD, профилирование" }
    ]
  },
  {
    id: "python-to-c", title: "Переход Python → C", icon: "🔀", color: "#10b981", level: "Средний", duration: "2–3 мес",
    steps: [
      { title: "Что изменится", desc: "Ручная память, статическая типизация" },
      { title: "Синтаксис C", desc: "printf, scanf, структуры, union" },
      { title: "Указатели", desc: "Адреса, разыменование, арифметика указателей" },
      { title: "Сборка проекта", desc: "Makefile, gcc/clang, заголовочные файлы" },
      { title: "Отладка", desc: "GDB, Valgrind, AddressSanitizer" }
    ]
  },
  {
    id: "web-dev", title: "Web-разработка", icon: "🌐", color: "#8b5cf6", level: "Начинающий", duration: "4–6 мес",
    steps: [
      { title: "HTML & CSS", desc: "Семантика, Flexbox, Grid, адаптивность" },
      { title: "JavaScript", desc: "DOM, события, fetch, async/await" },
      { title: "React", desc: "Компоненты, хуки, state management" },
      { title: "Backend", desc: "Node.js, Express, REST API" },
      { title: "База данных", desc: "SQL basics, PostgreSQL, ORM" },
      { title: "Деплой", desc: "Vercel, Railway, Docker basics" }
    ]
  }
];

const LANGUAGES = [
  {
    id: "python", name: "Python", logo: "🐍", color: "#3b82f6",
    paradigm: ["ООП", "Функциональный", "Процедурный"], difficulty: 1,
    domains: ["Data Science", "Backend", "ML/AI", "Автоматизация"],
    desc: "Читаемый язык с огромной экосистемой. Идеален для старта и data science.",
    pros: ["Простой синтаксис", "Огромная библиотека", "ML/AI экосистема"],
    cons: ["Медленнее компилируемых", "GIL в многопоточности"],
    popularity: 92
  },
  {
    id: "c", name: "C", logo: "©", color: "#f59e0b",
    paradigm: ["Процедурный", "Структурный"], difficulty: 4,
    domains: ["Системное ПО", "Встраиваемые системы", "ОС"],
    desc: "Язык-фундамент. Понимание C – понимание того, как работает компьютер.",
    pros: ["Максимальная производительность", "Контроль памяти", "Везде работает"],
    cons: ["Ручная память", "Нет ООП", "Сложная отладка"],
    popularity: 78
  },
  {
    id: "javascript", name: "JavaScript", logo: "JS", color: "#eab308",
    paradigm: ["ООП", "Функциональный", "Прототипный"], difficulty: 2,
    domains: ["Frontend", "Backend (Node)", "Мобильные"],
    desc: "Язык веба. Единственный язык, работающий в браузере нативно.",
    pros: ["Везде работает", "Огромное комьюнити", "Full-stack"],
    cons: ["Неявное приведение типов", "Event loop нюансы"],
    popularity: 95
  },
  {
    id: "csharp", name: "C#", logo: "C#", color: "#8b5cf6",
    paradigm: ["ООП", "Функциональный"], difficulty: 3,
    domains: ["Game Dev (Unity)", "Enterprise", "Desktop"],
    desc: "Мощный язык от Microsoft. Лучший выбор для Unity и корпоративной разработки.",
    pros: ["Строгая типизация", "Unity", "LINQ"],
    cons: ["В основном Windows/Microsoft", "Медленнее C++"],
    popularity: 71
  }
];

const ARTICLES = [
  {
    id: 1,
    title: "Почему каждый разработчик должен знать C",
    tag: "Теория", readTime: "8 мин", date: "15 дек 2026", author: "Егор Б.",
    excerpt: "C – не просто старый язык. Это линза, через которую видно, как на самом деле работает компьютер. Разбираем почему.",
    content: `
      <h2>Зачем учить C в 2026 году?</h2>
      <p>Многие новички задаются вопросом: зачем изучать язык, созданный в 1972 году, когда есть Python, JavaScript и Go? Ответ прост – C это не просто язык, это рентгеновский снимок компьютера.</p>
      <p>Когда вы пишете на Python <code>nums = [1, 2, 3]</code>, за этой строкой скрыты десятки операций: выделение памяти в куче, инициализация заголовка объекта, установка счётчика ссылок, запись указателей на элементы. В C вам придётся написать всё это явно – и именно это делает вас лучшим программистом.</p>

      <h2>Три причины учить C</h2>
      <h3>1. Вы поймёте память</h3>
      <p>В C нет сборщика мусора. Вы сами выделяете память через <code>malloc()</code> и освобождаете через <code>free()</code>. Это звучит страшно, но именно этот опыт даёт интуицию о том, что происходит «под капотом» любого другого языка.</p>
      <pre><code>int *arr = malloc(5 * sizeof(int));
if (arr == NULL) { /* обработка ошибки */ }
// ... используем arr ...
free(arr); // обязательно!</code></pre>

      <h3>2. Вы поймёте производительность</h3>
      <p>Почему NumPy быстрее чистого Python? Потому что внутри NumPy – C. Почему SQLite такой быстрый? C. Почему ядро Linux работает на любом железе? C. Понимание C объясняет производительность всей экосистемы.</p>

      <h3>3. Вы поймёте абстракции</h3>
      <p>Классы в Python, объекты в JavaScript, структуры в Go – всё это абстракции над тем, что C делает явно. Когда видишь механизм без корпуса, гораздо легче понять, как работает машина с корпусом.</p>

      <h2>С чего начать?</h2>
      <p>Начните с книги «Язык программирования C» Кернигана и Ричи. Затем – практика: напишите свой malloc, реализуйте связный список, напишите простой парсер. Это изменит ваше мышление навсегда.</p>
      <p>Смотрите роудмап <strong>«Низкоуровневые концепции»</strong> на нашей платформе – там всё по шагам.</p>
    `
  },
  {
    id: 2,
    title: "Stack vs Heap: визуальное объяснение",
    tag: "Концепции", readTime: "5 мин", date: "10 дек 2026", author: "Вячеслав Ф.",
    excerpt: "Большинство разработчиков знают слова «стек» и «куча». Но мало кто понимает, что происходит в памяти на самом деле.",
    content: `
      <h2>Две зоны памяти</h2>
      <p>Когда ваша программа запускается, операционная система выделяет ей несколько областей памяти. Две главные – это стек (stack) и куча (heap). Они принципиально разные по устройству и назначению.</p>

      <h2>Стек (Stack)</h2>
      <p>Стек – это область памяти, которая работает по принципу LIFO (Last In, First Out). Когда вы вызываете функцию, в стек добавляется «фрейм» с локальными переменными. Когда функция завершается – фрейм автоматически удаляется.</p>
      <pre><code>void foo() {
    int x = 10;  // на стеке
    int y = 20;  // на стеке
    // при выходе из foo – x и y исчезают
}</code></pre>
      <p><strong>Плюсы стека:</strong> молниеносное выделение (просто сдвиг указателя), автоматическое освобождение, отличная cache-локальность.</p>
      <p><strong>Минусы стека:</strong> ограниченный размер (обычно 1–8 МБ), нельзя использовать данные после выхода из функции.</p>

      <h2>Куча (Heap)</h2>
      <p>Куча – большая область памяти для динамического выделения. В отличие от стека, данные живут столько, сколько нужно программисту (или сборщику мусора).</p>
      <pre><code>// C: явное управление
int *arr = malloc(1000 * sizeof(int)); // выделяем на куче
// ... используем сколько угодно времени ...
free(arr); // освобождаем вручную

# Python: автоматически
my_list = list(range(1000))  # на куче, GC следит</code></pre>
      <p><strong>Плюсы кучи:</strong> практически неограниченный размер, данные живут за пределами функции, гибкость.</p>
      <p><strong>Минусы кучи:</strong> медленнее стека, фрагментация, в C – утечки памяти при забытом free().</p>

      <h2>Правило выбора</h2>
      <p>Если данные нужны только внутри функции и их размер известен заранее – стек. Если данные нужно вернуть, передать между функциями, или размер не известен – куча.</p>
    `
  },
  {
    id: 3,
    title: "Как Python управляет памятью за вас",
    tag: "Python", readTime: "6 мин", date: "5 дек 2026", author: "Александр В.",
    excerpt: "Reference counting, cyclic GC, arenas – разбираем механизм автоматического управления памятью в CPython.",
    content: `
      <h2>Три уровня управления памятью в Python</h2>
      <p>Python (точнее CPython – эталонная реализация) использует трёхуровневую систему управления памятью. Понимание этой системы помогает писать более эффективный код и избегать утечек памяти.</p>

      <h2>Уровень 1: Reference Counting</h2>
      <p>Каждый объект в Python хранит счётчик ссылок – сколько переменных или структур данных на него указывают. Как только счётчик падает до нуля, объект немедленно удаляется.</p>
      <pre><code>import sys
x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + аргумент getrefcount)
y = x
print(sys.getrefcount(x))  # 3
del y
print(sys.getrefcount(x))  # снова 2</code></pre>
      <p>Reference counting работает быстро и детерминировано – объект удаляется сразу, как только становится ненужным. Но у него есть фатальный недостаток: циклические ссылки.</p>

      <h2>Уровень 2: Cyclic Garbage Collector</h2>
      <p>Представьте два объекта, которые ссылаются друг на друга. Reference counting никогда не дойдёт до нуля, даже если больше никто на них не указывает. Для этого и существует cyclic GC.</p>
      <pre><code>import gc

class Node:
    def __init__(self):
        self.next = None

a = Node()
b = Node()
a.next = b
b.next = a  # цикл!
del a, b    # счётчики не нулевые

gc.collect()  # cyclic GC находит и чистит</code></pre>

      <h2>Уровень 3: Memory Arenas</h2>
      <p>Python не возвращает память ОС при каждом удалении объекта – это было бы слишком медленно. Вместо этого используется система арен (256 КБ), пулов (4 КБ) и блоков для маленьких объектов (до 512 байт).</p>
      <p>Это значит, что память, освобождённая внутри Python, остаётся в пуле и быстро переиспользуется для новых объектов. Только когда арена полностью пустеет – она возвращается ОС.</p>

      <h2>Практические выводы</h2>
      <p>Для обычного кода это всё работает автоматически. Но если вы работаете с большими данными, помните: <code>del</code> уменьшает счётчик ссылок, но не обязательно освобождает память сразу. Используйте <code>gc.collect()</code> при необходимости, и избегайте циклических ссылок в долгоживущих объектах.</p>
    `
  },
  {
    id: 4,
    title: "Замыкания: от теории к практике на трёх языках",
    tag: "Концепции", readTime: "10 мин", date: "1 дек 2026", author: "Егор Б.",
    excerpt: "Замыкание – одна из мощнейших концепций. Сравниваем реализацию в C (их нет!), Python и JavaScript.",
    content: `
      <h2>Что такое замыкание?</h2>
      <p>Замыкание – это функция, которая «помнит» переменные из окружающего контекста даже после того, как этот контекст перестал существовать. Это звучит абстрактно, поэтому сразу к примерам.</p>

      <h2>C: замыканий нет</h2>
      <p>В C функции – это просто адреса в памяти. У них нет доступа к контексту вызвавшей функции. Попытка эмулировать замыкания через глобальные переменные или структуры – это костыль, а не замыкание.</p>
      <pre><code>// Псевдозамыкание через struct + указатель на функцию
typedef struct {
    int captured_value;
    int (*call)(struct Closure*, int);
} Closure;

int adder_call(Closure *self, int x) {
    return self->captured_value + x;
}
// Это много кода для простой идеи...
// В C++ есть лямбды, но не в C</code></pre>

      <h2>Python: замыкания элегантны</h2>
      <p>В Python функция – это объект первого класса. Вложенная функция автоматически захватывает переменные из внешней области видимости.</p>
      <pre><code>def make_counter(start=0):
    count = start  # эта переменная «захватывается»

    def increment():
        nonlocal count  # говорим, что меняем внешнюю
        count += 1
        return count

    def reset():
        nonlocal count
        count = start

    return increment, reset

inc, rst = make_counter(10)
print(inc())  # 11
print(inc())  # 12
rst()
print(inc())  # 11 снова</code></pre>

      <h2>JavaScript: замыкания повсюду</h2>
      <p>JavaScript буквально построен на замыканиях. Паттерны модуля, приватные переменные, фабрики – всё это замыкания.</p>
      <pre><code>// Фабрика счётчиков
const makeCounter = (start = 0) => {
  let count = start; // приватная переменная!

  return {
    increment: () => ++count,
    decrement: () => --count,
    value:     () => count,
    reset:     () => { count = start; }
  };
};

const c1 = makeCounter(5);
const c2 = makeCounter(100); // независимый!

c1.increment(); // 6
c1.increment(); // 7
c2.increment(); // 101

// c1 и c2 имеют свои независимые count</code></pre>

      <h2>Когда использовать замыкания?</h2>
      <p>Замыкания идеальны для: фабричных функций, каллбэков с состоянием, мемоизации, эмуляции приватных переменных. Главное – не злоупотреблять: глубоко вложенные замыкания трудно читать и отлаживать.</p>
    `
  }
];

const TEAM = [
  {
    name: "Егор Бобровских",
    role: "Тимлид · Архитектор · UX",
    avatar: "Е",
    color: "#6366f1",
    desc: "Отвечает за техническую архитектуру, UX-прототипирование и code review. Координирует работу команды.",
    skills: ["Architecture", "UX/UI", "Code Review", "TypeScript"]
  },
  {
    name: "Вячеслав Федоренко",
    role: "Fullstack Developer · UI",
    avatar: "В",
    color: "#10b981",
    desc: "Разрабатывает визуальную часть и программную логику. Верстает компоненты, интегрирует бэкенд.",
    skills: ["React", "Node.js", "CSS", "API Design"]
  },
  {
    name: "Георгий Литвиненко",
    role: "QA Engineer",
    avatar: "Г",
    color: "#f59e0b",
    desc: "Тестирует функциональность, проверяет адаптивность и находит баги. Следит за качеством продукта.",
    skills: ["Testing", "Bug Reports", "Pixel Perfect", "UX Testing"]
  },
  {
    name: "Александр Владимиров",
    role: "Контент-менеджер · Аналитик",
    avatar: "А",
    color: "#8b5cf6",
    desc: "Пишет статьи, готовит примеры кода на трёх языках, анализирует рынок конкурентов.",
    skills: ["Technical Writing", "Python", "C", "Market Analysis"]
  }
];

const PRICING = [
  {
    name: "Бесплатно",
    price: "0 ₽",
    period: "навсегда",
    color: "#6366f1",
    highlight: false,
    desc: "Всё необходимое для старта",
    features: [
      { text: "Все базовые концепции", ok: true },
      { text: "Роудмапы обучения", ok: true },
      { text: "Статьи и гайды", ok: true },
      { text: "Сравнение языков", ok: true },
      { text: "Сохранение прогресса", ok: false },
      { text: "Личный кабинет", ok: false },
      { text: "Приоритетная поддержка", ok: false }
    ]
  },
  {
    name: "Pro",
    price: "299 ₽",
    period: "в месяц",
    color: "#6366f1",
    highlight: true,
    badge: "Популярный",
    desc: "Для серьёзного обучения",
    features: [
      { text: "Все базовые концепции", ok: true },
      { text: "Роудмапы обучения", ok: true },
      { text: "Статьи и гайды", ok: true },
      { text: "Сравнение языков", ok: true },
      { text: "Сохранение прогресса", ok: true },
      { text: "Личный кабинет", ok: true },
      { text: "Приоритетная поддержка", ok: false }
    ]
  },
  {
    name: "Team",
    price: "799 ₽",
    period: "в месяц",
    color: "#8b5cf6",
    highlight: false,
    desc: "Для групп и учебных заведений",
    features: [
      { text: "Все базовые концепции", ok: true },
      { text: "Роудмапы обучения", ok: true },
      { text: "Статьи и гайды", ok: true },
      { text: "Сравнение языков", ok: true },
      { text: "Сохранение прогресса", ok: true },
      { text: "Личный кабинет", ok: true },
      { text: "Приоритетная поддержка", ok: true }
    ]
  }
];
