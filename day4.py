
# Python For Data Analyst | Day 04 | Concept of Loops |
# loops are used to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in Python:
# 1. For Loop: Used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.
# 2. While Loop: Used to execute a block of code as long as a specified condition is true.



#while Loop Example
# Initialize a variable

#example 1 : print numbers from 1 to 5 using while loop

i=1;
n=5;
while i<=n:
    print(i)
    i=i+1;


#example 2 : program multiplication table of a given number using while loop

num=int(input("Enter a number:"))
i=1;
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1;


#example 3: print hello students 50 times using while loop

i=1;
while i<=50:
    print("hello students")
    i=i+1;








#for Loop Example

#example 1: print numbers from 3 to 50 using for loop
for i in range(3,51):
    print(i);

#example 2: print even numbers from 1 to 100 using for loop
for i in range(1,101):
    if i%2==0:
        print(i);

#example 3: print odd numbers from 1 to 100 using for loop

for i in range(1,101):
    if i%2!=0:
        print(i);