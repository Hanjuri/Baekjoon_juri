def howmany_possible(arr, dis, C):  # C 추가
    start = arr[0]
    count = 1
    for i in range(len(arr)):
        if arr[i] >= start + dis:
            count += 1
            start = arr[i]
    return count >= C

def solution(arr, N, C):
    start = 1  # 최소 거리
    end = arr[-1] - arr[0]  # 최대 거리
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if howmany_possible(arr, mid, C):  # C 전달
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
print(solution(arr, N, C))