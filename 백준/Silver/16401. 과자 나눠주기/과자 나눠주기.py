def solution(M, N, arr):

  def isPossible(mid):
    count = M
    for a in arr:
      count -= a // mid
    if count > 0:
      return False
    else:
      return True

  arr.sort()
  start, end = 1, arr[-1]
  result = 0
  while start <= end:
    mid = (start + end) // 2
    if isPossible(mid):
      result = mid
      start = mid + 1
    else:
      end = mid - 1
  return result

      

M, N = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(M,N,arr))
