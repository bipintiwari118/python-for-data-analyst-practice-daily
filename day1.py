#  Variables and operators in python

# 1. Variables
# A variable is a container for storing data values. In Python, you can create a variable by simply assigning a value to it.
# Example:
x = 5
print(x);
y = "Hello, World!"
print(y);



# 2. Data Types
# Python has several built-in data types, including: 
# - int: for integers
# - float: for floating-point numbers
# - str: for strings
# - bool: for boolean values (True or False)
# Example:
a = 10          # int   
b = 3.14        # float
c = "Python"    # str
d = True        # bool
e=[1,2,3,4,5,6,7,8,9,10] # list
f=(1,2,3,4,5,6,7,8,9,10) # tuple
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))




# 3. Operators
# Python supports various operators for performing operations on variables and values. Some common operators include:
# - Arithmetic Operators: +, -, *, /, %, **, //
# - Comparison Operators: ==, !=, >, <, >=, <=
# - Logical Operators: and, or, not

# Example:
num1 = 10
num2 = 5
# Arithmetic Operators
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication   
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus
print(num1 ** num2) # Exponentiation
print(num1 // num2) # Floor Division
# Comparison Operators
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to
print(num1 > num2)   # Greater than
print(num1 < num2)   # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to
# Logical Operators
is_sunny = True
is_warm = False
print(is_sunny and is_warm)  # Logical AND
print(is_sunny or is_warm)   # Logical OR
print(not is_sunny)          # Logical NOT

