import random as py_random

class TaipanRandom:
    @staticmethod
    def randint(min_val, max_val):
        return py_random.randint(min_val, max_val)
    
    @staticmethod
    def random_float():
        return py_random.random()
    
    @staticmethod
    def choice(sequence):
        return py_random.choice(sequence)
    
    @staticmethod
    def shuffle(sequence):
        temp_seq = list(sequence)
        py_random.shuffle(temp_seq)
        return temp_seq
    
    @staticmethod
    def random_range(start, stop, step=1):
        return py_random.randrange(start, stop, step)
    
    @staticmethod
    def random_sample(sequence, k):
        return py_random.sample(sequence, k)

def init_module():
    return TaipanRandom()
