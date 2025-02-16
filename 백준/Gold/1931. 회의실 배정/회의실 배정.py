def solution(N, arr):
  arr.sort(key=lambda x :( x[1], x[0]))
  count = 0
  last_end = 0

  for start, end in arr:
    if start >= last_end:
      count += 1
      last_end = end
  return count
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))