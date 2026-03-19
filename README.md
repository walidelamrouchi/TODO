# Todoit — Clarity, finally.

> A clean, focused task management web app built with Django. Capture every task, stay organized, and actually get things done.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Deployed](https://img.shields.io/badge/Deployed-Railway-purple)

**Live demo:** [todo-production-cbc3e.up.railway.app](https://todo-production-cbc3e.up.railway.app)

---

## Screenshots

| Inbox | Task Detail | Landing |
|-------|-------------|---------|
| Task list with priority colors, category badges, due dates | Full task detail with meta panel | Landing page with features, testimonials, CTA |

---

## Features

- **Inbox** — all your tasks in one place, sorted and clean
- **Today view** — only tasks due today
- **Completed** — track what you've already done
- **Add / Edit / Delete tasks** — full CRUD with a smooth modal card UI
- **Priority levels** — 4 levels with color coding (red → orange → blue → grey)
- **Categories** — Personal, Work, Home
- **Due dates** — date picker with formatted label
- **Search** — find tasks by title
- **Sidebar** — collapsible on desktop (slim 48px bar), overlay on mobile with animation
- **Authentication** — register, login, logout with per-user data isolation
- **Flash messages** — success/error alerts with auto-dismiss
- **Responsive** — works on mobile and desktop

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0 (Python) |
| Database | PostgreSQL (production) / SQLite (local) |
| Frontend | Vanilla HTML, CSS, JavaScript |
| Fonts | DM Sans + DM Serif Display (Google Fonts) |
| Deployment | Railway |
| Static files | WhiteNoise |

---

## Project Structure

```
todo/                          # Django project config
├── settings.py
├── urls.py
└── wsgi.py

Task/                          # Main app
├── models.py                  # Task, Category models
├── views.py                   # All views
├── forms.py                   # TaskForm
├── urls.py                    # App URL patterns
├── context.py                 # Sidebar context processor
├── templatetags/
│   └── task_filters.py        # Custom filters (priority_color, category_icon...)
├── templates/
│   ├── base2.html             # Base layout (sidebar + alerts)
│   ├── landing.html           # Public landing page
│   ├── app/
│   │   ├── inbox.html
│   │   ├── today.html
│   │   ├── completed.html
│   │   ├── search.html
│   │   ├── task_detail.html
│   │   ├── task_form.html
│   │   ├── task_update.html
│   │   └── task_confirm_delete.html
│   └── components/
│       ├── sidebar.html
│       ├── task_item.html
│       └── toggle_done.html
└── static/
    ├── styles/
    │   ├── main.css            # Global variables + layout
    │   ├── sidebar.css
    │   ├── inbox.css
    │   ├── task_detail.css
    │   ├── task_form.css
    │   ├── toggle_done.css
    │   └── login.css
    └── scripts/
        ├── main.js             # Sidebar toggle + add task card
        ├── task_form.js        # Dropdowns, date label, submit guard
        └── confirm.js          # Delete confirm modal

Auth/                          # Auth app (login, signup)
```

---

## Data Models

### Category
```python
name = IntegerField(choices=[(1, 'Personal'), (2, 'Work'), (3, 'Home')])
```

### Task
```python
title       = CharField(max_length=255)
description = TextField(blank=True)
is_done     = BooleanField(default=False)
priority    = IntegerField(choices=[1..4])
due_date    = DateTimeField(null=True)
created_at  = DateTimeField(auto_now_add=True)
updated_at  = DateTimeField(auto_now=True)
user        = ForeignKey(User)
category    = ForeignKey(Category, null=True)
```

---

## Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/todo.git
cd todo
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit `http://localhost:8000`

---

## Deployment (Railway)

The app is configured to deploy on [Railway](https://railway.app) with PostgreSQL.

### Environment variables required on Railway:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | your strong secret key |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app.up.railway.app` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-app.up.railway.app` |
| `DATABASE_URL` | auto-injected by Railway PostgreSQL plugin |

### Procfile
```
web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn todo.wsgi
```

---

## Custom Template Filters

Located in `Task/templatetags/task_filters.py`:

| Filter | Input | Output |
|--------|-------|--------|
| `priority_icon` | `1..4` | SVG icon with priority color |
| `priority_color` | `1..4` | Hex color string |
| `priority_label` | `1..4` | `"Priority 1"` etc. |
| `category_icon` | `1..3` | SVG icon |
| `category_label` | `1..3` | `"Personal"` etc. |
| `category_color` | `1..3` | Hex color string |

Usage in templates:
```django
{{ task.priority|priority_color }}
{{ task.category.name|category_icon }}
```

---

## URL Routes

| URL | View | Name |
|-----|------|------|
| `/` | Landing page | `landing` |
| `/inbox/` | All tasks | `inbox` |
| `/taday/` | Today's tasks | `today` |
| `/completed/` | Completed tasks | `completed` |
| `/search/` | Search tasks | `search` |
| `/tasks/add-task/` | Add task | `AddTask` |
| `/tasks/<id>/` | Task detail | `TaskDetail` |
| `/tasks/<id>/update/` | Edit task | `TaskUpdate` |
| `/tasks/<id>/delete/` | Delete task | `TaskDelete` |
| `/tasks/<id>/toggle/` | Toggle done | `TaskToggle` |
| `/auth/login/` | Login | `login` |
| `/auth/signup/` | Register | `signup` |
| `/logout/` | Logout | `logout` |

---

## What I Learned

- Django ForeignKey relationships and how `get_FOO_display()` works with integer choice fields
- Custom template tags and filters
- WhiteNoise for static files in production
- Railway deployment with PostgreSQL and environment variables
- CSS variables and component-based styling without any framework
- Intersection Observer API for scroll animations
- Mobile-first sidebar with CSS transitions

---

## Future Improvements

- [ ] Password reset by email
- [ ] Task search with `icontains` (currently exact match only)
- [ ] Due date notifications / reminders
- [ ] Drag and drop task reordering
- [ ] Subtasks
- [ ] Dark mode
- [ ] REST API + mobile app

---

## License

MIT — free to use and modify.

---

*Built with Django & ♥*
