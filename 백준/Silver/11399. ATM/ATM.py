number=int(input())
time_list=sorted(list(map(int,input().split())))

total=0
now=0
for i in time_list:
    now+=i
    total+=now

print(total)