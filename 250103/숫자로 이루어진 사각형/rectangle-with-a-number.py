n = int(input())

def draw_n_square(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if cnt%10 == 0:
                cnt += 1
            print(cnt%10, end=" ")
            cnt += 1
        print()


draw_n_square(n)