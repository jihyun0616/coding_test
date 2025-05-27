N=int(input())
km = list(map(int,input().split()))
price =  list(map(int,input().split()))

now_price = price[0]
total_price = 0

for i in range(N-1):
    total_price += now_price*km[i]

    if price[i+1] < now_price:
        now_price=price[i+1]

print(total_price)