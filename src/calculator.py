
class Calculator:
    def add(self,a:int, b:int) -> int:
        return a+b

    def subtract(self,a:int, b:int) -> int:
        return a-b

    def multiplicate(self,a:int, b:int) -> int:
        if b == 0:
            raise ZeroDivisionError('Division by zero is never allowed')
        return a*b

    def divide(self,a:int, b:int) -> float:
        return a/b
    

