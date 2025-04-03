x_list=[]
y_list=[]

x_last=0
y_last=0

for i in range(3):
    x,y=map(int,input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i])==1:
        x_last=x_list[i]
    if y_list.count(y_list[i])==1:
        y_last=y_list[i]

print(x_last,y_last)

