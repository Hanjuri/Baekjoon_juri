from collections import deque

def solution(N, M, arr):
  map_key = {key: value for key, value in arr}
  visited = [False] * 101
  def bfs(now, count):
    que = deque()
    que.append((now, count))
    visited[now] = True
    while que:
      now, count = que.popleft()
      if now == 100:
        return count
      for i in range(1, 7):
        after = now + i
        if after in map_key.keys():
          after = map_key[after]
        if after >= 1 and after <= 100 and visited[after] != True:
          que.append((after, count + 1))
          visited[after] = True
    return -1
  return bfs(1,0)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N+M)]
print(solution(N,M,arr))