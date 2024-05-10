n = int(input())
li = set(map(int, input().split()))

m = int(input())
test = map(int, input().split())

for i in test:
    if i in li:
        print(1)

    else:
        print(0)