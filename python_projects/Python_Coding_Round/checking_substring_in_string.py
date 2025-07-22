string1 = "A geek in need is a geek indeed"

substring = 'need'

#Method 1
if substring in string1:
    print("Yes! it is present in the string")
else:
    print("No, its not present")

#Method 2
def check(string1, substring):
    if string1.find(substring) == -1:
        print("Not present")
    else:
        print("Present")

#Method 3
if string1.count(substring) > 0:
    print("Present")
else:
    print("Not present")
