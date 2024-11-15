n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total_answer = []
for i in range(n):
    for j in range(m):
        best = set() #0 0
        if i + 2 < n:
            sum = 0
            for e in range(3):
                sum += arr[i+e][j]  
            best.add(sum)

        if j + 2 < m:
            sum = 0
            for e in range(3):
                sum += arr[i][j+e]
            best.add(sum)
        if i + 1 < n and j + 1 < m:
            best.add(arr[i][j] + arr[i+1][j] + arr[i][j+1])
            best.add(arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1])
            best.add(arr[i][j] + arr[i+1][j] + arr[i+1][j+1] )
            best.add(arr[i][j] +arr[i][j+1] + arr[i+1][j+1] )
        if best:
            total_answer.append(max(best))

print(max(total_answer))