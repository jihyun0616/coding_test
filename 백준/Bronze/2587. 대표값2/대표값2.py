num_list = []
for i in range(5):
    num_list.append(int(input()))

print(sum(num_list)//len(num_list))
print(sorted(num_list).pop(2))