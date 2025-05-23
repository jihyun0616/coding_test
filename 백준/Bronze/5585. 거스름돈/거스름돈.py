money_list=[500,100,50,10,5,1]
count = 0

money = 1000-int(input()) #입력

for i in money_list:
    count+=money//i
    money%=i

print(count)