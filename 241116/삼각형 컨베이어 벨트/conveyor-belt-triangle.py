n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    new_i = (i+ (j+t)//n) % n
    new_j = (j+t) % n
    arr2[new_i][new_j] = arr[i][j]

for e in arr2:
  print(' '.join(map(str,e)))