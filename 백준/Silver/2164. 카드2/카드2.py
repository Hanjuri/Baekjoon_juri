from collections import deque

def solution(N):
  queue = deque([i for i in range(1, N+1)])
  while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
  return queue[0]

print(solution(int(input())))