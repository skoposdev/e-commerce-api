# e-commerce-api

A RESTful API for an e-commerce application built with FastAPI and PostgreSQL.

## Stack

- **FastAPI** — web framework
- **PostgreSQL** — database
- **SQLAlchemy** — ORM
- **Alembic** — database migrations
- **Pydantic** — data validation

## Installation

### Prerequisites

- Python 3.11+
- PostgreSQL

### Setup

1. Clone the repository

```bash
git clone https://github.com/ton-user/e-commerce-api.git
cd e-commerce-api
```

2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables

Create a `.env` file at the root of the project:

```env
DATABASE_URL=postgresql+psycopg2://user:password@localhost/ecommerce
```

4. Run migrations

```bash
alembic upgrade head
```

5. Start the server

```bash
fastapi dev main.py
```

The API is available at `http://localhost:8000`  
Interactive documentation at `http://localhost:8000/docs`

## Endpoints

### Categories

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/categories` | Get all categories |
| POST | `/api/categories` | Create a category |
| PATCH | `/api/categories/{category_id}` | Update a category |
| DELETE | `/api/categories/{category_id}` | Delete a category |

### Products

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/api/products` | Get all products |
| POST | `/api/products` | Create a product |
| PATCH | `/api/products/{product_id}` | Update a product |
| DELETE | `/api/products/{product_id}` | Delete a product |
