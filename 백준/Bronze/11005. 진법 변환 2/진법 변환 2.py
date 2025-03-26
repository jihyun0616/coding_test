N,B=map(int,input().split())

allList=list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

store=[]

while(True):
    if(N==0):
        break
    store.append(allList[N%B])
    N=N//B


store.reverse() #reverse는 문자열만 뒤집을뿐 return값이 없다.

# 아래 코드를 대신하여 '구분자'.join(리스트)를 이용할 수 있다. 
# 리스트에 있는 문자열들을 하나로 이어 붙여서 문자열로 만들어주는 내장함수이다.
# for i in range(len(store)):
#     print(store[i],end="")

print(''.join(store))
