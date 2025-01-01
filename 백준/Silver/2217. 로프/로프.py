def solution(N, arr):
  arr.sort(reverse = True)
  maxWeight = 0
  for i in range(N):
    weight = arr[i] * (i+1)
    maxWeight = max(maxWeight, weight)
  return maxWeight

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))
print(solution(N, arr))