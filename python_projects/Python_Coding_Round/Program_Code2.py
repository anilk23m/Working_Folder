# Write a program to find common elements from 2 lists.
a = [2,4,1,6,8,3]
b = [4,2,6,7,5,9]

def find_common_elements(list1, list2):
    common_elements = []
    for i in list1:
        if i in list2:
            common_elements.append(i)
    return common_elements
output = find_common_elements(a, b)
print(output)
