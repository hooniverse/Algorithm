from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split(" "))) for _ in range(n)]
comb = [combinations(arr, i) for i in range(1, n+1)]

result = sys.maxsize


for com in comb:
    for a in com:
        sour, bitter = 1, 0
        for s, b in a:
            sour *= s
            bitter += b
        result = min(result, abs(sour-bitter))
print(result)