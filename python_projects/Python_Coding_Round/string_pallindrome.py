#Given a string, check if the given string is pallindrome or not

#Method 1
def check_pallindrome(s):
    i, j = 0, len(s)-1

    is_pallindrome = True

    while i < j:
        if s[i] != s[j]:
            is_pallindrome = False
            break
        i += 1
        j -= 1
    if is_pallindrome:
        print(f"Given string is a pallindrome - {s}")
    else:
        print("Given string is not a pallindrome")
s = "malayalam"
check_pallindrome(s)

#Method 2
if s[:] == s[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")

#Method 3
rev_s = "".join(reversed(s))
if s == rev_s:
    print("Pallindrome")
else:
    print("Not Pallindrome")

#Method 4
rev = ""
for i in s:
    rev = i + rev
if s == rev:
    print("Pallindrome")
else:
    print("Not Pallindrome")


