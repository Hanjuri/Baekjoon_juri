def solution(N,arr,total):

  def sumCost (cost):
    totalCost = 0
    for a in arr:
      if a < cost:
        totalCost += a
      else:
        totalCost += cost
    return totalCost
    
  arr.sort()
  left, right = 0, arr[-1]
  while left <= right:
    mid = (left + right) // 2
    if sumCost(mid) > total:
      right = mid - 1
    else:
      left = mid + 1
  return right

N = int(input())
arr = list(map(int,input().split()))
total = int(input())
print(solution(N, arr, total))