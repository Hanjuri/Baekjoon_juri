from collections import deque

def solution(M, N, K, arr):
  field = [[0 for _ in range(M+1)] for _ in range(N+1)]
  visited = [[False for _ in range(M+1)] for _ in range(N+1)]
  for a, b in arr:
    field[b][a] = 1

  move = [[0,1],[0,-1],[1,0],[-1,0]]
  def dfs(x,y):
    for mx, my in move:
      nx, ny = x+mx, y+my
      if 0 <= nx < N+1 and 0 <= ny < M+1 and not visited[nx][ny] and field[nx][ny] == 1:
        visited[nx][ny] = True
        dfs(nx,ny)
  def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
      x, y = queue.popleft()
      for mx, my in move:
        nx, ny = x+mx, y+my
        if 0 <= nx < N+1 and 0 <= ny < M+1 and not visited[nx][ny] and field[nx][ny] == 1:
          visited[nx][ny] = True
          queue.append((nx,ny))

  count = 0
  for a, b in arr:
    if not visited[b][a]:
      visited[b][a] = True
      bfs(b,a)
      count += 1
  return count



C = int(input())
for _ in range(C):
  M, N, K = map(int, input().split())
  arr = []
  for _ in range(K):
    arr.append(list(map(int, input().split())))
  print(solution(M, N, K, arr))

