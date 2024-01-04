def solution(s):
    li = list(map(int, s.split(" ")))
    max1 = max(li)
    min1 = min(li)
    answer = str(min1)+ " " + str(max1)
    return answer