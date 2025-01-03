n, m = map(int, input().split())

def draw_rectangle(n, m):
    for _ in range(n):
        print("1" * m)

draw_rectangle(n,m)