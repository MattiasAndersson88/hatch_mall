from src.calculator import Calculator

def test_add():
    #Set up
    calc = Calculator()
    #Test
    assert calc.add(2,2) == 4
    assert calc.add(2,2) != 5
