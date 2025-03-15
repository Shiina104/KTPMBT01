from bank import value
import pytest

@pytest.mark.value
def test_value_hello():
    assert value("hello") == 0

@pytest.mark.value
def test_value_h():
    assert value("H") == 20

@pytest.mark.value
def test_value_none():
    assert value("what") == 100