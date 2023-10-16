from src.calculator import Calculator
import unittest
def test_multiplicate():
    #Set up
    calc = Calculator()
    #Test
    assert calc.multiplicate(2,2) == 4
    assert calc.multiplicate(2,2) != 5
