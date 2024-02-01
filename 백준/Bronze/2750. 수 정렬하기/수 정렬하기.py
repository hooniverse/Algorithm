n = int(input())

result = []

for _ in range(n):
    a = int(input())
    
    result.append(a)

result.sort()
for i in result:
    print(i)
