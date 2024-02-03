x = list(input())
y = []
for i in range(len(x)-1,-1,-1):
    y.append(x[i])

result = 1
for i in range(len(x)):
    if x[i] != y[i]:
        result = 0

print(result)

