def solution(N, arr):
  
  dist = [[float('inf')] * (N) for _ in range(N)]
  for i in range(N):
    dist[i][i] = 0
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 'Y':
        dist[i][j] = 1
  for k in range(N):
    for i in range(N):
      for j in range(N):
         dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  answer = []
  for i in range(N):
    friend2count = sum(1 for j in range(N) if i!=j and dist[i][j] <= 2)
    answer.append(friend2count)
  return max(answer)

N = int(input())
arr = []
for _ in range(N):
  arr.append(list(input().strip()))
print(solution(N, arr))
