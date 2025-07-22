#`"AaSsBi"` → `Uppercase: 'ASB', Lowercase: 'asi'`

def separate_upper_lower(s):
    uppercase = []
    lowercase = []

    for i in s:
        if i.isupper():
            uppercase.append(i)
        elif i.islower():
            lowercase.append(i)
    return "".join(uppercase), "".join(lowercase)
s = "AaSsBi"
upper_list, lower_list = separate_upper_lower(s)
print(upper_list, lower_list)