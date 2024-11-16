n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0]* len(arr[0]) for _ in range(len(arr))]

for i in range(len(arr)):
  for j in range(n):
    new_i = (i+ (j+t)//n) % len(arr)
    new_j = (j+t) % n
    arr2[new_i][new_j] = arr[i][j]

for e in arr2:
  print(' '.join(map(str,e)))