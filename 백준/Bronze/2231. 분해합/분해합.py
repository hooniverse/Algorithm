n = int(input())

a = 1

while True:
    if a == n:
        print(0)
        break
    
    li = list(map(int, str(a)))
    a = int(a)
    
    if sum(li) + a == n:
        print(a)
        break

    a +=1