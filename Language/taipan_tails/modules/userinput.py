class TaipanUserInput:
    @staticmethod
    def get_text(prompt):
        return input(prompt)
    
    @staticmethod
    def get_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer!")
    
    @staticmethod
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number!")

def init_module():
    return TaipanUserInput()
