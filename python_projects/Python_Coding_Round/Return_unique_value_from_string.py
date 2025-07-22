#S="AaSsBi" - here output should be unique value which is "Bi"

s = "AaSsBi"

def return_unique_from_string(s):
    result = ""
    for i in range(len(s)):
        if s.lower().count(s[i].lower()) == 1:
            result += s[i]
    return result

output = return_unique_from_string(s)
print(output)