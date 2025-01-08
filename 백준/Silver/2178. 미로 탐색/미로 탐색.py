from collections import deque

N,M = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input())))
def solution(N, M, arr):
  visited = [[False for _ in range(M)] for _ in range(N)]
  move = [[0,1],[0,-1],[1,0],[-1,0]]
  def bfs(x,y):
    queue = deque()  
    queue.append((x,y,1))
    visited[x][y] = True
    while queue:
      x, y, depth = queue.popleft()
      if x == N-1 and y == M-1:
        return depth
      for mx, my in move:
        nx, ny = x+mx, y+my
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
          queue.append((nx,ny, depth+1))
          visited[nx][ny] = True
    return -1
  print(bfs(0,0))
solution(N,M,arr)