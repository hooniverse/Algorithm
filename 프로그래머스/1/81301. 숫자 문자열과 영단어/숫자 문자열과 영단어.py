def solution(s):
    answer = ""
    num = ""
    li = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            num += i
            if num in li:
                answer +=str(li.index(num))
                num =""
    
    return int(answer)