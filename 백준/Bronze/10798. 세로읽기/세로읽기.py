word = [input() for i in range(5)] #리스트 컴프리헨션

for j in range(15):
    for i in range(5):
        if j<len(word[i]):
            print(word[i][j],end="")