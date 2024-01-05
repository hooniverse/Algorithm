def solution(n):
    li = list(map(int, str(n)))

    li.sort(reverse=True)
    result = ""
    for i in li:
        result += str(i)
    
    return int(result)