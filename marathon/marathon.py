from time import time; START = time()
from random import random, sample, choice, randrange

submit = False
output_file_name = 'out.txt'
result = ''


def solve():
    _output()

def _output():
    if submit:
        print(result)
    else:
        # print("SCORE ", score)
        outf = open(output_file_name, 'w')
        print(result, file = outf)


if __name__ == "__main__": solve()
