x_list=[]
y_list=[]
x_min =0
x_max =0
y_min =0
y_max =0

N=int(input())

for i in range(N):
    x,y=map(int,input().split())
    if(N==1) :
        print(0)
        break
    x_list.append(x)
    y_list.append(y)
else : 
    x_min = min(x_list)
    x_max = max(x_list)
    y_min = min(y_list)
    y_max = max(y_list)
    print((x_max-x_min)*(y_max-y_min))
