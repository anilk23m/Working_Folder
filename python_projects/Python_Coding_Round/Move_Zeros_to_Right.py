def move_zeros_right(elements):
    non_zero = []
    zero = []
    for i in elements:
        if i == 0:
            zero.append(i)
        else:
            non_zero.append(i)
    return non_zero + zero

elements = [0, 1, 0, 3, 12]
output = move_zeros_right(elements)
print(output)

#Another way using list comprehension
elements = [0, 1, 0, 3, 12]
move_zero = [i for i in elements if i != 0] + [i for i in elements if i == 0]

print(move_zero)