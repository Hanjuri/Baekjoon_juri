import heapq

N = int(input())
min_heap = []
for _ in range(N):
  row = list(map(int, input().split()))
  for each in row:
    heapq.heappush(min_heap, each)
    if len(min_heap)> N:
      heapq.heappop(min_heap)
print(heapq.heappop(min_heap))