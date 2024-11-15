n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

total_count = 0 


for i in range(n):
    now = arr[i][0]  
    temp_count = 1
    for j in range(1, n):
        if arr[i][j] == now: 
            temp_count += 1
        now = arr[i][j]
    if temp_count >= m:
        total_count += 1



for j in range(n):
    now = arr[0][j]  
    temp_count = 1
    for i in range(1, n):
        if arr[i][j] != now:
            temp_count += 1
        now = arr[i][j]
    if temp_count >= m:
        total_count += 1

print(total_count)

