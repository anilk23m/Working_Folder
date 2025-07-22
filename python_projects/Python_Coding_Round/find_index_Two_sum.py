nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        compliment = target-num
        if compliment in num_map:
            return [num_map[compliment], i]
        num_map[num] = i
    return [] #incase no solution exists
print(two_sum(nums, target))
