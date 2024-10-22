from collections import deque

def solution(N, M, K, arr):
    # 음식물이 있는 위치를 집합으로 저장
    food_set = set((a - 1, b - 1) for a, b in arr)

    def BFS(startpos):
        count = 0
        que = deque([startpos])
        pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while que:
            currentx, currenty = que.popleft()
            
            # 방문한 위치는 food_set에서 제거하여 중복 방문 방지
            if (currentx, currenty) not in food_set:
                continue
            food_set.remove((currentx, currenty))
            count += 1

            # 상하좌우 탐색
            for x, y in pos:
                thenx = currentx + x
                theny = currenty + y

                # 배열의 범위를 벗어나지 않고, 음식물이 있는 경우에만 큐에 추가
                if 0 <= thenx < N and 0 <= theny < M and (thenx, theny) in food_set:
                    que.append((thenx, theny))

        return count

    answer = 0
    # 모든 음식물 위치에서 BFS를 수행하여 가장 큰 연결된 음식물 덩어리 크기를 찾음
    for a, b in arr:
        if (a - 1, b - 1) in food_set:  # 음식물이 있는 위치에서만 BFS를 수행
            temp = BFS((a - 1, b - 1))
            answer = max(answer, temp)

    return answer

N, M, K = map(int, input().split())
arr = []
for _ in range(K):
  arr.append(list(map(int,input().split())))

print(solution(N,M,K,arr))