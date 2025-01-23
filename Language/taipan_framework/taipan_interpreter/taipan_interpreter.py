from taipan_spine.taipanspine import spine

class TaipanInterpreter:
    def __init__(self):
        self.spine = spine
        print("Taipan Interpreter initialized!")
    
    def execute(self, filepath):
        try:
            with open(filepath, 'r') as file:
                content = file.read()
            
            # Execute the code and capture the output
            exec(content, globals(), locals())

        except Exception as e:
            print(f"Taipan Error: {str(e)}")
