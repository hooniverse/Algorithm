def solution(arr):
    answer = []
    answer.append(arr[0])
    del arr[0]
    
    for i in arr:
        answer.append(i)
        if answer[-2] == i:
            del answer[-1]
    return answer