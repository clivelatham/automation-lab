import os
import pytest
import requests
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv(override=True)

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://127.0.0.1:5000").rstrip("/")

@pytest.fixture(scope="session")
def timeout():
    return int(os.getenv("TIMEOUT", "5"))

@pytest.fixture(scope="session")
def http():
    session = requests.Session()
    yield session
    session.close()



