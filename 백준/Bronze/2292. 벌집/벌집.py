N=int(input())


# 1   
# 2 ~ 7 >> 1*6+1 >> 1+6
# 8 ~ 19  >> 2*6+1*6+1 >> 1+6+12
# 20 ~ 37  >> 3*6+2*6+1*6+1 >> 1+6+12+18
# 38 ~ 61  >> 4*6+3*6+2*6+1*6 >> 1+6+12+18+24 ...

cnt=1
room=1

for i in range(1,1000000000):
    if(N<=cnt):
        break
    cnt+=6*i
    room+=1

print(room)