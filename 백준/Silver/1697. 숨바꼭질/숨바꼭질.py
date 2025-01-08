from collections import deque

def solution(N, K):
  max_limit = max(N, K) * 2
  arr = [-1 for _ in range(max_limit +1)]

  def bfs(start):
    queue = deque()
    queue.append(start)
    arr[start] = 0

    while queue:
      nowIndex = queue.popleft()
      if nowIndex == K:
        return arr[nowIndex]
      for nextIndex in [nowIndex-1, nowIndex+1, nowIndex*2]:
        if 0<= nextIndex <= max_limit and arr[nextIndex] == -1:
          arr[nextIndex] = arr[nowIndex] + 1
          queue.append(nextIndex)
  return bfs(N)
  
N, K = map(int, input().split())
print(solution(N,K))