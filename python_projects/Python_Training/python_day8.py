A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}
D = {7, 8, 9}

print(A.issubset(B))   # True  → all of A is inside B
print(A <= B)           # True  → operator version

print(A < B)            # True  → proper subset (A is inside B and not equal)
print(A < C)            # False → A equals C, so not a proper subset

print(B.issuperset(A))  # True  → B contains everything in A
print(B >= A)            # True  → operator version

print(A.isdisjoint(D))  # True  → A and D share nothing - no common element
print(A.isdisjoint(B))  # False → they share {1, 2, 3}


s = {"Python", "Selenium", "Playwright"}

for tool in s:
    print(tool)
# Order is NOT guaranteed

print("Python" in s)

# Squares of numbers 1-5
squares = {x**2 for x in range(1, 6)}
print(squares)  # {1, 4, 9, 16, 25}

# Extract unique first letters
names = ["Anil", "Amit", "Ravi", "Rahul", "Priya"]
initials = {name[0] for name in names}
print(initials)  # {'A', 'R', 'P'}

# Filter even numbers
nums = {x for x in range(1, 11) if x % 2 == 0}
print(nums)  # {2, 4, 6, 8, 10}

square_dict = {x:x**2 for x in range(1, 6)}
print(square_dict)

s = {1,2,3,4}
s2 = s.copy()
print(id(s))
print(id(s2))
s2.add(5)
print(s2)
print(s)

