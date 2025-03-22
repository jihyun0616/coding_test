T = int(input())


for i in range(T):
    sum=0
    count=0
    quiz=list(input())
    for j in quiz:
        if(j!='X'):
            count+=1
            sum+=count
        else:
            count=0
    print(sum)