N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans.append((i,j))

def fill_gird(i,j,type,visited,n):
    if type == 1:
        dirx = [0, 0, 0, 0, 0]
        diry = [-2, -1, 0, 1, 2]
    elif type == 2:
        dirx = [-1, 0, 1, 0, 0]
        diry = [0, 0, 0, 1, -1]
    elif type == 3:
        dirx = [-1, 0, 1, -1, 1]
        diry = [1, 0, 1, -1, -1]
    for e in range(5):
        nexti = i + diry[e]
        nextj = j + dirx[e]
        if 0 <= nexti < n and 0 <= nextj < n:
            visited.add((nexti, nextj))

max_covered = 0


def sol(cnt, temp):
    global max_covered

    if cnt == len(ans):
        visited = set()
        for t, (x, y) in zip(temp, ans):
            fill_gird(x, y, t, visited, N)
        max_covered = max(max_covered, len(visited))
        return

    for i in range(1, 4):
        temp.append(i)
        sol(cnt + 1, temp)
        temp.pop()


sol(0, [])
print(max_covered)


