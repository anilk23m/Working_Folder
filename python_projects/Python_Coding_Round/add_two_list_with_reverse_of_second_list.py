list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

output_list = []
for i in range(len(list1)):
    output_list.append(list1[i] + list2[::-1][i])
print(output_list)