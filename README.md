Dưới đây là phiên bản được viết lại của README với ngôn ngữ rõ ràng hơn, trình bày mạch lạc, dùng markdown chuẩn và chuyên nghiệp hơn:

---

# 🛠️ FastAPI Project Setup Guide

This guide will walk you through setting up the virtual environment, installing dependencies, configuring environment variables, running Alembic migrations, and starting the FastAPI server.

---

## 📦 1. Initialize the Virtual Environment

```bash
python -m venv <your-env-name>
```

## ▶️ 2. Activate the Virtual Environment

```bash
<your-env-name>\Scripts\activate  # On Windows
# Or:
source <your-env-name>/bin/activate  # On macOS/Linux
```

> ⚠️ Ensure your Python interpreter is set to use the virtual environment you've just created.

---

## 📚 3. Install Dependencies

```bash
cd src
pip install -r requirements.txt
cd ..
```

---

## 🔐 4. Create `.env` File in `src/`

Create a `.env` file inside the `src/` directory and populate it with your environment variables:

```ini
database_username=<your-database-username>
database_password=<your-database-password>
database_hostname=<your-database-hostname>
database_portnumber=<your-database-port>
database_name=<your-database-name>

secret_key=<your-secret-key>
algorithm=<your-jwt-algorithm>
access_token_exp_time=<access-token-expiry-time>
```

---

## 🔧 5. Initialize Alembic

```bash
alembic init migration
```

This will create a `migration/` directory containing Alembic configuration files.

---

## ⚙️ 6. Configure `alembic.ini`

Open `alembic.ini` and clear the default URL line:

```ini
sqlalchemy.url =
```

> 💡 You can also paste the full DB connection string here if you prefer not to load from the `.env`.

---

## 🧬 7. Configure `env.py` inside `migration/`

Edit the `env.py` file to load the database connection dynamically and import metadata:

```python
from src.models import Base
from src.database.engine import engine
from core.config.envConfig import settings

# Set DB connection from .env settings
config.set_main_option(
    "sqlalchemy.url", f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_portnumber}/{settings.database_name}"
)

# Use model metadata for Alembic autogenerate
target_metadata = Base.metadata
```

---

## 🚀 8. Run Alembic Migrations

```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

---

## 🏁 9. Start the FastAPI Server

Navigate to the `src/` directory and run:

```bash
python main.py
# or use uvicorn (recommended)
uvicorn main:app --reload
```

---
