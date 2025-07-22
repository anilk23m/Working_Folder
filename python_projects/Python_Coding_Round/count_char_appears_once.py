s = "Teeter"

def count_chr_having_lenone(s):
    s = s.lower()
    result = []
    for i in s:
        if s.count(i) == 1:
            result.append(i)
    return result
result = count_chr_having_lenone(s)
print(result)
