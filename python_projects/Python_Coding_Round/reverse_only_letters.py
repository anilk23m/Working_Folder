# Input: "a1b2c3!" → Output: "c1b2a3!"
# Reverse only letters, keep digits/special character in place
string1 = "a1b2c3!"
def reverse_only_letters(s):
    letters = list(s)
    only_letters = [ch for ch in letters if ch.isalpha()]
    only_letters.reverse()

    result = []
    index = 0

    for i in letters:
        if i.isalpha():
            result.append(only_letters[index])
            index += 1
        else:
            result.append(i)
    return "".join(result)
output = reverse_only_letters(string1)
print(output)

