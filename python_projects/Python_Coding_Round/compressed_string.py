def compressed_str(s):
    comp_s = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            comp_s.append(s[i-1] + str(count))
            count = 1
    comp_s.append(s[-1] + str(count))
    return "".join(comp_s)
s = "aaabbcc"
print(compressed_str(s))