class TaipanPrint:
    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
    
    @staticmethod
    def output(value):
        print(value)

def init_module():
    return TaipanPrint()
