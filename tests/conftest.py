import pytest
from app.main import Calculator

@pytest.fixture
def calculator():
    return Calculator()
