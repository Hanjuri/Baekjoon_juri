n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
happy_sequence_no = 0

def is_happy_sequence(arr, m):
    count = 1
    prev = arr[0] #이전 숫자 저장

    for i in range(1, len(arr)):
        if arr[i] == prev : 
            count += 1
            if count >= m :
                return True
        else :
            count = 1 #초기화
        prev = arr[i]
    
    return count >= m #m=1인 경우 고려

for row in grid :
    if is_happy_sequence(row, m):
        happy_sequence_no += 1

for j in range(n):
    column = [grid[i][j] for i in range(n)]
    if is_happy_sequence(column, m):
        happy_sequence_no += 1

print(happy_sequence_no)
        