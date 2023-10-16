from src.calculator import Calculator

def test_subtract():
    #Set up
    calc = Calculator()
    #Test
    assert calc.subtract(2,2) == 0
    assert calc.subtract(2,2) != 1
