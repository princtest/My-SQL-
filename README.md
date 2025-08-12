# 🚀 FastAPI + MySQL Boilerplate

Python FastAPI + MySQL starter template — जिसमें **SQLAlchemy ORM**, **Alembic migrations**, **Docker/Docker Compose**, और **GitHub Actions CI** सब कुछ पहले से configured है।

## ✨ Features

- ⚡ **FastAPI** backend with automatic Swagger docs (`/docs`)
- 🗄 **MySQL** database (Dockerized)
- 🛠 **SQLAlchemy ORM** models & CRUD
- 🔄 **Alembic** migrations system
- 🐳 **Dockerfile** + **docker-compose.yml** for local & production setup
- ✅ **Pytest** unit tests (in-memory SQLite for speed)
- 🔍 **Linting** with Black & Flake8
- 🔁 **GitHub Actions CI** (runs tests + lint on push/PR)
- 📂 Example `users` & `items` API endpoints

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2️⃣ Copy .env file and set DB URL

cp .env.example .env

Edit .env to match your DB settings:

DATABASE_URL=mysql+pymysql://user:password@db:3306/mydatabase


---

🐳 Run with Docker (Recommended)

Build and start services:

docker-compose up --build

📌 This will start:

db → MySQL container at localhost:3306

web → FastAPI app at http://localhost:8000


Run Alembic migrations (inside container):

docker-compose exec web alembic upgrade head

Stop services:

docker-compose down


---

💻 Run Locally (without Docker)

1. Create virtual environment

python -m venv .venv
source .venv/bin/activate  # Windows → .venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Set environment variable

export DATABASE_URL="mysql+pymysql://user:password@127.0.0.1:3306/mydatabase"

(Windows PowerShell)

$env:DATABASE_URL="mysql+pymysql://user:password@127.0.0.1:3306/mydatabase"

4. Run migrations

alembic upgrade head

5. Start FastAPI server

uvicorn app.main:app --reload

➡ App available at: http://127.0.0.1:8000


---

🧪 Running Tests

pytest -q

📌 Tests use in-memory SQLite — no need for MySQL during unit testing.


---

📜 API Docs

Once server is running:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc



---

🔄 Common Commands

Create new Alembic migration:

alembic revision --autogenerate -m "add new table"

Upgrade DB to latest migration:

alembic upgrade head

Format code with Black:

black .

Lint code with Flake8:

flake8


---

🛡 GitHub Actions CI

On every push/PR:

Runs Black (code formatting check)

Runs Flake8 (lint)

Runs pytest (tests)



---

👨‍💻 Author

Your Name — GitHub @Princtest