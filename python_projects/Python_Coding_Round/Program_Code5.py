# Find the least frequent character in the string.

s = 'thisistest'
def find_least_frequent_chr(s):
    d = {}
    l = []
    c = 0
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    min_freq = 0
    for i in d:
        if d[i] < min_freq:
            min_freq = d[i]
    least_freq_char = []
    for i in d:
        if d[i] == min_freq:
            least_freq_char.append(i)
        return least_freq_char
output = find_least_frequent_chr(s)
print(output)
