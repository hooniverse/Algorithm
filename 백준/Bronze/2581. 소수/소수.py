def prime(x):
    if x == 1:
        return False

    for i in range(2,x):
        if x % i ==0:
            return False

    return True

m = int(input())
n = int(input())

result = []

for i in range(m,n+1):
    if prime(i):
        result.append(i)

if len(result)>=1:
    print(sum(result))
    print(min(result))

else:
    print(-1)