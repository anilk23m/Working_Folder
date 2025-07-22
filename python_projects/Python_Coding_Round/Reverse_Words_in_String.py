s = "this is the sentence to reverse"

def reverse_words_in_string(s):
    words = s.split()
    reversed_words = ""

    for word in reversed(words):
        reversed_words += word + " "
    print(reversed_words.strip())
reverse_words_in_string(s)
