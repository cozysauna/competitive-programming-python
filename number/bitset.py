class Bitset:
    '''
        N:       bitの長さ
        add():   xビット目を1にする
        sub():   xビット目を0にする
        count(): 1となるビットの数を取得
        self[x]: xビット目を取得
        bit演算子 and, or, xor 対応
    '''
    def __init__(self, N):
        self.bit_size = 63
        self.bits_size = (N + self.bit_size - 1) // self.bit_size 
        self.bits = self.bits_size * [0]
        self.N = N

    def add(self, x):
        self.bits[x // self.bit_size] |= 1 << (x % self.bit_size)

    def sub(self, x):
        self.bits[x // self.bit_size] &= ~(1 << (x % self.bit_size))

    def count(self):
        cnt = 0
        for x in self.bits:
            c = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
            c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
            c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
            c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
            c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
            c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
            cnt += c

        return cnt

    def __and__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] & other.bits[i]

        return _bitset

    def __or__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] | other.bits[i]

        return _bitset

    def __xor__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] ^ other.bits[i]

        return _bitset

    def __getitem__(self, x):
        return self.bits[x // self.bit_size] >> (x % self.bit_size) & 1
