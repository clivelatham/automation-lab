# Automation Lab

A simple API test automation project built with **Python**, **pytest**, and **Flask**.

This project demonstrates how to design and structure automated API tests, including:
- smoke tests
- route tests
- positive and negative contract testing
- environment-based configuration

---

## Project Structure
automation-lab/
│
├── app.py # Simple Flask API used as the system under test
├── requirements.txt # Python dependencies
├── pytest.ini # Pytest configuration
├── tests/
│ ├── Smoke/ # Basic health and version checks
│ ├── Routes/ # Route availability and status tests
│ ├── Contracts/ # API response contract tests
│ └── conftest.py # Shared pytest fixtures and configuration
└── README.md


---

## API Endpoints

The Flask application exposes the following endpoints:

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/health` | Health check endpoint |
| GET | `/version` | Service metadata |
| GET | unknown | Returns JSON 404 error |

---

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1

**Install dependencies**
pip install -r requirements.txt

**Start the API server**
python app.py

**Start the API server**
python app.py

**Running the Tests**

With the server running in a separate terminal:
pytest

Or quieter output:
pytest -q

**Purpose**
-This project is intended for learning and demonstrating:
-API test automation fundamentals
-pytest fixtures and structure
-contract testing concepts
-clean environment and dependency management
-basic Git and GitHub workflows


