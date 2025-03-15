import pytest
from divide import divide

#@pytest.mark.testdivide
def test_divide():
    assert divide(5, 2)
    assert divide(-7, 3)
    assert divide(3, 1) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(8, 0)