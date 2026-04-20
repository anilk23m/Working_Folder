#A set is an unordered collection of unique elements.
#No index, no position - you can not do s[0]
#Duplicate element not allowed - duplicates are automatically removed
#Mutable - We can add/remove elements
#No index/slicing - cant access by position
#Iterable - Can loop through with for
#Only immutable elements - Can contain int, str, tuple, bool - Not list, dict, set

#Creating Set -
s = {1,2,3,4}
print(s)
print(type(s))

s2 = set([1,2,3,4,5])
print(s2)

s3 = set("hello")
print(s3)

s4 = set((10,20,30,40))
print(s4)

empty_set = set()
empty_dict = {}

print(type(empty_set))
print(type(empty_dict))

#add() - add single element
s5 = {1,2,2,3,3,3,4,5}
print(s5)
s5.add(6)
print(s5)

#update() - add multiple elements
s6 = {1,2}
s6.update([3,4,5,6,5,6])
print(s6)

#remove() - remove element (raise error if value missing)
# s6.remove(6)
# print(s6)
# s6.remove(99)

#discard() - Remove element (no error if value missing) - ignore
s7 = {1,2,3}
s7.discard(3)
print(s7)
s7.discard(4)
print(s7)

#remove and return an arbitrary element - unpredictable
s = {10,20,30,40,5}
item = s.pop()
print(item)

empty = empty_set.pop()
print(empty)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#union - | or union() -
print(A|B)  #union() - all elements from both
print(A&B)  #intersection() - common elements only
print(A^B)  #symetric difference() - in either A or B but not both
print(A-B)  #difference() - in A but not in B

