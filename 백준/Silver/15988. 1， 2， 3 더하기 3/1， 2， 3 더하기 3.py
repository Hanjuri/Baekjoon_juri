def solution(maxN):
  MOD = 1000000009
  if maxN == 1:
    return [1]
  elif maxN == 2:
    return [1,2]
  elif maxN == 3:
    return [1,2,4]
  dp = [0] * 3
  dp[0], dp[1], dp[2] = 1, 2, 4
  result = [1,2,4]
  for i in range(4, maxN+1):
    now = (dp[0] + dp[1] + dp[2]) % MOD
    dp[0], dp[1], dp[2] = dp[1], dp[2], now
    result.append(now)
  return result

T = int(input())
paramls = [int(input()) for _ in range(T)]
maxN = max(paramls)
answerDp = solution(maxN)
for p in paramls:
  print(answerDp[p-1])