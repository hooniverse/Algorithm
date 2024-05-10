import sys
input = sys.stdin.readline

def zzz(start, end):
    while start <= end:
        count = 0
        mid = (start + end) // 2

        for i in arr:
            count += min(i, mid)

        if count <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

print(zzz(0, max(arr)))