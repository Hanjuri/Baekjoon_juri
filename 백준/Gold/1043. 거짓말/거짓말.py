def solution(N, M, T, trueP, partyP):
  
  def find(a):
    if a == parent[a]:
      return a
    else:
      parent[a] = find(parent[a])
      return parent[a]
  def union(a, b):
    parenta = find(a)
    parentb = find(b)
    if parenta != parentb:
      parent[parentb] = parenta 
  
  def checkSame(a,b):
    parenta = find(a)
    parentb = find(b)
    if parenta == parentb:
      return True
    else:
      return False
   
  parent = [ i for i in range(N+1)]
  count = 0

    
  
  for party in partyP:
    firstPeople = party[1]
    for person in party[2:]:
      union(firstPeople, person)

  for party in partyP:
    isPossible = True
    firstPeople = party[1]
    for truePerson in trueP:
      if find(truePerson) == find(firstPeople):
        isPossible = False
        break
    if isPossible:
      count += 1

  return count



N, M = map(int, input().split())
arr = list(map(int, input().split()))
T = arr[0]
trueP = arr[1:]
partyP = list(list(map(int, input().split())) for _ in range(M))
print(solution(N, M, T, trueP, partyP))