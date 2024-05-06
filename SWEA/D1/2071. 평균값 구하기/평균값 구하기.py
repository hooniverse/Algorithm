t = int(input())

for case in range(1, t+1):
        li = map(int, input().split())
        result = 0
        for i in li:
            result += i
        
        print(f"#{case} {round(result/10)}")