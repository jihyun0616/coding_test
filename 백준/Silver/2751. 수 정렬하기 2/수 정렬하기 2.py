import sys # 입력 많이 받을때는 sys.stdin.readline()
N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(num_list):
    print(i)