import math

A,B,V=map(int,input().split())


day = math.ceil((V-A)/(A-B))+1 #(V-A)까지는 확실, 전날 A까지 올라가서 도달하는것을 고려해야함
print(day)