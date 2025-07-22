# find all the subarrays from the list where the total of elements is 10. List will always be traversed sequentially.
#brute-force approace with O(n2) time complexity
L = [1,2,3,2,1,1,2,3,1,2,2]
def find_subarrays_with_sum(lst, target):
    result = []
    for start in range(len(lst)):
        total = 0
        subarray = []
        for end in range(start, len(lst)):
            total += lst[end]
            subarray.append(lst[end])
            if total == target:
                result.append(subarray)
                break
            elif total > target:
                break
    return result
output = find_subarrays_with_sum(L, target=10)
print(output)

#sliding window with O(n) time complexity
def sliding_window_subarrays_with_sum(lst, target):
    result = []
    start = 0
    current_sum = 0
    for end in range(len(lst)):
        current_sum += lst[end]

        while current_sum > target:
            current_sum -= lst[start]
            start += 1
        if current_sum ==  target:
            result.append(lst[start:end +1])
    return result
output = sliding_window_subarrays_with_sum(L, target=10)
print(output)
