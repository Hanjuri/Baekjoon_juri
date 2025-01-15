def solution(N, arr):
  dp = [0] * N
  ls = []
  flag = 1
  for i in range(N):
    if i == 0:
      dp[i] = arr[i]
    now = arr[i]
    if now > dp[flag-1]:
      dp[flag] = now
      flag += 1
    else:
      index = 0
      for j in range(flag):
        if dp[j] >= now:
          dp[j] = now
          break 
  return flag




N = int(input())
arr = list(map(int, input().split()))    
print(solution(N, arr))