<div align="center">

# 📒 ClassLedger (STUDENT MANAGEMENT SYSTEM)

**A lightweight student record manager built with FastAPI + SQLite**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?logo=jinja&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white)

</div>
---

## 🧭 At a Glance

| | |
|---|---|
| **What it does** | Create, view, update and delete student records |
| **Rendering** | Server-side with Jinja2 templates |
| **Database** | SQLite, auto-created on first run |
| **Validation** | Pydantic model on every form submit |
| **Security** | Parameterized SQL queries (no SQL injection) |
| **Form safety** | Post/Redirect/Get (303), refresh never resubmits |

---

## 🗃️ Student Record

| Field | Type |
|---|---|
| `id` | integer, auto-increment, primary key |
| `name` | text, required |
| `age` | integer |
| `gender` | text |
| `marks` | integer |
| `course` | text |
| `image` | text (image URL/path) |
| `status` | integer (0 / 1) |

---

## 🔗 Routes

| Method | URL | Purpose |
|---|---|---|
| GET | `/students` | List all students |
| GET | `/students/add` | Show add form |
| POST | `/students/add` | Save new student |
| GET | `/students/{id}` | View one student |
| GET | `/students/{id}/update` | Show edit form |
| POST | `/students/{id}/update` | Save changes |
| POST | `/students/{id}/delete` | Delete student |

---

## 📁 Project Structure

```
STUDENT_MANAGEMENT_SYSTEM/
├── main.py            # app, routes, DB logic
├── students.db        # created automatically
└── templates/
    ├── students.html
    ├── add-student.html
    ├── one-std.html
    └── update-student.html
```

---

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/ram-yadav-390/STUDENT_MANAGEMENT_SYSTEM.git
cd STUDENT_MANAGEMENT_SYSTEM

# 2. Install dependencies
pip install fastapi uvicorn jinja2 python-multipart

# 3. Run
uvicorn main:app --reload
```

Open **http://127.0.0.1:8000/students**

> `python-multipart` is required for form handling.

---

## 🔮 Roadmap

- [ ] Search and filter by course / status
- [ ] Pagination on the student list
- [ ] Real image upload (`UploadFile`)
- [ ] Dashboard with average marks per course
- [ ] Admin login

---

## 👤 Author

**Ram Yadav**
GitHub: [@ram-yadav-390](https://github.com/ram-yadav-390)

---

<div align="center">

⭐ Star the repo if you found it useful

</div>

