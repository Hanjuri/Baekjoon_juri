from collections import deque
def solution(N, arr):

  adjList = [[] for _ in range(N)]
  answer = [[0 for _ in range(N)] for _ in range(N)] 

  for i in range(N):
    for j in range(N):
      if arr[i][j] == 1:
        adjList[i].append(j)

  def findway(start):
    visited = [False for _ in range(N)]
    que = deque()
    que.append(start)
    while que:
      current = que.popleft()
      for temp in adjList[current]:
        if not visited[temp]:
          visited[temp] = True
          answer[start][temp] = 1
          que.append(temp)
        if temp == start:
          answer[start][start] = 1
        
  for i in range(N):
    findway(i)

  for row in answer:
    print(' '.join(map(str, row)))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
solution(N, arr)