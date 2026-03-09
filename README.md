# Pokémon API 

A **RESTful API built with FastAPI** to manage Pokémon and their evolutions.

This project demonstrates how to build a **modern backend API** using **FastAPI, SQLModel, and SQLite**, including data validation, filtering, and relational database models.

The API allows users to:

- Create Pokémon
- Retrieve Pokémon
- Filter Pokémon by type
- Search Pokémon by name
- Store Pokémon evolutions

---

# Features

- RESTful API with **FastAPI**
- Database ORM using **SQLModel**
- **SQLite database**
- **Pydantic validation**
- Pokémon evolution relationships
- Filtering Pokémon by type
- Searching Pokémon by name
- Dependency injection for database sessions
- Automatic interactive API documentation

---

# Tech Stack

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Pydantic**
- **Uvicorn**
- **Alembic** (database migrations)

---

```bash
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
# Project Structure
## API Endpoints

GET /pokemons

Optional query parameters:

| Parameter | Description |
|-----------|-------------|
| tipo | Filter Pokémon by type |
| q | Search Pokémon by name |

Example:

GET /pokemons?tipo=fuego
GET /pokemons?q=char


---

## Get Pokémon by ID
GET /pokemons/{id}

GET /pokemons/3
---

## Create Pokémon
POST /pokemons

Example request:

```json
{
  "name": "Charmander",
  "tipo1": "Fuego",
  "tipo2": "Normal"
}

```
Example with evolutions
```json
{
  "name": "Bulbasaur",
  "tipo1": "Planta",
  "tipo2": "Veneno",
  "evoluciones": [
    {
      "subname": "Ivysaur",
      "fecha_aparicion": "2001-12-28"
    },
    {
      "subname": "Venusaur",
      "fecha_aparicion": "2001-12-28"
    }
  ]
}

```

## Installation
```bash 
git clone https://github.com/your-username/pokemon-fastapi.git
cd pokemon-fastapi
pip install fastapi uvicorn sqlmodel pydantic
uvicorn main:app --reload

```
