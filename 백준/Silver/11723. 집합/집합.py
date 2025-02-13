import sys

M = int(sys.stdin.readline().strip())
set_data = set()

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "add":
        set_data.add(int(command[1]))
    elif command[0] == "remove":
        set_data.discard(int(command[1]))  # discard 사용
    elif command[0] == "check":
        print(1 if int(command[1]) in set_data else 0)
    elif command[0] == "toggle":
        num = int(command[1])
        if num in set_data:
            set_data.remove(num)
        else:
            set_data.add(num)
    elif command[0] == "all":
        set_data = set(range(1, 21))  # copy 없이 직접 할당
    elif command[0] == "empty":
        set_data.clear()
