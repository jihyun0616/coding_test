piano = list(map(int,input().split()))

flag=0

for i in range(7):
    if(piano[i]<piano[i+1]):
        flag += 1
    elif(piano[i]>piano[i+1]):
        flag += 2

if(flag==7):
    print("ascending")
elif(flag==14):
    print("descending")
else:
    print("mixed")