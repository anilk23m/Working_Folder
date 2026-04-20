#String methods
### `upper()`
#Converts all characters to uppercase.

"hello".upper()           # 'HELLO'
"Hello World".upper()     # 'HELLO WORLD'
"123abc".upper()          # '123ABC'  → digits stay as-is
"".upper()                # ''        → empty string returns empty

### `lower()`
#Converts all characters to lowercase.
"HELLO".lower()           # 'hello'
"Hello World".lower()     # 'hello world'
"ABC123".lower()          # 'abc123'

### `title()`
#Converts the **first letter of every word** to uppercase, rest to lowercase.

"hello world".title()         # 'Hello World'
"it's a test".title()         # "It'S A Test"  ⚠️ treats ' as word boundary
"hello-world".title()         # 'Hello-World'  → hyphen is also a boundary
"123abc def".title()          # '123Abc Def'


import python_String
string.capwords("it's a test")   # "It's A Test"


### `capitalize()`
#Only the **first character** of the entire string is uppercased. Everything else becomes lowercase.


"hello world".capitalize()    # 'Hello world'
"HELLO WORLD".capitalize()    # 'Hello world'  → rest forced to lower
"123hello".capitalize()       # '123hello'     → digit can't be capitalized
"".capitalize()               # ''

#**Difference from `title()`:** `capitalize()` affects only the very first character, `title()` affects every word.

### `swapcase()`
#Flips uppercase to lowercase and vice versa.

"Hello World".swapcase()      # 'hELLO wORLD'
"PyThOn".swapcase()           # 'pYtHoN'
"123".swapcase()              # '123'  → no effect on digits

## 2. SEARCH & FIND METHODS
### `find(sub, start, end)`
#Returns the **lowest index** where substring `sub` is found. Returns **`-1`** if not found.

"hello world".find("world")       # 6
"hello world".find("python")      # -1  → not found
"hello hello".find("hello")       # 0   → first occurrence
"hello world".find("o", 5)        # 7   → search starts from index 5
"hello world".find("o", 5, 8)     # 7   → search between index 5 and 8

### `index(sub, start, end)`
#Exactly like `find()`, but raises **`ValueError`** if not found instead of returning -1.

"hello".index("ell")              # 1
"hello".index("xyz")              # ValueError: substring not found

#**When to use `find()` vs `index()`:**

### `count(sub, start, end)`
#Counts **non-overlapping** occurrences of a substring.

"hello world hello".count("hello")     # 2
"aaa".count("aa")                      # 1  ⚠️ non-overlapping!
"hello".count("l")                     # 2
"hello".count("xyz")                   # 0
"hello world".count("o", 5)            # 1  → count from index 5

#Edge case:** `"aaa".count("aa")` returns `1`, not `2`, because Python doesn't count overlapping matches.

### `startswith(prefix, start, end)`
#Checks if string starts with the given prefix. Can accept a **tuple** of prefixes.

"hello".startswith("hel")              # True
"hello".startswith("Hel")              # False  → case-sensitive
"hello world".startswith("world", 6)   # True   → check from index 6
"hello".startswith(("hi", "he", "ho")) # True   → tuple of prefixes

### `endswith(suffix, start, end)`
#Checks if string ends with the given suffix. Also accepts a tuple.


"hello.py".endswith(".py")             # True
"hello.py".endswith((".py", ".js"))    # True
"report.pdf".endswith(".docx")         # False

#**Practical use:** File type checking → `if filename.endswith((".jpg", ".png", ".gif"))`


## 3. MODIFY / REPLACE METHODS
### `replace(old, new, count)`
#Replaces occurrences of `old` with `new`. Optional `count` limits how many replacements.

"hello world".replace("world", "Python")     # 'hello Python'
"aaa".replace("a", "b")                      # 'bbb'
"aaa".replace("a", "b", 2)                   # 'bba'  → only first 2
"hello".replace("xyz", "abc")                # 'hello' → no match, no change

### `strip(chars)`
#Removes leading AND trailing characters. Default is whitespace.


"  hello  ".strip()              # 'hello'
"\n\thello\n".strip()            # 'hello'  → removes all whitespace types
"***hello***".strip("*")         # 'hello'
"xxyhelloxyy".strip("xy")       # 'hello'  ⚠️ strips any combo of chars

"abcHELLOcba".strip("abc")      # 'HELLO'   → strips a, b, c individually

## 4. SPLIT & JOIN METHODS
### `split(sep, maxsplit)`
#Splits string into a **list**. Default separator is any whitespace.

"hello world python".split()           # ['hello', 'world', 'python']
"a,b,c".split(",")                     # ['a', 'b', 'c']
"a,,b".split(",")                      # ['a', '', 'b']  → empty string preserved
"a,b,c".split(",", 1)                  # ['a', 'b,c']    → maxsplit=1
"  hello  ".split()                    # ['hello']        → whitespace collapsed
"  hello  ".split(" ")                 # ['', '', 'hello', '', '']  ⚠️ different!

#**Key insight:** `split()` with no argument treats **consecutive whitespace as one separator** and strips leading/trailing. `split(" ")` splits on each individual space — big difference!

### `splitlines(keepends)`
#Splits at line boundaries (`\n`, `\r\n`, `\r`, etc.).


"hello\nworld\npython".splitlines()          # ['hello', 'world', 'python']
"hello\nworld\n".splitlines()                # ['hello', 'world']  → no trailing empty
"hello\nworld\n".split("\n")                 # ['hello', 'world', '']  ⚠️ different!
"hello\nworld".splitlines(keepends=True)     # ['hello\n', 'world']

### `join(iterable)`
#Joins elements of an iterable using the string as **glue**.


",".join(["a", "b", "c"])             # 'a,b,c'
" -> ".join(["start", "middle", "end"])  # 'start -> middle -> end'
"".join(["h", "e", "l", "l", "o"])    # 'hello'
"\n".join(["line1", "line2"])          # 'line1\nline2'


#**Important:** All elements must be strings. Use a generator for non-strings:
",".join(str(x) for x in [1, 2, 3])  # '1,2,3'


## 5. VALIDATION (is-CHECK) METHODS

#All of these return `True` or `False` and return `False` for empty strings.

### `isalpha()`
#True if **all characters are letters** (Unicode letters, not just A-Z).

"Hello".isalpha()        # True
"Hello World".isalpha()  # False  → space is not alpha
"Hello123".isalpha()     # False
"".isalpha()             # False  → empty is always False

### `isdigit()`
#True if all characters are **digits** (includes superscripts like ² but not fractions).

"123".isdigit()          # True
"12.3".isdigit()         # False  → dot is not a digit
"²³".isdigit()           # True   → superscript digits
"-5".isdigit()           # False  → minus sign
"".isdigit()             # False


### `isdecimal()`
#True if all characters are **decimal digits** (0-9). Stricter than `isdigit()`.

"123".isdecimal()        # True
"²³".isdecimal()         # False  → superscripts excluded
"٣٢١".isdecimal()        # True   → Arabic-Indic digits

### `isnumeric()`
#True if all characters are **numeric** (includes digits, fractions, Roman numerals, etc.). Broadest check.

"123".isnumeric()        # True
"²³".isnumeric()         # True
"½¾".isnumeric()         # True   → fractions
"Ⅶ".isnumeric()         # True   → Roman numerals
"1.5".isnumeric()        # False  → dot is not numeric


### `isalnum()`
#True if all characters are **alphanumeric** (letters OR digits).

"Hello123".isalnum()     # True
"Hello 123".isalnum()    # False  → space
"Hello!".isalnum()       # False  → punctuation

### `isupper()`
#True if all **cased** characters are uppercase. Non-cased characters (digits, symbols) are ignored.

"HELLO".isupper()        # True
"HELLO123".isupper()     # True   → digits ignored
"Hello".isupper()        # False
"123".isupper()          # False  → no cased characters

### `islower()`
#True if all **cased** characters are lowercase.

"hello".islower()        # True
"hello123".islower()     # True
"Hello".islower()        # False

### `istitle()`
#True if string follows title-case rules (first letter of each word is uppercase, rest lowercase).

"Hello World".istitle()      # True
"Hello world".istitle()      # False
"HELLO WORLD".istitle()      # False
"Hello 123 World".istitle()  # True  → digits ignored

## 8. FORMAT METHODS
### `format(*args, **kwargs)`
#Fills placeholders `{}` with values.
# Positional
"Hello {} {}".format("Anil", "Kumar")        # 'Hello Anil Kumar'

# Indexed
"Hello {0} {1} {0}".format("Anil", "Kumar")  # 'Hello Anil Kumar Anil'

# Named
"Hello {name}".format(name="Anil")            # 'Hello Anil'

