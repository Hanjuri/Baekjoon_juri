n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
max_sum = 0
for i in range(n-2):
    for j in range(n-2):
            sum = 0
            for e in range(3):
              for f in range(3):
                if arr[i+e][j+f] == 1:
                    sum += 1
            if max_sum < sum:
                max_sum = sum

print(max_sum)
                