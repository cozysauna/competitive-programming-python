'''
    参考: 
        https://github.com/firewood/topcoder/blob/master/algorithm/two_opt.cpp
        https://qiita.com/hotpepsi/items/424f9491e7baaa63b6ce
'''

from random import randrange

def swap(route, a, b, c, d):
    N = len(route)
    x = d
    y = b
    if y - x > a + N - c:
        x = c
        y = a + N

    while x < y:
        route[x % N], route[y % N] = route[y % N], route[x % N]
        x += 1
        y -= 1

def main():
    # INPUT
    N = int(input())
    cors = [list(map(float, input().split())) for _ in range(N)]

    # PRE-PROCESSING
    dist = [[None] * N for _ in range(N)]
    for i in range(N):
        y1, x1 = cors[i]
        for j in range(N):
            y2, x2 = cors[j]
            dist[i][j] = ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** .5

    # TSP
    route = list(range(N))
    LOOP_CNT = 10 ** 7

    for _ in range(LOOP_CNT):
        a = randrange(0, N)
        b = randrange(0, N)
        if a == b: continue
        if a > b: a, b = b, a
        d = (a + 1) % N
        c = (b + 1) % N
        if dist[route[a]][route[b]] + dist[route[c]][route[d]] < dist[route[a]][route[d]] + dist[route[b]][route[c]]:
            '''
                a   b         a - b
                  x      -> 
                c   d         c - d
            '''
            swap(route, a, b, c, d)

    # OUTPUT
    output_file_name = "out.txt"
    with open(output_file_name, 'w') as f:
        print(*route, file = f)

if __name__ == "__main__":
    main()
