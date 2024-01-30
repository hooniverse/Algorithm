n = int(input())

a = 666

count = 0
while True:

    if "666" in str(a):
        count +=1
    
    if count == n:
        break

    a += 1

print(a)
    