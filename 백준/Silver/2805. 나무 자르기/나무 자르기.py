def solution(N, answerMeter, arr):
    # 나무 높이를 정렬하지 않고 그대로 사용
    left, right = 0, max(arr)  # left는 0, right는 가장 높은 나무의 높이
    result = 0  # 최적의 절단기 높이
    
    while left <= right:
        mid = (left + right) // 2
        sumtree = 0
        
        # 중간값(mid)으로 나무를 자르고 자른 나무의 총합 계산
        for tree in arr:
            if tree > mid:
                sumtree += (tree - mid)

        # 자른 나무가 M미터 이상이면, 더 높이 자를 수 있는지 확인
        if sumtree >= answerMeter:
            result = mid  # 일단 mid 값이 유효하므로 저장
            left = mid + 1  # 더 높은 절단기 설정 가능성을 탐색
        # 자른 나무가 M미터보다 적으면, 더 낮게 잘라야 함
        else:
            right = mid - 1  # 절단기 높이를 낮춤
    
    return result

# 입력 받기
N, answerMeter = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
print(solution(N, answerMeter, arr))