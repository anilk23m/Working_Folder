# Write a program to find the largest element in the list.

L = [10,45,23,22,5]

def find_largest_value(l):
    largest_value = l[0]
    for i in l:
        if i > largest_value:
            largest_value = i
    return largest_value
output = find_largest_value(L)
print(output)

