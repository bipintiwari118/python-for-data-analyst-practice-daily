#Python For Data Analyst | Day 10 | Concept of Dictionary |

# A dictionary is a collection of key-value pairs which are ordered, changeable and indexed. It does not allow duplicate members.
# A dictionary is defined by having values between curly braces { }.
# Example of Dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

a={"id":101,"school":"Abc School","marks":[90,80,70],"result":True}
print(a)
print(type(a))

print(a["id"])


#lenth of dictionary
print("Length of my_dict:", len(my_dict))


#nested dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science"
    },
    "hobbies": ["reading", "traveling", "coding"],
    "lucky_numbers": (7, 14, 21)
}   


print("nested dict:",my_dict["education"]["degree"])


b=dict(name="Bob", age=25, city="Los Angeles")
b.update({"country":"USA"})
b.pop("city")
print(b)
print(type(b))
x=b.keys()
print(x)
print(b.values())

b["age"]=34

print(b)


#add new key-value pair to dictionary
b["profession"]="Data Analyst"
print(b)


#write a program for square of numbers using dictionary
squares = {}
for i in range(1, 16):
    squares[i] = i**2
    print(squares)
  

#write a program check if a key exists in a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
key_to_check = "age"
if key_to_check in my_dict:
    print(f"{key_to_check} exists in the dictionary.")
    
    
key={"name":"Alice","age":30,
     "city":"New York","a":5,"b":10}
user=input("Enter the key to check: ")

if user in key.keys():
    print("keys are present in the dictionary")
else:
    print("keys are not present in the dictionary")      