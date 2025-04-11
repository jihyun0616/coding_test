N,k=map(int,input().split())
num_list=list(map(int,input().split()))
print(sorted(num_list).pop(N-k))