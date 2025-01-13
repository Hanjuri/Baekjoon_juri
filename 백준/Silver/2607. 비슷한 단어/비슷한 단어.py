from collections import Counter

def solution(N, word, arr):
    target_count = Counter(word)  # 기준 단어의 문자 빈도 수
    answerCount = 0

    for a in arr:
        current_count = Counter(a)  # 비교 단어의 문자 빈도 수
        diff = 0

        # 기준 단어와 비교 단어의 차이 계산
        for char in set(word + a):
            diff += abs(target_count[char] - current_count[char])

        # 비슷한 단어 조건
        if len(word) == len(a) and diff <= 2:  # 교체
            answerCount += 1
        elif len(word) + 1 == len(a) and diff <= 1:  # 추가
            answerCount += 1
        elif len(word) - 1 == len(a) and diff <= 1:  # 제거
            answerCount += 1

    return answerCount

# 입력 처리
N = int(input())
target = input()
arr = [input() for _ in range(N - 1)]
print(solution(N, target, arr))