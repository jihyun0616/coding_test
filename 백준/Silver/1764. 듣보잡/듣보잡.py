N,M=map(int,input().split())
a=set(input() for _ in range (N))
b=set(input() for _ in range(M))

duplicate = sorted(a&b)

print(len(duplicate))
for i in duplicate:
    print(i)
