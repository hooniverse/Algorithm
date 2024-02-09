n, k = map(int, input().split(" "))
coin = []

for _ in range(n):
    coin.append(int(input()))

count = 0

coin.sort(reverse=True)

for i in coin:
    a = k//i
    k -= a*i
    count += a

print(count)