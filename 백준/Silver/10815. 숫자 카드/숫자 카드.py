import sys

N=int(input())
N_set=set(map(int,sys.stdin.readline().split()))
M=int(input())
M_set=list(map(int,sys.stdin.readline().split()))

for i in M_set:
    if(i in N_set):
        print(f'1 ',end="")
    else:
        print(f'0 ',end="")