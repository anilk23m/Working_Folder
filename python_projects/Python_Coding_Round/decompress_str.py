s = "a3b2c4"
def decompress(s):
    result = []
    compress_s = ''
    for i in range(len(s)):
        if s[i].isalpha():
            compress_s += s[i]
        else:
            result.append(compress_s*int(s[i]))
            compress_s = ''
    return "".join(result )
print(decompress(s))