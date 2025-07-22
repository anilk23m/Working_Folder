#Given string is symmetric or not - first half should be equal to second half if its even length else will skip the middle char to check symmetric

s = "amaama"

def is_symmetric(s):
    half = len(s) // 2
    sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]

    if sym:
        print("Given string is symmetric")
    else:
        print("Given string is not symmetric")
is_symmetric(s)



