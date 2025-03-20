num = int(input())
board=[[0]*100 for _ in range(100)] #100x100 배열을 0으로 초기화

for i in range(num): #색종이 수만큼 반복
    x,y=map(int,input().split())

    for i in range(x,x+10): #(변경) x1~x1+10까지 순회하는 코드 range로 작성
        for j in range(y,y+10): #(변경) y1~y1+10까지 순회하는 코드 range로 작성
            board[i][j]=1 #색종이로 뒤덮여 있는 지역은 1로 변경


area = 0
for i in range(100): #100x100 배열을 순회하며 색종이로 덮여있는 (배열값이 1인) 넓이를 구함
    area+=board[i].count(1) #(변경)2차원 리스트이므로, board[i]에서 1인 값을 추출(count(1))하여 누적합을 구한다.
print(area)
     
# 참고 : https://ji-gwang.tistory.com/325