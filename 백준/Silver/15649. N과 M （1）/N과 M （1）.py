def recur():
    if len(result) == m:
        print(' '.join(map(str, result)))

    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur()
            result.pop()
            visited[i] = False

n, m = map(int, input().split())
result  = []
visited = [False] * (n + 1)

recur()