n, s = map(int, input().split())

num = list(map(int, input().split()))

result = 100001
count = 0
left, right = 0, 0

while True:
    if count >= s:
        result = min(result, right-left)
        count -= num[left]
        left +=1
    elif right == n:
        break

    else:
        count += num[right]
        right +=1

if result == 100001:
    print(0)
else:
    print(result)