def recur(index,dan,jjan,use):
    global answer
    if index == n:
        if use ==0:
            return
        result = abs(dan-jjan)
        answer = min(answer, result)
        return
    recur(index + 1, dan + ingre[index][1], jjan*ingre[index][0],use+1)
    recur(index + 1 ,dan, jjan, use)

n = int(input())

ingre = [list(map(int, input().split())) for _ in range(n)]
answer = 99999999999999

recur(0,0,1,0)

print(answer)