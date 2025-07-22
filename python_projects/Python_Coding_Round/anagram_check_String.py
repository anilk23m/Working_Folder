#`"Listen"` and `"Silent"` → `True`

def check_anagram_string(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    counter_s1 = {}
    for ch in s1:
        counter_s1[ch] = counter_s1.get(ch, 0) + 1

    counter_s2 = {}
    for ch in s2:
        counter_s2[ch] = counter_s2.get(ch, 0) + 1
    return counter_s1 == counter_s2

s1 = "Listen"
s2 = "Silent"
output = check_anagram_string(s1, s2)
print(output)
