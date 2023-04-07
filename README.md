# Address Book API

A FastAPI application to manage an address book with CRUD operations and search functionality.

## Requirements

- Python 3.9 or higher
- FastAPI
- SQLAlchemy

## Installation

1. Clone this repository:
git clone https://github.com/dslavov23/addresses.git

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # For Windows, use "venv\Scripts\activate"

3. Install the required packages:
pip install fastapi[all] sqlalchemy


## Running the Application

1. Create the SQLite database:
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

2. Run the FastAPI server:
python main.py

3. Open your browser and navigate to:
(http://127.0.0.1:8000/docs) to access the Swagger UI and test the application.



