# reverse the string but keep the special character position in place
st1 = 'abc@45def##g'
# out = 'gfe@d54cb##a'

def reverse_keep_special(s):
    chars = list(s)
    only_char = [ch for ch in chars if ch.isalnum()]
    only_char.reverse()

    result = []
    index = 0

    for ch in chars:
        if ch.isalnum():
            result.append(only_char[index])
            index += 1
        else:
            result.append(ch)
    return "".join(result)
output = reverse_keep_special(st1)
print(output)