N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def isPossible(arr):
    arr = sorted(arr)
    end_time = 0
    for a, b in arr:
        if end_time < a:
            end_time = b
        else:
            return False
    return True

maxCount = 0
def sol(selected):
    global maxCount
    if isPossible(selected):
        maxCount = max(maxCount, len(selected))
    for a in arr:
        if a not in selected:
            selected.append(a)
            sol(selected)
            selected.pop()
    return maxCount
print(sol([]))
