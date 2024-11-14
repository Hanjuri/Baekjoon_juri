def solution(n):
    dp = [0] * (n+1)
    dp[1] = 2
    if n > 1:
        for i in range(2, n+1):
            dp[i] = dp[i-1] * 2 + dp[i-1]+1
    return dp[n] % 1000000007


n = int(input())
print(solution(n))