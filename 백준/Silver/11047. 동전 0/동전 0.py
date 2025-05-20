N, K = map(int, input().split())

money_list = []
for i in range(N):
    money = int(input())
    money_list.append(money)


money_list.sort()

flag = 0
for i in range(len(money_list)):
    if K < money_list[i]:
        flag = money_list[i - 1]
        break
    elif K == money_list[i]:
        flag = money_list[i]
        break
    else:
        flag = money_list[-1] 
        
money_list.sort(reverse=True)

count = 0
for coin in money_list:
    if coin > flag:
        continue
    if K >= coin:
        num = K // coin
        count += num
        K -= coin * num

print(count)