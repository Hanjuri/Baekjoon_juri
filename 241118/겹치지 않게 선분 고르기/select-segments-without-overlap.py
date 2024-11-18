N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def isPossible(start, end):
    end_time = 0
    if start > end_time:
        end_time = end
    return True

maxCount = 0
def sol(start,selected):
    global maxCount
    if len(selected) > 0:
        start_t, end_t= sorted(selected)[-1]
        if isPossible(start_t, end_t):
            maxCount = max(maxCount, len(selected))
    for i in range(start, N):
        selected.append(arr[i])
        sol(start+1, selected)
        selected.pop()
    return maxCount
print(sol(0,[]))

