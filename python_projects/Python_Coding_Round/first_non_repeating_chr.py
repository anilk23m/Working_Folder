def first_non_repeating_chr(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0)+1
    print(d)
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1
print(first_non_repeating_chr("swiss"))