def solution(n):
    answer = ''
    li = ["수","박"]
    
    for i in range(n):
        if i %2 == 0:
            answer += li[0]
        else:
            answer += li[1]
    return answer