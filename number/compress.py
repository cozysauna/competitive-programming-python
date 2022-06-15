class Compress:
    def __init__(self, A, indexed = 0):
        self.compress = {}
        self.original = {}
        for i, e in enumerate(sorted(set(A))):
            self.compress[e] = i + indexed
            self.original[i + indexed] = e 

    def get_compress(self, A): 
        if type(A) == list: return [self.compress[e] for e in A]
        if type(A) == int: return self.compress[A]

    def get_original(self, A): 
        if type(A) == list: return [self.original[e] for e in A]
        if type(A) == int: return self.original[A]
