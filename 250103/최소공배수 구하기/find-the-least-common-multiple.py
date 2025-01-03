n, m = map(int, input().split())

def cal_gcd(n, m):
    if n < m : 
        n, m = m, n
    if n % m == 0 : 
        return m
    else : 
        return cal_gcd(m, cal_gcd(m, n%m))

def cal_lcm(n, m):
    return (n * m) / cal_gcd(n,m)

result = cal_lcm(n,m)
print(int(result))