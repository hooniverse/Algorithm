def solution(n):
    answer = n
    for x in range(2,n):
        if n % x ==1:
            answer = min(answer,x)
    return answer