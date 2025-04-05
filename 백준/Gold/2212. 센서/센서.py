def solution(N, K, arr):
  arr.sort()
  dis = []
  for i in range(0, len(arr)-1):
    dis.append(arr[i+1] - arr[i])
  dis.sort(reverse = True)
  dis = dis[K-1:]
  return sum(dis)

N = int(input())
K = int(input())
arr = list(map(int, input().split())) 
print(solution(N,K,arr))        

