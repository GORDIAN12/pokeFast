# Pokémon API with FastAPI

A **RESTful API built with FastAPI** to manage Pokémon and their evolutions.  
This project demonstrates how to build a backend API using **FastAPI, SQLModel, and SQLite**, including data validation, filtering, and relational models.

The API allows users to **create Pokémon, retrieve them, filter by type, and search by name**.

---

# Features

- RESTful API built with **FastAPI**
- Database management using **SQLModel + SQLite**
- Data validation using **Pydantic**
- Pokémon evolution relationships
- Filtering Pokémon by type
- Searching Pokémon by name
- CRUD operations
- Database session dependency injection
- Optional evolution creation when adding Pokémon

---

# Tech Stack

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Pydantic**
- **Alembic** (for migrations)

---
```bash

# Project Structure
pokemon-fastapi/
│
├── main.py
├── models.py
├── db.py
├── db.sqlite
├── api.http
└── README.md
```

---
# Database Models

## Pokemon

| Field | Type | Description |
|------|------|-------------|
| id | int | Primary key |
| name | string | Pokémon name |
| tipo1 | string | Primary type |
| tipo2 | string | Secondary type |
| date_formed | date | Optional creation date |
| evoluciones | list | Related evolution records |

---

## Evolucion

| Field | Type | Description |
|------|------|-------------|
| id | int | Primary key |
| subname | string | Evolution name |
| fecha_aparicion | date | Evolution appearance date |
| poke_id | int | Foreign key referencing Pokémon |

---
# Get Pokemons

Optional query parameters:

- `tipo` → filter by Pokémon type
- `q` → search Pokémon by name

Example:
```bash

GET /pokemons?tipo=fuego
GET /pokemons?q=char
```


## Get Pokémon by ID

```bash
GET /pokemons/{id}
```


Example request body:

```json
{
  "name": "Charmander",
  "tipo1": "Fuego",
  "tipo2": "Normal"
}
```
## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pokemon-fastapi.git
cd pokemon-fastapi
```
```bash
pip install fastapi uvicorn sqlmodel pydantic

```

# Running the API

Run the FastAPI server:
```bash
uvicorn main:app --reload
```
# The API will be available at:
```bash
http://localhost:8000

```

# Alternative documentation

```bash
http://localhost:8000/redoc
```

