n = int(input())
li = sorted(list(map(int, input().split())))
x = int(input())
count = 0

s, e = 0, n - 1

while s < e:

    a = li[s] + li[e]
    if a == x:
        count +=1
        s += 1
    elif a < x:
        s += 1
    else:
        e -= 1

print(count)