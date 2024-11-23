N, M, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
blow = [list(input().split()) for _ in range(Q)]

def pushDir(row, dir):
    # 행을 좌/우로 회전
    new_row = [0] * M
    for bIndex in range(M):
        if dir:  # 왼쪽으로 이동
            then = (bIndex + 1) % M
        else:    # 오른쪽으로 이동
            then = (bIndex - 1) % M
        new_row[then] = arr[row][bIndex]
    arr[row] = new_row  # 업데이트

def isSameColumn(first, second):
    # 두 행의 동일 열 값 확인
    for col in range(M):
        if arr[first][col] == arr[second][col]:
            return True
    return False

for row, dir in blow:
    firstRow = int(row) - 1  # 1-based index를 0-based index로 변환
    firstDir = True if dir == "L" else False

    # 첫 번째 행 처리
    pushDir(firstRow, firstDir)

    # 아래로 탐색
    nowRow = firstRow
    nowDir = firstDir
    while nowRow + 1 < N:
        nextRow = nowRow + 1
        thenDir = not nowDir
        if isSameColumn(nowRow, nextRow):
            pushDir(nextRow, thenDir)
            nowRow = nextRow
            nowDir = thenDir
        else:
            break

    # 위로 탐색
    nowDir = firstDir
    nowRow = firstRow
    while nowRow - 1 >= 0:
        prevRow = nowRow - 1
        thenDir = not nowDir
        if isSameColumn(nowRow, prevRow):
            pushDir(prevRow, thenDir)
            nowRow = prevRow
            nowDir = thenDir
        else:
            break

# 최종 출력
for row in arr:
    print(" ".join(map(str, row)))