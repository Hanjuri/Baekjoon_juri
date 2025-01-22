def solution(N, arr):
  shortKey = set()
  result = []
  for i, a in enumerate(arr):
    for j, e in enumerate(a):
      if e[0].upper() not in shortKey:
        shortKey.add(e[0].upper())
        a[j] = f"[{e[0]}]{e[1:]}"
        break
    else:
        for j, e in enumerate(a):
          for k in range(1, len(e)):
            if e[k].upper() not in shortKey:
              shortKey.add(e[k].upper())
              a[j] = f"{e[:k]}[{e[k]}]{e[k+1:]}"
              break
          else:
             continue
          break
    result.append(" ".join(a))
  for r in result:
    print(r)

N = int(input())
arr = [list(map(str, input().split()))for _ in range(N)]
solution(N, arr)