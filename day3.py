#Python For Data Analyst | Day 04 | Control Flow Statement 
# Control flow statements are used to control the execution of code based on certain conditions. They allow you to make decisions and repeat actions in your programs. Here are some commonly used control flow statements in Python:
# types of control flow statements
# 1. if statement: This statement is used to execute a block of code if a specified condition is true.
#2. else statement: This statement is used to execute a block of code if the condition in the if statement is false.
#3. elif statement: This statement is used to check multiple conditions after an if statement.
#4. for loop: This statement is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.
#5. while loop: This statement is used to execute a block of code repeatedly as long as a specified condition is true.
#6. break statement: This statement is used to exit a loop prematurely when a certain condition is met.
#7. continue statement: This statement is used to skip the current iteration of a loop and move on to the next iteration.  
#8. pass statement: This statement is used as a placeholder when a block of code is required syntactically but you don't want to execute any code.


#conditional statements
#if statement is used to execute a block of code if a specified condition is true. The syntax for an if statement is as follows:
# if condition:
#     # block of code to be executed if the condition is true
#syntax for if-else statement is as follows:
# if condition:
#     # block of code to be executed if the condition is true
# else:
#     # block of code to be executed if the condition is false
#syntax for if-elif-else statement is as follows:
# if condition1:
#     # block of code to be executed if condition1 is true
# elif condition2:
#     # block of code to be executed if condition2 is true
# else:
#     # block of code to be executed if both condition1 and condition2 are false

# conditional statements questions
# 1. Write a Python program that checks if a number is positive, negative, or zero.

num=float(input("Enter a number: "))
if num > 0:
    print("The number is positive.", num)
elif num < 0:
    print("The number is negative.", num)    
else:
    print("The number is zero.", num)



#2 Write a program to calculate the percentage of students in the subjects math,science,social,english and nepali.

name=str(input("Enter a student's name: "))
math=float(input("Enter the Math marks: "))
science=float(input("Enter the Science marks: "))
social=float(input("Enter the Social marks: "))
english=float(input("Enter the English marks: "))
nepali=float(input("Enter the Nepali marks: "))
total_marks=math+science+social+english+nepali
percentage=(total_marks/500)*100
print(f"{name}'s percentage is: {percentage:.2f}%")
if percentage >= 90:
    print( "The student have Grade: A")
elif percentage >= 80:
    print("The student have Grade: B")
elif percentage >= 70:
    print("The student have Grade: C")        
elif percentage >= 60:
    print("The student have Grade: D")
else:
    print("The student have Grade: F")



#3. Write a program to check if a year is a leap year or not.
# A leap year is defined as:
# - It is divisible by 4;
# - However, if it is divisible by 100, it must also be divisible by 400 to be a leap year.
#  Example: 2000 is a leap year because it is divisible by 4 and also divisible by 400. However, 1900 is not a leap year because it is divisible by 4 but not divisible by 400.
# 
# Example:
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")    



#4. Write a program to check if a number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")         