def solution(N,M,arr,route):
  parent  = [0] * (N+1)
  for i in range(1,N+1):
    parent[i] = i

  def find(a):
    if a == parent[a]:
      return a
    else:
      parent[a] = find(parent[a])
      return parent[a]

  def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
      parent[b] = a

  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == 1:
        union(i+1,j+1)
  root = find(route[0])
  for r in route[1:]:
    if find(r) != root:
      return 'NO'
  return 'YES'



N = int(input())
M = int(input())
arr =[]
for _ in range(N):
  arr.append(list(map(int, input().split())))
route = list(map(int, input().split()))
print(solution(N,M,arr,route))