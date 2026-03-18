from unittest.mock import patch


# real function
def get_temperature():
    return 30  # imagine API call


# function we want to test
def is_hot():
    temp = get_temperature()
    return temp > 25


# TEST
def test_is_hot():
    with patch("mocking_example.get_temperature", return_value=20):
        assert is_hot() == False
