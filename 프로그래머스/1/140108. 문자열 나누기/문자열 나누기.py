def solution(s):
    answer = 0
    
    count1, count2 = 0, 0
    for i in s:
        if count1 == count2:
            answer +=1
            a = i
        if a == i:
            count1 +=1
        else:
            count2 +=1
    return answer