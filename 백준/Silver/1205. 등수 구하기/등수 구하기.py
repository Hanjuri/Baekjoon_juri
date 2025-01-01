N, score, P = map(int, input().split())
arr = list(map(int, input().split())) if N > 0 else []
minScore = min(arr) if arr else float('-inf')

if len(arr) >= P and score <= minScore:
  print(-1)
else:
  arr.append(score)
  sortedarr = sorted(arr, reverse = True)
  answerIndex = sortedarr.index(score)+1
  print(answerIndex)


