T=int(input())
money_list=[25,10,5,1] #쿼터, 다임, 니켈, 페니

for i in range(T):
    money=int(input())
    money_count=[0]*4

    for j in range(len(money_list)):
        money_count[j]=money//money_list[j]
        money=money%money_list[j]
        if(money==0):
            break

    print(' '.join(map(str,money_count))) 
    #join은 문자열끼리만 합칠 수 있다.
    #현재 money_count는 정수형 리스트이므로 str형으로 변환한다.







