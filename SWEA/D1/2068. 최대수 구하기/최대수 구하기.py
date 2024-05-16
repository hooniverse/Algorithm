t = int(input())

for i in range(1,t+1):
    li = list(map(int, input().split()))
    li.sort()
    print(f"#{i} {li[-1]}")