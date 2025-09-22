# Expense Tracker API

A FastAPI-based backend for a simple expense manager application. This project provides RESTful APIs for tracking expenses, managing users, and organizing expense categories, all backed by a PostgreSQL database.

## Features

- **User Management**: Register, login, and update user profiles.
- **Expense Tracking**: Add, edit, delete, and view expenses.
- **Category Management**: Organize expenses under customizable categories.
- **Summary & Analytics**: Get summaries of expenses by date, category, or user.
- **Secure Authentication**: JWT-based authentication for API access.
- **PostgreSQL Integration**: Persistent, scalable data storage.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Authentication**: JWT Tokens
- **Environment**: Python 3.10+

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rastogiharshita/expense_tracker.git
cd expense_tracker
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and set your database connection string and secret key:

```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<db_name>
SECRET_KEY=your_jwt_secret
```

### 5. Run Database Migrations

If using Alembic or manual migration scripts, run them to initialize tables.

```bash
alembic upgrade head
```

### 6. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`.

## Usage

- Interactive API docs at [`/docs`](http://localhost:8000/docs)
- Redoc docs at [`/redoc`](http://localhost:8000/redoc)

## Example Endpoints

- `POST /users/register` — Register a new user
- `POST /users/login` — Authenticate and get JWT
- `GET /expenses/` — List all expenses for user
- `POST /expenses/` — Add a new expense
- `GET /categories/` — List expense categories

## Project Structure

```
expense_tracker/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── auth.py
│   └── routers/
│       ├── users.py
│       ├── expenses.py
│       └── categories.py
├── tests/
├── requirements.txt
├── alembic/
└── README.md
```

## Contributing

Pull requests and suggestions are welcome! Please open an issue first to discuss what you’d like to change.

## License

MIT

---

**Author:** [Harshita Rastogi](https://github.com/rastogiharshita)