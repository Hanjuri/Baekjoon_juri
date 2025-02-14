from collections import deque
def solution(N, M, arr):
  visited = [[False] * M for _ in range(N)]
  dirarr = [[1,0],[0,1],[-1,0],[0,-1]]

  def bfs(nowx, nowy, count):
    num = 0
    queue = deque()
    queue.append((nowx, nowy, count))
    visited[nowx][nowy] = True

    while queue:
      nowx, nowy, count = queue.popleft()
      num += 1
      for dx, dy in dirarr:
        thenx = nowx + dx
        theny = nowy + dy
        if 0 <= thenx < N and 0 <= theny < M and arr[thenx][theny] == 1 and not visited[thenx][theny]:
          queue.append((thenx, theny, count+1))
          visited[thenx][theny] = True
    return num
  
  answerLs = []
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1 and not visited[i][j]:
        answerLs.append(bfs(i,j,1))
  return len(answerLs), max(answerLs) if answerLs else 0

    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = solution(N,M,arr)
for a in answer:
  print(a)