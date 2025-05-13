n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 트로미노의 가능한 모든 형태 (회전 및 대칭 포함)
tromino_shapes = [
    [(0, 0), (1, 0), (1, 1)],  # ㄴ자
    [(0, 0), (0, 1), (1, 1)],  # ㄱ자
    [(0, 1), (1, 0), (1, 1)],  # ㄴ자 반전
    [(0, 0), (0, 1), (1, 0)],  # ㄱ자 반전
    [(0, 0), (0, 1), (0, 2)],  # 가로 일자
    [(0, 0), (1, 0), (2, 0)]   # 세로 일자
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

max_sum = 0

for i in range(n):
    for j in range(m):
        for shape in tromino_shapes:
            current_sum = 0
            valid = True
            for dx, dy in shape:
                nx, ny = i + dx, j + dy
                if not in_range(nx, ny):
                    valid = False
                    break
                current_sum += board[nx][ny]
            if valid:
                max_sum = max(max_sum, current_sum)

print(max_sum)