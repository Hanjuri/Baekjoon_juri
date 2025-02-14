from collections import deque
def solution(N, M, arr):
  dirarr = [[1,0],[-1,0],[0,1],[0,-1]]

  def bfs(nowx, nowy, count):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((nowx, nowy, count))
    while queue:
      nowx, nowy, count = queue.popleft()
      for dx, dy in dirarr:
        thenx = nowx + dx
        theny = nowy + dy
        if 0 <= thenx < N and 0<= theny < M and arr[thenx][theny] == 1 and visited[thenx][theny] == 0:
          queue.append((thenx, theny, count+1))
          visited[thenx][theny] = count+1
    return visited

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 2:
        result = bfs(i,j,0)
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1 and result[i][j] == 0:
        result[i][j] = -1
  for row in result:
    print(*row)
  



N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
solution(N,M,arr)
