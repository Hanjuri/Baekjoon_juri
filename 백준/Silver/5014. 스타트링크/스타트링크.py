from collections import deque

def solution(F,S,G,U,D):

  move = [U, -D]
  visited = [False] * (F+1)
  def dfs(stair, count):
    que = deque()
    que.append((stair,count))
    visited[stair] = True
    while que:
      now, count = que.popleft()
      if now == G:
        return count
      for m in move:
        after = now + m
        if after >= 1 and after <= F and visited[after] != True:
          visited[after] = True
          que.append((after, count + 1))
    return "use the stairs"
  return dfs(S,0)

F, S, G, U, D = map(int, input().split())
print(solution(F,S,G,U,D))