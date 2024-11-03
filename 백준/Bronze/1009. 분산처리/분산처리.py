def solution(N, arr):
    # 1의 자리 숫자에 대한 주기 테이블을 미리 정의
    last_digit_patterns = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    results = []
    for a in arr:
        base, exp = a[0], a[1]
        nowBase = base % 10
        nowPattern = last_digit_patterns[nowBase]
        nowPatternLen = len(nowPattern)
        answer = nowPattern[(exp%nowPatternLen)-1]

        if answer == 0:
          answer  = 10
        
        results.append(answer)
        
    for r in results:
      print(r)

# 입력 처리
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

solution(N, arr)