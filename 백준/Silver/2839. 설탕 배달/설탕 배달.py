n = int(input())

count = 0

while True:
    if n % 5 ==0:
        count += 1
        n -= 5
    else:
        count += 1
        n -= 3
    
    if n <= 0:
        break

if n != 0:
    print(-1)

else:
    print(count)