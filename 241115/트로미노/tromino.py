n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

total_answer = []
for i in range(n):
    for j in range(m):
        best = [] #0 0
        if i + 2 < n:
            sum = 0
            for e in range(3):
                sum += arr[i+e][j]  
            best.append(sum)

        if j + 2 < m:
            sum = 0
            for e in range(3):
                sum += arr[i][j+e]
            best.append(sum)
        if 0 <= j-1 & 0 <= i-1:
            sum = 0
            sum += arr[i][j]
            sum += arr[i-1][j]
            sum += arr[i][j-1]
            best.append(sum)
        if j+1 < m & i+1 < n:
            sum = 0
            sum += arr[i][j]
            sum += arr[i+1][j]
            sum += arr[i][j+1]
            best.append(sum)
        total_answer.append(max(best))

print(max(total_answer))
