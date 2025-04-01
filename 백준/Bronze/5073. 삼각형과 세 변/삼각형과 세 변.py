
while True:
    A,B,C=map(int,input().split())
    t_list = [A,B,C]

    if(A==0 and B==0 and C==0): #종료 조건
        break

    if(A==B and B==C and C==A):
        print("Equilateral") #정삼각형 조건이 맨 위에 와야함

    elif(max(t_list)>=sum(t_list)-max(t_list)):
        print("Invalid")

    elif(A==B or B==C or C==A):
        print("Isosceles")
    else:
        print("Scalene")


