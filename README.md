
---

🛠️ FastAPI Project Setup Guide
---

## 1. Initialize the Virtual Environment

```bash
python -m venv <your-env-name>
```

## 2. Activate the Virtual Environment

```bash
<your-env-name>\Scripts\activate  # On Windows
# Or:
source <your-env-name>/bin/activate  # On macOS/Linux
```

>  Ensure your Python interpreter is set to use the virtual environment you've just created.

---

## 3. Install Dependencies

```bash
cd src
pip install -r requirements.txt
cd ..
```

---

## 4. Create `.env` File in `src/`

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
## 5. Run Alembic Migrations

```bash
alembic upgrade head
```

---

## 6. Start the FastAPI Server

Navigate to the `src/` directory and run:

```bash
python main.py
# or use uvicorn (recommended)
uvicorn main:app --reload
```

---
