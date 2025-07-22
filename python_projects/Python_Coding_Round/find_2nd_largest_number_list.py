# find the second-largest number from the list
def find_2nd_largest(elements):
    first_largest = second_largest = float('-inf')
    for num in elements:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    if second_largest == float('-inf'):
        return "No second largest number found"
    return second_largest
list1 = [45,78,89,56,23,12]
print(find_2nd_largest(list1))

def find_second_lowest(elements):
    first_lowest = second_lowest = float('inf')
    for num in elements:
        if num < first_lowest:
            second_lowest = first_lowest
            first_lowest = num
        elif num < second_lowest and num != first_lowest:
            second_lowest = num
    if second_lowest == float("inf"):
        return "No second lowest number found"
    return second_lowest
list1 = [45,78,89,56,23,12]
print(find_second_lowest(list1))