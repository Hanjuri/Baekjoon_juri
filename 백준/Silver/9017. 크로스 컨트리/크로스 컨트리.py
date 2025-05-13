from collections import Counter

def solution(M, arr):
    # 조건을 만족하는 참가자만 추출
    pass_Index = list(x for x in set(arr) if arr.count(x) >= 6)

    # 통과한 사람들의 리스트
    passPeople = list(x for x in arr if x in pass_Index)

    # 점수와 등장 횟수 초기화
    totalScore = [0 for _ in range(len(pass_Index))]
    totalCount = [0 for _ in range(len(pass_Index))]
    fifthAppearanceIndex = [-1 for _ in range(len(pass_Index))]  # 5번째 등장 위치 기록
    realScore = [0 for _ in range(len(pass_Index))]

    for i, p in enumerate(passPeople):
        idx = pass_Index.index(p)
        totalCount[idx] += 1
        totalScore[idx] += (i + 1)

        # 5번째 등장 시점 기록
        if totalCount[idx] == 5:
            fifthAppearanceIndex[idx] = i + 1  # 등장한 시점 (1-based)

        # 4번째까지 점수를 기록
        if totalCount[idx] == 4:
            realScore[idx] = totalScore[idx]


    # 결과 정렬: Real Score 기준으로 우선 정렬, 같으면 5번째 등장 인덱스 기준
    result = sorted(zip(pass_Index, realScore, fifthAppearanceIndex), key=lambda x: (x[1], x[2]))

    # 최종 결과
    finalResult = result[0][0]
    return finalResult

N = int(input())
totalArr = []
for _ in range(N):
  M = int(input())
  arr = list(map(int, input().split()))
  totalArr.append((M, arr))
for total in totalArr:
  print(solution(total[0], total[1]))