def solution(N, K, strarr):
  arr = list(strarr)
  ansSet = set()
  count = 0
  for i in range(len(arr)):
    if arr[i] == 'P':
      for j in range(max(i-K,0), i):
        if arr[j] == 'H' and j not in ansSet:
          ansSet.add(j)
          count += 1
          break
      else:
        for j in range(i+1, min(i+K+1, len(arr))):
          if arr[j] == 'H' and j not in ansSet:
            ansSet.add(j)
            count += 1
            break
  return count
N, K = map(int, input().split())
strarr = input()
print(solution(N, K, strarr))

