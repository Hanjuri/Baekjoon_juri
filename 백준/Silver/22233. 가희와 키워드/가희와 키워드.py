import sys
input = sys.stdin.read

def solution(N, M, keyword, arr):
    answer = []
    keySet = set(keyword)  # 키워드를 집합으로 변환
    for a in arr:
        usedKey = set(a)  # 현재 문장의 단어들을 집합으로 변환
        keySet -= usedKey  # 키워드에서 사용된 단어 제거
        answer.append(len(keySet))  # 남은 키워드 개수 추가
    return answer

# 입력 처리
data = input().splitlines()
N, M = map(int, data[0].split())
keyword = data[1:N+1]  # N개의 키워드
arr = [line.split(",") for line in data[N+1:N+1+M]]  # M개의 문장

# 결과 계산 및 출력
answerArr = solution(N, M, keyword, arr)
print(*answerArr, sep="\n")