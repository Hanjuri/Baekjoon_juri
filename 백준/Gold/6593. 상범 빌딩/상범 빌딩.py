from collections import deque

def solution(L,R,C,arr):

  move = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[-1,0,0],[1,0,0]]
  visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

  def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z,0))
    visited[x][y][z] = True
    while queue:
      x, y, z, count = queue.popleft()
      if arr[x][y][z] == 'E':
        return f'Escaped in {count} minute(s).'
      for mx, my, mz in move:
        nx, ny, nz = x+mx, y+my, z+mz
        if 0 <= nx < L and 0 <= ny < R and 0<= nz < C and not visited[nx][ny][nz] and arr[nx][ny][nz] in ('.','E'):
          queue.append((nx,ny,nz,count +1))
          visited[nx][ny][nz] = True
    return 'Trapped!'
  answer = 0
  for i in range(L):
    for j in range(R):
      for k in range(C):
        if arr[i][j][k] == 'S':
          answer = bfs(i,j,k)
          return answer
  return 'Trapped!'

realAnswer = []
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    arr = []
    for _ in range(L):
        insidearr = []
        for _ in range(R):
            row = input().strip()
            insidearr.append(list(row))
        arr.append(insidearr)
        input()  # 층 사이의 빈 줄 처리
    print(solution(L, R, C, arr))