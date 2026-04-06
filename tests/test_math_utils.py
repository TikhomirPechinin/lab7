import pytest
from my_library.math_utils import calculate_mean, factorial, is_prime

def test_calculate_mean_positive():
    assert calculate_mean([1, 2, 3]) == 2

def test_calculate_mean_float():
    assert calculate_mean([1, 2, 3, 4]) == 2.5

def test_calculate_mean_single():
    assert calculate_mean([10]) == 10

def test_calculate_mean_empty():
    with pytest.raises(ValueError):
        calculate_mean([])

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)

def test_is_prime_true():
    assert is_prime(7) is True
    assert is_prime(13) is True
    assert is_prime(2) is True

def test_is_prime_false():
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False