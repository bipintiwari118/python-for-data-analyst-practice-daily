#Python For Data Analyst | Day 07 | Concept of List- Python |

# List is a collection of items which are ordered and changeable. It allows duplicate members.
# List is defined by having values between square brackets [ ].
# Example of List
my_list = [1, 2, 3, 4, 5]
print(my_list)
# List can contain different types of data
my_list = [1, "Hello", 3.14, True]
print(my_list)

print("Length of my_list:", len(my_list))

#accessing list items
print("First item:", my_list[0])  # Accessing the first item
print("Last item:", my_list[-1])  # Accessing the last item
print("Items from index 1 to 3:", my_list[1:4])  # Accessing items from index 1 to 3


#slicing of the list
print("Items from index 0 to 2:", my_list[0:3])


#change the value of list
my_list[1] = "World"
print("Updated list:", my_list)


a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[5]=100;
print(a);

a[2:5]=[200,300,400]
print(a)


a.append(500);
print(a)

a.remove(100);
print(a)


#insert() method is used to insert an item at a specified index in the list. It takes two parameters: the index where the item should be inserted and the item itself.
a.insert(2, 600);
print(a)



#question 1: print sum of number like 1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5

numbers = [1, 2, 3, 4, 5]
cumulative_sum = 0
for num in numbers:
    cumulative_sum += num
    print(cumulative_sum)
    
    
a=0
for i in range(len(numbers)):
    a=a+numbers[i]
    i=i+1
    print(a)
    
for i in range(len(numbers)):
    a=a*numbers[i]
    i=i+1
    print(a)