import pytest

@pytest.fixture
def sample_data():
    return {"name": "Aatish", "age": 20}

def test_name(sample_data):
    assert sample_data["name"] == "Aatish"
