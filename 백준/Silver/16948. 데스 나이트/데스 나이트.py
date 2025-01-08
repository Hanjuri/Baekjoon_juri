from collections import deque
def bfs_solution(N, start, end):
  dirx = [-2,-2,0,0,2,2]
  diry = [-1,+1,-2,+2,-1,+1]
  que = deque([start])
  visited = [[False]* N for _ in range(N)]
  answer = 0

  visited[start[0]][start[1]] = True

  while que:
    for _ in range(len(que)):
      nowpos = que.popleft()
      nowx, nowy = nowpos

      if nowx == end[0] and nowy == end[1]:
        return answer
      
      for i in range(6):
        nextx = nowx + dirx[i]
        nexty = nowy + diry[i]

        if 0<=nextx<N and 0<=nexty<N and not visited[nextx][nexty]:
          visited[nextx][nexty] = True
          que.append((nextx, nexty))
    answer += 1
  return -1

N = int(input())
arr = list(map(int, input().split()))
start = arr[:2]
end = arr[2:]
print(bfs_solution(N,start, end))