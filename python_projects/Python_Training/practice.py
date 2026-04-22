#write a python code to convert the lower case to upper and upper case to lower -
#input - "AaMeRicA is sIlIcON vaLLey of WORld"
#output - "aAmErICa IS SiLiCon VAllEY OF worLD"

s = "AaMeRicA is sIlIcON vaLLey of WORld"
output = ""
for i in s:
    if i.islower():
        output += i.upper()
    elif i.isupper():
        output += i.lower()
    else:
        output += i
print(output)

#write a code to move all the 0 to right side of the list
#input - [1,2,0,3,0,4,5]
#output-[1,2,3,4,5,0,0]
nums = [1,2,0,3,0,4,5]
non_zero = [x for x in nums if x!=0]
zeros = [x for x in nums if x == 0]

result = non_zero + zeros
print(result)
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
print(nums)
