debug = True
from time import time; START = time()
from random import random, sample, choice, randrange
from collections import deque, defaultdict
from random import random, choice, choices
from sys import stdin

output_file_name = 'out.txt'
log_file_name = '.log'

readline = stdin.readline
''' Input '''
def I(): return int(readline())
def ST(): return readline()[:-1]
def LI(): return list(map(int, readline().split()))
def LII(): return list(map(lambda x: int(x) - 1, readline().split()))
def LF(x, func): return [func() for _ in [0] * x]
def SPI(): return map(int, readline().split())
def SPII(): return map(lambda x: int(x) - 1, readline().split())
def FIE(x): return [readline()[:-1] for _ in [0] * x]

def pprint(_A):
    print()
    for _E in _A:
        print(*_E)

################################ solve ################################

def solve():

    _output()

def _output(score, result):
    if debug:
        logf = open(log_file_name, 'a')
        print("SCORE", score)
        print(score, file = logf)
        outf = open(output_file_name, 'w')
        print(result, file = outf)
    else:
        print(result)

if __name__ == "__main__": 
    solve()