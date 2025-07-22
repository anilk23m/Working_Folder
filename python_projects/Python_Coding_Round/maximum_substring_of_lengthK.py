s = 'aaabbc'
k =3
def find_maximum_substring(s,k):
    if len(s)<k:
        return 0
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in char_count:
        if char_count[char]<k:
            max_length = 0
            for part in s.split(char):
                max_length = max(max_length, find_maximum_substring(part, k))
            return max_length
    return len(s)
print(find_maximum_substring(s,k))