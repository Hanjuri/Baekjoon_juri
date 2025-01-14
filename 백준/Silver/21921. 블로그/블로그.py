def solution(N, X, arr):
  initialSum = sum(arr[:X])
  maxSum = initialSum
  result = [initialSum]
  for i in range(X, N):
    initialSum += arr[i] - arr[i-X]
    if initialSum >= maxSum:
      maxSum = initialSum
      result.append(initialSum)
  if maxSum == 0:
    return ['SAD']
  count = result.count(maxSum)
  return [maxSum, count]


N, X = map(int, input().split())
arr = list(map(int, input().split()))
answer = solution(N, X, arr)
for a in answer:
  print(a)