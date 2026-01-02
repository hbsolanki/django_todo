cat <<EOF > README.md

# 📝 django_todo (Django Template Based)

A simple **Todo Application built using Django Templates**.  
This project focuses on **server-side rendering**, Django fundamentals, and clean CRUD operations, using **PostgreSQL** as the database.

---

## 🚀 Features

- Create, update, delete todo items
- Server-side rendering with Django Templates
- PostgreSQL database integration
- Clean and beginner-friendly Django structure
- Environment-based configuration using \`.env\`

---

## 🛠 Tech Stack

- Python
- Django
- PostgreSQL
- HTML / CSS
- python-dotenv

---

## 📦 Project Setup (Step-by-Step)

### 1️⃣ Clone the Repository

\`\`\`bash
git clone https://github.com/your-username/django_todo.git
cd django_todo
\`\`\`

---

### 2️⃣ Create & Activate Virtual Environment

\`\`\`bash
python3 -m venv myenv
source myenv/bin/activate
\`\`\`

**Windows:**
\`\`\`bash
myenv\\Scripts\\activate
\`\`\`

---

### 3️⃣ Install Dependencies

\`\`\`bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
\`\`\`

---

## 🔐 Environment Variables Setup

### 4️⃣ Create \`.env\` file

Copy from template:

\`\`\`bash
cp .env.template .env
\`\`\`

### 📄 \`.env.template\`

\`\`\`env

# Django settings

DEBUG=True
SECRET_KEY=your-secret-key

# PostgreSQL Database

DB_NAME=django_todo
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
\`\`\`

⚠️ **Do NOT commit \`.env\` to GitHub**

---

## 🗄 PostgreSQL Configuration (Django)

In **settings.py**:

\`\`\`python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(**file**).resolve().parent.parent

DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql",
"NAME": os.getenv("DB_NAME"),
"USER": os.getenv("DB_USER"),
"PASSWORD": os.getenv("DB_PASSWORD"),
"HOST": os.getenv("DB_HOST"),
"PORT": os.getenv("DB_PORT"),
}
}
\`\`\`

---

### 5️⃣ Create Database (PostgreSQL)

\`\`\`bash
psql postgres
\`\`\`

\`\`\`sql
CREATE DATABASE django_todo;
\`\`\`

Exit:
\`\`\`sql
\\q
\`\`\`

---

### 6️⃣ Apply Migrations

\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

---

### 7️⃣ Create Superuser (Optional)

\`\`\`bash
python manage.py createsuperuser
\`\`\`

---

### 8️⃣ Run Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Open in browser:
\`\`\`
http://127.0.0.1:8000/
\`\`\`

---

## 📁 Project Structure

\`\`\`
django_todo/
├── todo/
│ ├── migrations/
│ ├── templates/
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── django_todo/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
├── .env.template
├── .gitignore
└── README.md
\`\`\`

---

## 📦 requirements.txt (Example)

\`\`\`txt
Django>=4.2
psycopg2-binary
python-dotenv
\`\`\`

---

## 🧪 Useful Commands

\`\`\`bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
\`\`\`

---

## ❗ Notes

- PostgreSQL must be running before starting the server
- \`.env\` is required for database connection
- Ideal for learning Django with a real production-style DB setup

---

## 📌 Future Improvements

- User authentication
- Task priorities & due dates
- Pagination
- UI enhancements
- Deployment (Render / Railway / VPS)

---

## 📄 License

Open-source and free to use for learning purposes.

---

## 🙌 Author

Built with Django Templates & PostgreSQL for learning and practice.
EOF
