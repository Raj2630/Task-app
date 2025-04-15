# 🧩 FastAPI Task Board Application

This is a lightweight web-based Task Board application built using **FastAPI** with **Jinja2** templating. The project showcases clean routing and dynamic rendering of task boards using HTML templates and static assets.

---

## 🚀 Features

- Simple login/home interface (`/`)
- Task board listing view (`/boards`)
- Dynamic task board detail pages (`/board/{board_id}`)
- Serves static content like CSS and JavaScript
- FastAPI-powered backend for easy development and scalability

---

## 📁 Project Structure


. ├── main.py ├── requirements.txt ├── README.md ├── templates/ │ ├── index.html │ ├── boards.html │ └── board.html └── static/ ├── style.css


---

## 🧰 Prerequisites

Make sure you have Python 3.8 or higher installed.

Then install dependencies with:

```bash
pip install -r requirements.txt


python main.py
uvicorn main:app --reload
