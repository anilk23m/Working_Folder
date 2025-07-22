def find_permutation(s):
    if len(s) == 1:
        return list(s)
    permutations = []

    for i in range(len(s)):
        curr_chr = s[i]
        remaining_chr = s[:i] + s[i + 1:]
        remaining_permutations = find_permutation(remaining_chr)

        for p in remaining_permutations:
            permutations.append(curr_chr + p)
    return permutations


s = "abc"
print(find_permutation(s))