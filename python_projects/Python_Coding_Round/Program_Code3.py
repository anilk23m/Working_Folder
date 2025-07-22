# Write a program to remove duplicate from the list.
L = [1,3,2,5,6,1,5,8,7]

def remove_duplicate(l):
    unique_value_list = []
    for i in l:
        if i not in unique_value_list:
            unique_value_list.append(i)
    return unique_value_list
output = remove_duplicate(L)
print(output)