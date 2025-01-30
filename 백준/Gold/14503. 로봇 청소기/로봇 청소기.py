from collections import deque

def solution(N, M, startx, starty, nowDir, arr):
    # 방향: 북(0), 동(1), 남(2), 서(3)
    dirarr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False] * M for _ in range(N)]  # 방문 체크 배열

    def anyPlaceclean(nowx, nowy):
        for i in range(4):
            nx, ny = nowx + dirarr[i][0], nowy + dirarr[i][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and not visited[nx][ny]:
                return True
        return False

    def bfs(startx, starty, dir):
        que = deque()
        que.append((startx, starty, dir))
        visited[startx][starty] = True  # 첫 위치 청소
        count = 1  # 첫 칸은 이미 청소했으므로 1부터 시작

        while que:
            nowx, nowy, dir = que.popleft()

            if anyPlaceclean(nowx, nowy):  # 주변에 청소할 공간이 있는 경우
                for _ in range(4):  # 최대 4번 회전 가능
                    dir = (dir - 1) % 4  # 왼쪽으로 회전
                    afterx, aftery = nowx + dirarr[dir][0], nowy + dirarr[dir][1]

                    if 0 <= afterx < N and 0 <= aftery < M and arr[afterx][aftery] == 0 and not visited[afterx][aftery]:
                        que.append((afterx, aftery, dir))
                        visited[afterx][aftery] = True
                        count += 1
                        break  # 이동했으면 회전 중단

            else:  # 주변이 모두 청소되었거나 벽인 경우 후진
                backdir = (dir + 2) % 4
                backx, backy = nowx + dirarr[backdir][0], nowy + dirarr[backdir][1]

                if 0 <= backx < N and 0 <= backy < M and arr[backx][backy] == 0:  # 벽이 아니라면 후진 가능
                    que.append((backx, backy, dir))
                else:  # 후진도 불가능하면 종료
                    return count

        return count

    return bfs(startx, starty, nowDir)


N, M = map(int, input().split())
startx, starty, nowDir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N,M,startx, starty, nowDir,arr))