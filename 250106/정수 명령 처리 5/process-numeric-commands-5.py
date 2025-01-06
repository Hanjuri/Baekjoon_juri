N = int(input())

command = []
num = []
array = []

# 명령 입력 받기
for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

for i in range(N):
    if command[i] == "push_back":
        array.append(num[i])
    elif command[i] == "get":
        print(array[num[i] - 1])  # Arrays are 0-based, but input is 1-based
    elif command[i] == "size":
        print(len(array))
    elif command[i] == "pop_back":
        if array:  # Check if array is not empty
            array.pop()