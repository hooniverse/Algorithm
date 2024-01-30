from itertools import combinations

n, m = map(int, input().split())

card = list(map(int, input().split()))

li = list(combinations(card, 3))

answer = []

for i in li:
    i_sum = sum(i)

    if i_sum <=m:
        answer.append(i_sum)

print(max(answer))