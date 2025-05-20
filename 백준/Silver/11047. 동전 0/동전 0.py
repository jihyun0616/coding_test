N, K = map(int, input().split())

money_list = [int(input()) for _ in range(N)]
money_list.sort(reverse=True)

count=0
for i in money_list:
    if i<=K:
        count+=K//i #몫
        K=K%i #나머지

print(count)


