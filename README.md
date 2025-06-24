# 📚 Bookstore API

A modern FastAPI application to manage a simple bookstore. It supports asynchronous endpoints, SQLite for storage, SQLAlchemy for ORM, and Pydantic for validation.

---

## 🚀 Features

✅ Create a new book  
✅ Get all books (with pagination)  
✅ Get a book by ID  
✅ Async support using `async SQLAlchemy + aiosqlite`  
✅ Clean code structure (separated into `main.py`, `models.py`, `schemas.py`, `crud.py`, `database.py`)  
✅ Welcome route  
✅ Basic test support using `pytest` 

---

## 🛠️ Project Structure

```
bookstore-api/
├── main.py           # Entry point with routes
├── models.py         # SQLAlchemy ORM models
├── schemas.py        # Pydantic schemas
├── crud.py           # Database logic (CRUD)
├── database.py       # Async DB connection + session setup
├── test_main.py      # Async test file
├── requirements.txt  # Project dependencies
```

---

## 💻 How to Run

### 1. ✅ Clone the repository

```bash
git clone https://github.com/your-username/bookstore-api.git
cd bookstore-api
```

### 2. ✅ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### 4. ✅ Run the app using Uvicorn

```bash
uvicorn main:app --reload
```

📍 Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
📘 Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
📕 ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Run Tests

```bash
pytest test_main.py
```

✅ Make sure you installed `pytest` 

---

## 📦 Example `requirements.txt`

```
fastapi
uvicorn
sqlalchemy
aiosqlite
pydantic
pytest
httpx
```

---

## 💡 Notes

- Data is stored in `books.db` (SQLite)
- You can easily switch to PostgreSQL/MySQL by updating the connection URL in `database.py`
- Cleanly separated logic for maintainability and scalability

---

## 📬 Contact

Made with ❤️ using FastAPI
