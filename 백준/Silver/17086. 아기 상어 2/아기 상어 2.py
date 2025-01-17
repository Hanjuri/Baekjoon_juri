from collections import deque
def solution(arr):
  row, col = len(arr), len(arr[0])
  move = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
  
  def bfs(x,y,count):
    visited = [[False] * col for _ in range(row)]
    queue = deque()
    queue.append((x,y,count))
    visited[x][y] = True
    while queue:
      x, y, count = queue.popleft()
      if arr[x][y] == 1:
        return count
      for dx, dy in move:
        nx, ny = x+dx, y+dy
        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
          queue.append((nx,ny,count+1))
          visited[nx][ny] = True
    return -1
  
  max = 0
  for i in range(row):
    for j in range(col):
      if arr[i][j] == 0:
        result = bfs(i,j,0)
        if result > max:
          max = result
  return max



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(arr))