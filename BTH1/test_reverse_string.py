import pytest
from reverse_string import reverse_string

@pytest.mark.reversestring
def test_reverse_string():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abcde") == "edcba"
    assert reverse_string("  ads gd  sd   ") == ""