N,B=input().split()

B=int(B)

N=list(N) #또는 N=N[::-1]
N.reverse() 

allList=list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
convert=0


for i in range(len(N)):
    convert += (allList.index(N[i]))*(B**i)

print(convert)