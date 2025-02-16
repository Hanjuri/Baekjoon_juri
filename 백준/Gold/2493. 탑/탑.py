def solution(N, arr):
  result = [0] * (N)
  stack = []

  for i in range(N-1, -1, -1):
    now = arr[i]
    while stack and now > arr[stack[-1]]:
      index = stack.pop()
      result[index] = i+1
    stack.append(i)
  return result
N = int(input())
arr = list(map(int, input().split()))
print(*solution(N, arr))