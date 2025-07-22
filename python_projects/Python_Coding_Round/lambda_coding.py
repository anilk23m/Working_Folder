add_10 = lambda x:x+10
print(add_10(15))

multiply_two = lambda x,y : x*y
print(multiply_two(5,6))

even_odd_check = lambda x : "even" if x%2 == 0 else "odd"
print(even_odd_check(2))

people = [
    ("Alice", 30, 88),
    ("Bob", 25, 75),
    ("Charlie", 35, 95),
    ("David", 28, 65),
    ("Eve", 22, 85),
    ("Frank", 30, 70),
    ("Grace", 25, 90),
]

sorted_people = sorted(people, key = lambda x:x[1])
print(sorted_people)

l = [2,3,4,5,6,7]
l_square = list(map(lambda x : x**2, l))
print(l_square)

words = [
    "apple",
    "Banana",
    "cherry",
    "date",
    "Elderberry",
    "fig",
    "grape",
    "Honeydew",
    "kiwi",
    "lemon",
    "Mango",
    "nectarine"
]

word_title = list(map(lambda x: x.title(), words))
print(word_title)

word_len5 = lambda x :  len(x) == 5
print(list(filter(word_len5, words)))

sorted_words = sorted(words, key = len)
print(sorted_words)

sorted_words = sorted(words, key = lambda x : len(x))
print(sorted_words)

word_filter = lambda x : x[0].lower() in "aeiou"
print(list(filter(word_filter, words)))

count_vowel = lambda word: sum(1 for ch in word.lower() if ch in "aeiou")
vowel_count = list(map(count_vowel, words))
print(vowel_count)

word_e = lambda word: "e" not in word.lower()
print(list(filter(word_e, words)))

longest_word = max(words, key=lambda x:len(x))
print(longest_word)

shortest_word = min(words, key=lambda x:len(x))
print(shortest_word)

word_4 = lambda word: word[::-1] if len(word) > 4 else word
print(list(map(word_4, words)))

#Filter out all even numbers from a list.
even_no = lambda x:x%2==0
print(list(filter(even_no, l)))

#Filter all strings longer than 5 characters.
string_5 = lambda x : len(x) == 5
print(list(filter(string_5, words)))

#Keep only palindromes from a list of strings
palindrome_str = lambda x : x == x[::-1]
print(list(filter(palindrome_str, words)))

#Filter numbers that are divisible by both 3 and 5
num_div_3_5 = lambda x : x %3 ==0 and x %5 == 0
print(list(filter(num_div_3_5, l)))

from functools import reduce
#Find the product of all numbers in a list.
prod_nums = lambda x,y : x*y
print(reduce(prod_nums, l))

#Concatenate all strings in a list into a single string
Concatenate_str = lambda x,y : x + " "+y
print(reduce(Concatenate_str, words))

