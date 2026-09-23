### Warehouse Management Web API

A modern, robust, and asynchronous-ready Warehouse Management Web API built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic** v2. This project demonstrates industry-standard backend architecture, data validation, database normalization, and secure resource lifecycle management. 

### 🚀 Key Features

* **RESTful API Architecture:** Fully compliant with HTTP methods (GET, POST, PUT, DELETE) for intuitive resource manipulation.
* **Advanced Schema Validation:** Powered by **Pydantic** to decouple database representations from request/response payloads (ItemCreate, ItemResponse, etc.).
* **Automatic API Documentation:** Native integration with **Swagger UI** (/docs) used actively as a live interactive environment for testing and debugging.
* **Relational Database Design:** Two separate, normalized tables separating the Official Product Registry (Item) from Physical Inventory (Magazzino).
* **Dependency Injection & Connection Pools:** Implements the official FastAPI dependency pattern (Depends(get_db)) with a strict try/finally context manager to guarantee explicit connection cleanup and avoid leaks.
* **Data Integrity & Business Logic:** Strict database constraints (unique=True, nullable=False), automatic input casing (.upper()), and server-side validation preventing illegal states (e.g., negative stock).

### 🛠️ System Architecture & Modularity

The project strictly adheres to the **Separation of Concerns (SoC)** principle, making it highly maintainable and ready to scale: 

* **main.py (API Layer):** Configures FastAPI routes, orchestrates inputs, enforces HTTP status codes natively via HTTPException (e.g., 404 Not Found), and delegates data manipulation.
* **models.py (Data & Schema Layer):**

 Houses both SQLAlchemy ORM models (inheriting from an abstract BaseModello to share common attributes like id) and Pydantic validation schemas utilizing from_attributes = True for smooth object-to-JSON serialization.
* **db.py (Infrastructure Layer):** Establishes the database engine connectivity, session factory configurations (autocommit=False), and handles runtime transaction lifecycles.

### Tech Stack

* **Framework:** FastAPI
* **Validation:** Pydantic v2
* **ORM:** SQLAlchemy (Object-Relational Mapping)
* **Database Engine:** SQLite3

### 📋 Database Schema

### 1. items (Product Registry)

* id (INTEGER, Primary Key)
* code (STRING, Unique, Not Null) — *The official SKU/Barcode*
* name (STRING, Unique, Not Null)

### 2. magazzino (Physical Inventory)

* id (INTEGER, Primary Key)
* code (STRING, Unique, Not Null)
* name (STRING, Not Null)
* quantity (INTEGER)

### 💻 How to Run & Test

1. Clone the repository: 

bash

git clone https://github.com/CocoJambis/Warehouse-Management-System-CLI-API.git
cd Warehouse-Management-System-CLI-API

Usa il codice con cautela.
2. Install dependencies: 

bash

pip install fastapi uvicorn sqlalchemy pydantic

Usa il codice con cautela.
3. Launch the live Uvicorn server: 

bash

uvicorn main:app --reload

Usa il codice con cautela.
4. Open your browser and navigate to **http://127.0.0.1:8000/docs** to access the interactive **Swagger UI** documentation to test and debug all endpoints directly from the interface.
