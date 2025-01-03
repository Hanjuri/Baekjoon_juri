n, m = map(int, input().split())

def calculate_gcd(n, m):
    if n < m : 
        n, m = m, n
    if n % m == 0 :
        print(m)
    else :
        return calculate_gcd(m, (n%m))

calculate_gcd(n, m)