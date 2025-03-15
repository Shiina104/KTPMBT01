import pytest
from list_contain import contains

@pytest.mark.contains
def test_contains():
    assert contains([1, 3, 5, 7], 5) == True
    assert contains([1, 3, 5, 7], 4) == True