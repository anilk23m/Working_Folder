#`"ProPgramming"` → `"Poain"`

def remove_repeated_characters(s):
    chars = list(s)
    count = {}
    for i in s:
        count[i.lower()] = count.get(i.lower(),0) + 1

    result = []
    for ch in chars:
        if count[ch.lower()] == 1:
            result.append(ch)
    return "".join(result)

s = "ProPgramming"
output = remove_repeated_characters(s)
print(output)