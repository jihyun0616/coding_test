N=int(input())
numlist=[]
for i in range(N):
    number=int(input())
    numlist.append(number)

for i in sorted(numlist):
    print(i)