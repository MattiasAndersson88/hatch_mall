from src.calculator import Calculator

def test_divide():
    #Set up
    calc = Calculator()
    #Test
    assert calc.divide(2,2) == 1
    assert calc.divide(2,2) != 2
