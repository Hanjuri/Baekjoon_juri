def rotateBorder(arr, start, end):
    top, left = start
    bottom, right = end

    # 시작 위치의 값을 저장
    temp = arr[top][left]

    # 왼쪽 (위 → 아래)
    for i in range(top, bottom):
        arr[i][left] = arr[i + 1][left]

    # 하단 (왼쪽 → 오른쪽)
    for i in range(left, right):
        arr[bottom][i] = arr[bottom][i + 1]

    # 오른쪽 (아래 → 위)
    for i in range(bottom, top, -1):
        arr[i][right] = arr[i - 1][right]

    # 상단 (오른쪽 → 왼쪽)
    for i in range(right, left, -1):
        arr[top][i] = arr[top][i - 1]

    # temp 복구
    arr[top][left + 1] = temp

    return arr


def plusAround(arr, start, end):
    top, left = start
    bottom, right = end

    # 새로운 배열 생성
    new_arr = [row[:] for row in arr]

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            total = arr[i][j]
            count = 1

            # 인접 값 추가
            if i - 1 >= 0:  # 위쪽
                total += arr[i - 1][j]
                count += 1
            if i + 1 < len(arr):  # 아래쪽
                total += arr[i + 1][j]
                count += 1
            if j - 1 >= 0:  # 왼쪽
                total += arr[i][j - 1]
                count += 1
            if j + 1 < len(arr[0]):  # 오른쪽
                total += arr[i][j + 1]
                count += 1

            # 평균 값 계산 (버림)
            new_arr[i][j] = total // count

    return new_arr

N, M, Q = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))
wind = []
for _ in range(Q):
  wind.append(list(map(int, input().split())))

# 바람 처리
for w in wind:
    # 0-based 인덱스 변환
    start = (w[0] - 1, w[1] - 1)
    end = (w[2] - 1, w[3] - 1)
    rotateBorder(arr, start, end)
    arr = plusAround(arr, start, end)

# 결과 출력
for row in arr:
    print(' '.join(map(str,row)))