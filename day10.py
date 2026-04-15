#Python For Data Analyst | Day 11 | Intro to SETS in Python
# A set is a collection of unique elements which are unordered and unindexed. It is defined by having values between curly braces { }.

# Example of Set
my_set = {1, 2, 3, 4, 5}
print(my_set)
# Sets do not allow duplicate members
my_set = {1, 2, 3, 4, 5, 5, 5}
print(my_set)

# Sets are unordered, so you cannot access items in a set by referring to an index or a key.
# However, you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
    
    

# Check if a value is in the set
print(3 in my_set)  # Output: True

# Add an item to a set
my_set.add(6)
print(my_set)


animal={"cat","dog","rabbit"}
print(animal)
print(type(animal))


a={"apple","banana","cherry"}

print('banana' in a)
a.add("orange")
print(a)

a.remove("banana")
print(a)

b={"grape","melon","kiwi","apple"}
a.update(b)
print(a)


c=a.union(b)
print(c)

d=a.intersection(b)
print(d)

#write a program to find max and min number in a set
numbers = {5, 10, 15, 20, 25}
max_number = max(numbers)
min_number = min(numbers)
print("Max number:", max_number)
print("Min number:", min_number)