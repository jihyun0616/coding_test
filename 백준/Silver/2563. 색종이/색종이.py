num = int(input())
board=[[0]*100 for _ in range(100)] #100x100 배열을 0으로 초기화

for i in range(num): #색종이 수만큼 반복
    x,y=map(int,input().split())
    x-=1
    y-=1
    for j in range(10):
        for k in range(10):
            if(board[x+j][y+k]!=1): #색종이의 넓이만큼 배열값을 1로 변경(이미 덮어져있다면 변경x)
                board[x+j][y+k]=1

area = 0
for i in range(100): #100x100 배열을 순회하며 색종이로 덮여있는 (배열값이 1인) 넓이를 구함
    for j in range(100):
        if(board[i][j]==1):
            area+=1

print(area)
     
