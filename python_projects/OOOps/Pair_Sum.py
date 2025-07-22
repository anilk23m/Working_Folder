X = [1,7,4,2,1,3,11,5]

def twosum(arr, sum):
    arr.sort()
    left = 0
    right = len(arr)-1
    while (left <= right):
        if (arr[left] + arr[right]>sum):
            right = right-1
        elif (arr[left] + arr[right] < sum):
            left = left+1
        elif (arr[left] + arr[right] == sum):
            print ("values of pair are ", arr[left], "&", arr[right])
            right = right - 1
            left = left + 1
arr = X
sum = 6
twosum(arr, sum)