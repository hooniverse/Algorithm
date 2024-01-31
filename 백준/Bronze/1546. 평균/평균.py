n = int(input())

score = list(map(int, input().split()))

result = sum(score)/max(score)
result *= 100
result /= len(score)


print(result)