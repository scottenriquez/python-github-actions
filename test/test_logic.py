from services.logic import *

def test_add_for_positive_numbers():
  assert add(2, 3) == 5

def test_add_for_negative_numbers():
  assert add(-2, -3) == -5