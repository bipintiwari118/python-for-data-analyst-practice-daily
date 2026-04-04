# Python For Data Analyst | Day 03 | In-Built Functions of Python 
#  built in functions are functions that are already defined in Python and can be used without the need for importing any additional libraries. These functions perform various tasks such as mathematical operations, string manipulation, type conversion, and more. Here are some commonly used built-in functions in Python:
# 1. print(): This function is used to display output on the console.
# Example:
print("Hello, World!")
# 2. len(): This function returns the length of an object, such as a string, list, or tuple.
# Example:
my_string = "Python"
print(len(my_string))  # Output: 6
# 3. type(): This function returns the type of an object.
# Example:
my_variable = 42
print(type(my_variable))  # Output: <class 'int'>
# 4. int(), float(), str(): These functions are used for type conversion.
# Example:
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(num_int)  # Output: 123
num_float = float(num_str)  # Convert string to float
print(num_float)  # Output: 123.0
# 5. range(): This function generates a sequence of numbers.
# Example:
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# 6. sum(): This function returns the sum of all items in an iterable.
# Example:
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15
# 7. max() and min(): These functions return the maximum and minimum values from an iterable, respectively.
# Example:
values = [10, 20, 5, 15]
print(max(values))  # Output: 20
print(min(values))  # Output: 5


# abs() : This function returns the absolute value of a number.
# Example:
num = -5
print(abs(num))  # Output: 5
num2=3.14
print(abs(num2)) # Output: 3.14
num3=-3.14
print(abs(num3)) # Output: 3.14
num4=-5+3j
print(abs(num4)) # Output: 5.830951894845301



#bin() : This function converts an integer to a binary string.
# Example:
num = 10
print(bin(num))  # Output: '0b1010'

num2=5.56
print(bin(int(num2))) # Output: '0b101'



#bytes() : This function converts a string to bytes.
# Example:  
my_string = "Hello"
my_bytes = bytes(my_string, 'utf-8')
print(my_bytes)  # Output: b'Hello'

num = 123
num_bytes = bytes(num)
print(num_bytes) 





#char() : This function returns the character that corresponds to a given ASCII value.
# Example:
ascii_value = 65
print(chr(ascii_value))  # Output: 'A'

num = 97
print(chr(num))  # Output: 'a'





#complex() : This function creates a complex number from real and imaginary parts.
# Example:
real_part = 3
imaginary_part = 4
complex_num = complex(real_part, imaginary_part)
print(complex_num)  # Output: (3+4j)


num1 = 2
num2 = 3
complex_num2 = complex(num1, num2)
print(complex_num2)  # Output: (2+3j)






#float() : This function converts a number or a string to a floating-point number.
# Example:
num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14

num_int = 10
num_float2 = float(num_int)
print(num_float2)  # Output: 10.0


#int() : This function converts a number or a string to an integer.
# Example:
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

num_float = 3.14
num_int2 = int(num_float)
print(num_int2)  # Output: 3

print(type(num_str), type(num_int));





#str() : This function converts an object to a string.
# Example:
num = 123
num_str = str(num)
print(num_str)  # Output: '123'
print(type(num_str))  # Output: <class 'str'>

num_float = 3.14
num_str2 = str(num_float)
print(num_str2)  # Output: '3.14'
print(type(num_str2))  # Output: <class 'str'>





#help() : This function provides information about a function, module, or object.
# Example:
help(print)  # This will display the documentation for the print() function
help(len)    # This will display the documentation for the len() function
help(int)    # This will display the documentation for the int() function







#input() : This function allows the user to input data from the console.
# Example:
name = input("Enter your name: ")
print(name)  
age = input("Enter your age: ")
print(age)



#what is typecasting?
# Typecasting is the process of converting a variable from one data type to another. In Python, you can use built-in functions like int(), float(), str(), etc., to perform typecasting. This is useful when you want to ensure that a variable is of a specific type before performing operations on it.
# Example:
num_str = "123"
num_int = int(num_str)  # Typecasting string to integer
print(num_int)  # Output: 123




