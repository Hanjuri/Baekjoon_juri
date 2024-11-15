n = int(input())

d = [0] * (n+1)
d[0], d[1] = 1, 1

for i in range(2, n+1):
    summ = 0
    for j in range(n+1):
        summ += d[j] * d[i-j-1]
    d[i]  = summ
print(d[n])