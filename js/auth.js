// ─── AUTH & USER STORAGE ─────────────────────────────────────────────────────
// Uses localStorage to persist user session and account data.

const AUTH_KEY  = 'foc_user';
const USERS_KEY = 'foc_users';

const Auth = {
  // Returns current logged-in user object or null
  current() {
    try { return JSON.parse(localStorage.getItem(AUTH_KEY)); }
    catch { return null; }
  },

  // Returns all registered users
  allUsers() {
    try { return JSON.parse(localStorage.getItem(USERS_KEY)) || []; }
    catch { return []; }
  },

  // Register a new user
  register(firstName, lastName, email, password) {
    if (!firstName || !lastName || !email || !password)
      return { ok: false, error: 'Заполните все поля.' };

    // Имя и Фамилия: только русские/латинские буквы и дефисы, от 2 символов
    const nameRegex = /^[a-zA-Zа-яА-ЯёЁ\-]{2,}$/;
    if (!nameRegex.test(firstName.trim()))
      return { ok: false, error: 'Имя должно содержать только буквы (минимум 2).' };
    if (!nameRegex.test(lastName.trim()))
      return { ok: false, error: 'Фамилия должна содержать только буквы (минимум 2).' };

    // Email: стандартная проверка формата
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.trim()))
      return { ok: false, error: 'Введите корректный email адрес.' };

    // Пароль: минимум 8 символов, хотя бы одна цифра, одна заглавная и одна строчная буква
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!passwordRegex.test(password)) {
      return { ok: false, error: 'Пароль должен содержать минимум 8 символов, включая цифры, строчные и заглавные буквы.' };
    }

    const users = Auth.allUsers();
    if (users.find(u => u.email.toLowerCase() === email.toLowerCase()))
      return { ok: false, error: 'Аккаунт с таким email уже существует.' };

    const user = {
      id: Date.now().toString(),
      firstName: firstName.trim(),
      lastName: lastName.trim(),
      email: email.trim().toLowerCase(),
      password,                     // plaintext – MVP only, not for production
      joinedAt: new Date().toISOString(),
      progress: {},                 // conceptId -> 0..100
      savedRoadmaps: [],
      activityDays: [true, true, false, true, true, false, true],
    };

    users.push(user);
    localStorage.setItem(USERS_KEY, JSON.stringify(users));
    Auth._setSession(user);
    return { ok: true, user };
  },

  // Login an existing user
  login(email, password) {
    const users = Auth.allUsers();
    const user = users.find(
      u => u.email === email.trim().toLowerCase() && u.password === password
    );
    if (!user) return { ok: false, error: 'Неверный email или пароль.' };
    Auth._setSession(user);
    return { ok: true, user };
  },

  // Logout
  logout() {
    localStorage.removeItem(AUTH_KEY);
  },

  // Save session
  _setSession(user) {
    localStorage.setItem(AUTH_KEY, JSON.stringify(user));
  },

  // Update user data (progress, roadmaps, etc.)
  save(updatedUser) {
    localStorage.setItem(AUTH_KEY, JSON.stringify(updatedUser));
    const users = Auth.allUsers().map(u => u.id === updatedUser.id ? updatedUser : u);
    localStorage.setItem(USERS_KEY, JSON.stringify(users));
  },

  // Formatted display name: "Вячеслав Ф."
  displayName(user) {
    if (!user) return '';
    const last = user.lastName ? user.lastName.charAt(0).toUpperCase() + '.' : '';
    return `${user.firstName} ${last}`.trim();
  },

  // Avatar letter (first letter of first name)
  avatarLetter(user) {
    if (!user) return '?';
    return user.firstName.charAt(0).toUpperCase();
  },

  // Days since joined
  daysAgo(user) {
    if (!user) return 0;
    const ms = Date.now() - new Date(user.joinedAt).getTime();
    return Math.max(1, Math.floor(ms / 86400000));
  },

  // Human-readable join label
  joinLabel(user) {
    const d = Auth.daysAgo(user);
    if (d === 1) return 'Начал сегодня';
    if (d < 7)   return `Начал ${d} дня назад`;
    if (d < 14)  return 'Начал неделю назад';
    if (d < 30)  return `Начал ${Math.floor(d/7)} недели назад`;
    return `Начал ${Math.floor(d/30)} месяца назад`;
  },

  // Require auth – redirect to register if not logged in
  requireAuth(redirectTo) {
    if (!Auth.current()) {
      window.location.href = redirectTo || 'register.html';
      return false;
    }
    return true;
  }
};
