from collections import deque

def solution(N, answerTwo, M, arr):
  graph = [[] for _ in range(N+1)]
  visited = [False for _ in range(N+1)]
  for a, b in arr:
    graph[a].append(b)
    graph[b].append(a)
  def bfs(start, end, depth):
    queue = deque()
    queue.append((start, depth))
    visited[start] = True
    while queue:
      now, depth = queue.popleft()
      if now == end:
        return depth
      for next in graph[now]:
        if not visited[next]:
          queue.append((next, depth+1))
          visited[next] = True
    return -1



  print(bfs(answerTwo[0],answerTwo[1],0))
  return


N = int(input())
twoAnswer = list(map(int, input().split()))
M = int(input())
arr = []
for _ in range(M):
  arr.append(list(map(int, input().split())))
solution(N, twoAnswer, M, arr)
