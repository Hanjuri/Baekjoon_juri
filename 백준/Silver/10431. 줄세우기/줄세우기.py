def solution(index, arr):
  nowarr = []
  sumAll = 0
  for a in arr:
    if not nowarr or all(s <= a for s in nowarr):
      nowarr.append(a)
    else:
      larger_index = next(i for i, s in enumerate(nowarr) if s > a)
      sumAll += len(nowarr) - larger_index
      nowarr.insert(larger_index, a)
  return index, sumAll
      

N = int(input())
allArr = []
for _ in range(N):
  arr = list(map(int, input().split()))
  allArr.append(arr)


for a in allArr:
  answer = solution(a[0], a[1:])
  print(answer[0], answer[1])


