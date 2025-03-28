while True:

    n=int(input())

    if(n==-1): # 종료 조건
        break

    n_list=[] # 약수들 저장할 리스트

    for i in range(1,n):
        if(n%i==0):
            n_list.append(i) # i가 n의 약수라면 n_list에 추가한다.
    
    if(sum(n_list)==n): # n의 약수들의 합이 n과 같다면
        print(str(n)+" = "+' + '.join(map(str,n_list))) 
    else:
        print(str(n)+" is NOT perfect.") 
    


