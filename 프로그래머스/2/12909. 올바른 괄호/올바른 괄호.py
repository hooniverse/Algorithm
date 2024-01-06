def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        
        elif i == ")":
            if len(stack) >=1 and stack.pop() == "(":
                continue
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False