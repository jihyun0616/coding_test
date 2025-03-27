N=int(input())

# 1번 - 2^2
# 2번 - 3^2 +1
# 3번 - 5^2 +2
# 4번 - 9^2 +4
# 5번 - 17^2 +8
# 6번 - 33^2 +19

sum=2

for i in range(0,N):
    sum+=pow(2,i)

print(pow(sum,2))
