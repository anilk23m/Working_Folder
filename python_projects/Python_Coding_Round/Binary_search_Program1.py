#Input: arr = [1, 3, 5, 7, 9], target = 5
#Output: 2 (index)
#it apply to only sorted array
def find_index_binary_search(elements, target):
    left_index, right_index = 0, len(elements)-1
    while left_index <= right_index:
        mid = (left_index+right_index)//2
        if elements[mid] == target:
            return mid
        elif elements[mid] < target:
            left_index = mid +1
        else:
            right_index = mid - 1
    return -1

elements = [1, 3, 5, 7, 9]
output = find_index_binary_search(elements=elements, target=7)
print(output)