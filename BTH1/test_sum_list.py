import pytest
from sum_list import sum_list

#@pytest.mark.sumlist
def test_sum_list_nonelist():
    assert sum_list([]) == 0

#@pytest.mark.sumlist
def test_sum_list_one():
    assert sum_list([5]) == 5

#@pytest.mark.sumlist
def test_sum_list():
    assert sum_list([6, 1, 5, 6, 7, 1])

#@pytest.mark.sumlist
def test_sum_list2():
    assert sum_list([6, -1, 5, -6, -7, 1]) == 2