# tests/test_my_project.py

# Import the function to be tested from src/my_project.py
from src.my_project import add_numbers

# Test case 1: Add two positive numbers
def test_add_numbers():
    assert add_numbers(2, 3) == 5  # This should pass as 2 + 3 = 5

# Test case 2: Add negative numbers
def test_add_numbers_negative():
    assert add_numbers(-1, -1) == -2  # This should pass as -1 + (-1) = -2
