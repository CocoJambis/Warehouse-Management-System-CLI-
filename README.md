# Warehouse Management System (CLI)

A robust and modular Warehouse Management System built in Python using **SQLAlchemy ORM** and an **SQLite** database. This project demonstrates backend architecture best practices, data integrity, and strict separation of concerns.

## 🚀 Features

- **Relational Database Design:** Two separate, normalized tables for Official Product Registry (`Item`) and Physical Inventory (`Magazzino`).
- **Data Integrity:** Strict constraints including data types, unique constraints (`unique=True`), and non-nullable fields (`nullable=False`).
- **Full CRUD Operations:** Complete transactional lifecycle management (Create, Read, Update, Delete) abstracted through an ORM layer.
- **Robust Error Handling:** Comprehensive `try/except` blocks protecting the interface from crashes due to invalid user inputs.
- **Smart Business Logic:** Automatically prevents negative stock, formats text inputs (`.upper()` / `.lower()`), and handles selective bulk deletions (`.delete()`) for items out of stock.

---

## 🛠️ Architecture & Technologies

The project is structured following professional backend development standards:
- **`main.py`**: The Presentation Layer. Handles user interaction (CLI) via a modern `match/case` loop and ensures User Experience (UX) safety (e.g., confirmation prompts before destructive actions).
- **`crud.py`**: The Business Logic / Data Access Layer. Contains atomic, reusable functions to query and mutate the database state without mixing UI concerns.
- **`db.py`**: The Infrastructure Layer. Configures the SQLAlchemy engine, session maker, base declarative metadata, and maps the relational schemas.

### Tech Stack
* **Language:** Python 3.10+
* **Database Framework:** SQLAlchemy ORM
* **Database Engine:** SQLite3

---

## 📋 Database Schema

### 1. `items` (Product Registry)
* `id` (INTEGER, Primary Key)
* `code` (STRING, Unique, Not Null) — *The official SKU/Barcode*
* `name` (STRING, Not Null)

### 2. `magazzino` (Physical Inventory)
* `id` (INTEGER, Primary Key)
* `code` (STRING, Unique, Not Null)
* `name` (STRING, Not Null)
* `quantity` (INTEGER)
