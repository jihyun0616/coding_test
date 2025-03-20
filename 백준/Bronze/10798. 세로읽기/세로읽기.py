word = []
max_len = 0 

for i in range(5):
    inputValue = list(input())  
    word.append(inputValue)
    if max_len <= len(inputValue):  
        max_len = len(inputValue)

for i in range(5):
    if len(word[i]) < max_len: 
        for j in range(max_len - len(word[i])):
            word[i].append(' ') 

for i in range(max_len):
    for j in range(5):
        if(word[j][i]!=' '):
            print(word[j][i],end="")
