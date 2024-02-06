def prime(x):
    if x == 1:
        return False

    for i in range(2,x):
        if x % i ==0:
            return False

    return True

n = int(input())
li = list(map(int, input().split(" ")))
count = 0
for i in li:
    if prime(i):
        count += 1

print(count)