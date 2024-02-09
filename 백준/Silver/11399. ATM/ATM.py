n = int(input())

li = list(map(int,input().split(" ")))

li.sort(reverse=True)

result = 0

for i in range(n):
    result += li[i]*(i+1)

print(result)