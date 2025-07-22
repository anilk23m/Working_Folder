#Reverse each word in a sentence, but keep word order
#Input: "hello world" → Output: "olleh dlrow"

def reverse_each_word(s):
    split_string = s.split()
    result = []
    for i in split_string:
        reverse_string = ''
        for j in i:
            reverse_string = j+reverse_string
        result.append(reverse_string)
    return " ".join(result)
s = "hello world"
output = reverse_each_word(s)
print(output)