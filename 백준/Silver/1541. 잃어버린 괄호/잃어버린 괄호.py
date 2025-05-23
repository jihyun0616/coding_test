user_input = input()
expression = user_input.split('-') #-는 분리

total=0
for i in range(len(expression)):
    plus=expression[i].split('+') #+는 무조건 더하기(괄호 효과)
    plus_sum=sum(map(int,plus))

    if (i==0):
        total+=plus_sum #첫번째는 무조건 더하고
    else:
        total-=plus_sum #이후부터는 -로 빼기


print(total)
    