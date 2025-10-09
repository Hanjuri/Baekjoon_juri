MAX_DIGIT = 10

def radix_sort(arr):
    max_val = max(arr)
    p = 1
    while max_val // p > 0:  # 실제 최대 자릿수만큼 반복
        arr_new = [[] for _ in range(MAX_DIGIT)]

        for elem in arr:
            digit = (elem // p) % 10
            arr_new[digit].append(elem)

        arr = []
        for digit in range(MAX_DIGIT):
            for elem in arr_new[digit]:
                arr.append(elem)

        p *= 10

    return arr


# 입력
n = int(input())
arr = list(map(int, input().split()))

# 실행
arr = radix_sort(arr)

print(*arr)
