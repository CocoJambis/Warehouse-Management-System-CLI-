# Dual-Interface Warehouse Management System

A comprehensive Warehouse Management System in Python featuring a dual implementation: a **Web API (FastAPI)** and a local **CLI**, powered by **SQLAlchemy ORM** and **SQLite**.

---

## 📁 Repository Structure
* **`cli_version/`**: Local application layer with an interactive terminal interface.
* **`api_version/`**: Web infrastructure exposing RESTful endpoints and input validation.

---

## 🚀 Key Features
- **Relational Design:** Normalized tables for Product Registry (`Item`) and Physical Inventory (`Magazzino`).
- **Data Integrity:** Strict structural constraints and transactional lifecycles via SQLAlchemy.
- **Web API (`api_version/`):** RESTful endpoints, Pydantic v2 validation, automatic Swagger documentation, and dependency injection.

---

## 🛠 Tech Stack & Schema
* **Stack:** Python 3.10+, FastAPI, Pydantic v2, SQLAlchemy, SQLite3.
* **Schema:** `items` (Product Registry) and `magazzino` (Physical Inventory with quantities).

---

## 💻 How to Run
Clone the repo and install dependencies (`fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`), then run either the CLI (`cd cli_version && python main.py`) or the API (`cd api_version && uvicorn main:app --reload`).
