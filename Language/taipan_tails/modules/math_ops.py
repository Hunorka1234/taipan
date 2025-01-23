class TaipanMathOps:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
        
    @staticmethod
    def multiply(a, b):
        return a * b
        
    @staticmethod
    def division(a, b):
        return a / b if b != 0 else "Cannot divide by zero"

def init_module():
    return TaipanMathOps()
