#Python For Data Analyst | Day 08 | Intro to Tuples- Python
# A tuple is a collection of items which are ordered and unchangeable. It allows duplicate members.
# A tuple is defined by having values between parentheses ( ).
# Example of Tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)



#mixed data types in tuple
my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)


a=("bipin",[1,2,3],(4,5,6))
print(a)
print(type(a))

b=("bipin")
print(type(b))

c=("bipin",)
print(type(c))


#tuple constructors
my_tuple = tuple((1, 2, 3, 4, 5))
print(my_tuple)



#indexing and slicing of tuple
print("First item:", my_tuple[0])  # Accessing the first item
print("Last item:", my_tuple[-1])  # Accessing the last item
print("Slice:", my_tuple[1:4])  # Slicing the tuple


t=(1, 2, 3, 4, 5)
print(t[::])
print(t[::2])
print(t[::-1])


t1=(1, 2, 3, 4, 5,3,4,5,7,8,9,0)



#append() method is not available for tuple because tuples are immutable, which means that once a tuple is created, its elements cannot be changed or modified. Therefore, you cannot add new elements to a tuple using the append() method or any other method that modifies the contents of the tuple.    


y=(110,120,130,140,150,160,170,180,190,200)
y=list(y)
print(y)
y.append(210)
print(y)
y=tuple(y)
print(y)


#loop through tuple
for item in my_tuple:
    print(item)
    
    
x=("ram","shyam","hari","gita")

for i in x:
    print(i)
    
    
    
#join two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3=("bipin","shyam","hari")
joined_tuple = tuple1 + tuple2 + tuple3
print(joined_tuple)  


#multiply tuple
tuple1 = (1, 2, 3)
multiplied_tuple = tuple1 * 3
print(multiplied_tuple)

tuple2=("bipin","shyam","hari")
multiplied_tuple2=tuple2*3      
print(multiplied_tuple2)
print(tuple2*2)

print(len(tuple1))




#write a program to take 5 numbers from user and store them in a tuple.

numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers_tuple = tuple(numbers)
print("The tuple of numbers is:", numbers_tuple)