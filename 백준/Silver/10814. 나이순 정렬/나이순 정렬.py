N=int(input())
member=[list(input().split()) for _ in range(N)]

member.sort(key=lambda x:int(x[0]))

for age,name in member:
    print(age,name)