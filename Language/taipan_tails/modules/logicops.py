class TaipanLogicOps:
    @staticmethod
    def if_statement(condition, true_block, false_block=None):
        if condition:
            return true_block()
        elif false_block:
            return false_block()
    
    @staticmethod
    def while_loop(condition, block):
        while condition():
            block()
    
    @staticmethod
    def for_loop(iterable, block):
        for item in iterable:
            block(item)
    
    @staticmethod
    def elif_statement(condition, true_block, next_elif=None):
        if condition:
            return true_block()
        elif next_elif:
            return next_elif()

def init_module():
    return TaipanLogicOps()
