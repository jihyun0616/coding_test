N=input()
number_list=[]
for i in str(N):
    number_list.append(int(i))

print("".join(map(str,sorted(number_list,reverse=True))))