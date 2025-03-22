number_list=[0]*42

for i in range (10):
    number=int(input())
    number_2 = number%42
    number_list[number_2]+=1

count = 0 

for i in number_list:
    if(i!=0):
        count+=1

print(count)