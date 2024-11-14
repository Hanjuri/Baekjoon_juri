def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return dp(n-1) + dp(n-2)
    return dp(n)
n = int(input())
print(dp(n))