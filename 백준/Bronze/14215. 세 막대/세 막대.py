a,b,c=map(int,input().split())
round_list=[a,b,c]

if a==b==c:
    print(a*3)
else:
    if max(round_list)<sum(round_list)-max(round_list):
        print(sum(round_list))
    else:
        index = round_list.index(max(round_list))
        round_list.pop(index)
        print(sum(round_list)+sum(round_list)-1)