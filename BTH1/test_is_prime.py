import pytest
from is_prime import is_prime

#@pytest.mark.isprime
def test_is_prime_1():
    assert is_prime(-5) == False

#@pytest.mark.isprime
def test_is_prime_2():
    assert is_prime(29) == True

#@pytest.mark.isprime
def test_is_prime_3():
    assert is_prime(25) == True