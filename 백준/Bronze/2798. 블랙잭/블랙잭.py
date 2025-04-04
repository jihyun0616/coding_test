N,M=map(int,input().split())
cards=list(map(int,input().split()))


max=0 # 초기화
for first in range(N): # 하나씩 전부 탐색
    for second in range(first+1,N):
        for third in range(second+1,N):
            res=cards[first]+cards[second]+cards[third]
            
            if(res==M): #M 과 같다면 출력
                print(res)
                exit() #프로그램 전체를 종료하고 싶을 때 사용하는 메서드
            elif M>res>max:
                max=res

print(max)          