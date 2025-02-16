import heapq

def solution(N, arr):
  heapq.heapify(arr)
  total = 0

  while len(arr) >= 2:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    total += first+second
    heapq.heappush(arr, first+second)
  return total


N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))
print(solution(N, arr))