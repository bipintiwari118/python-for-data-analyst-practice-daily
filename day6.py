#Python For Data Analyst | Day 06 | Introduction to Strings |
#String is a sequence of characters. It is a data type that is used to represent text. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").
#Creating a string
string1 = 'Hello, World!'
print(string1)

print(type(string1))

#String concatenation
string2 = 'Python is great.'
string3 = 'I love programming.'
concatenated_string = string2 + ' ' + string3
print(concatenated_string)



#indexing and slicing
w = 'Data Science'
print(w[0])  # Output: 'D'
print(w[5])  # Output: 'S'
print(w[4])
print(w[-2])

s='Hello, Students of Data Science'
print(s[7:19])

print(s[0:24:2])

print(len(s)) #space is also counted as a character


#some string methods
#1. upper() - converts all characters in a string to uppercase
s1 = 'hello, world!'
print(s1.upper())  # Output: 'HELLO, WORLD!'

#2. lower() - converts all characters in a string to lowercase
s2 = 'HELLO, WORLD!'
print(s2.lower())  # Output: 'hello, world!'

#3. title() - converts the first character of each word to uppercase and the rest to lowercase
s3 = 'hello, world!'
print(s3.title())  # Output: 'Hello, World!'

#4. strip() - removes leading and trailing whitespace from a string
s4 = '                          Hello, World!                      '
print(s4.strip())  # Output: 'Hello, World!'


#5. replace() - replaces all occurrences of a specified substring with another substring
s5 = 'Hello, World! Hello, Python!'
print(s5.replace('H', 'B'))  # Output: 'Bi, World! Bi, Python!'
print(s5.replace('Hello', 'Hi'))  # Output: 'Hi, World! Hi, Python!'



#6. split() - splits a string into a list of substrings based on a specified delimiter
s6 = 'Hello, World! Hello, Python!'
print(s6.split())  # Output: ['Hello,', 'World!', 'Hello,', 'Python!']
print(s6.split(', '))  # Output: ['Hello', 'World!', 'Hello', 'Python!']

#7. find() - returns the index of the first occurrence of a specified substring in a string
s7 = 'Hello, World! Hello, Python!'
print(s7.find('World'))  # Output: 7
print(s7.find('Python'))  # Output: 20
print(s7.find('W'))


#8. count() - returns the number of occurrences of a specified substring in a string
s8 = 'Hello, World! Hello, Python!'
print(s8.count('Hello'))  # Output: 2
print(s8.count('o'))  # Output: 4


#9. join() - concatenates a list of strings into a single string, using a specified separator
list_of_strings = ['Hello', 'World', 'Python']
separator = ' '
joined_string = separator.join(list_of_strings)
print(joined_string)  # Output: 'Hello World Python' 