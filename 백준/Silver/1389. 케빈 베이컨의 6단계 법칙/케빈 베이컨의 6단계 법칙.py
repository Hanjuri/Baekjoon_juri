### 메모리 크기 줄이기
### floydWashall 알고리즘

def solution(N, M , arr):
  dist = [[float('inf')] * (N+1) for _ in range(N+1)]

  for i in range(1, N + 1):
    dist[i][i] = 0
  for a, b in arr:
    dist[a][b] = 1
    dist[b][a] = 1
  
  for k in range(1,N+1):
    for i in range(1,N+1):
      for j in range(1,N+1):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  answerls = [0] * (N+1)
  for i in range(1, N+1):
    for j in range(1, N+1):
      answer = dist[i][j]
      if answer != float('inf'):
        answerls[i] += answer
  return answerls.index(min(answerls[1:]))
N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
print(solution(N,M,arr))