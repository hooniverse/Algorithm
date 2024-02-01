def solution(n):
    answer = 1
    
    for i in range(1,n):
        count = 0
        for j in range(i,n):
            count +=j
            if count == n:
                answer +=1
                break
            elif count > n:
                break
    return answer