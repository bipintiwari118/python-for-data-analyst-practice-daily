#User defined function

def hello():
    print("Hello Students")

hello() #function call



#task 1: student result name,math,science,social for user input and after result school contact details on every result

def contact():
    print("Contact details of school:")
    print("Kathmandu Valley School")
    print("kathmandu, Nepal ")
    print("Phone: 01-1234567")
    print("Email: info@kathmanduvalleyschool.edu.np")


for i in range(4):
    name=input("Enter student name:")
    math=int(input("Enter math marks:"))
    science=int(input("Enter science marks:"))
    social=int(input("Enter social marks:"))
    total=math+science+social
    percentage=total/3
    print("Student Name:",name)
    print("Total Marks:",total)
    print("Percentage:",percentage)
    contact()    




# Arguments and Parameters in Function: 
# 
# Arguments are the values that are passed to a function when it is called, while parameters are the variables that are defined in the function to receive those values.

def greet(name):
    print("Hello",name)

fname=input("Enter your name:")
greet(fname)





#task 2 : Write a program to calculate electricity bill based on the following criteria:
# Units consumed    Rate per unit
# 0-500            Rs. 15
# 501-700            Rs. 20
# 701-1000          Rs. 25
# Above 1000         Rs. 30
#last date to submit bill 20th June 2026
#users details name, units consumed, bill amount, contact details of electricity office


   

name = input("Enter User name: ")
units = int(input("Enter Units consumed: "))



def electricity_bill(units):
    if units <= 500:
        bill_amount = units * 15
        details(bill_amount)
        
    elif units>500 and  units <= 700:
        bill_amount = units * 20
        details(bill_amount)
        
    elif units <= 1000:
        bill_amount =  units * 25
        details(bill_amount)
        
    else:
        bill_amount =  units * 30 
        details(bill_amount)
        

def details(bill_amount):
    print("User Name:", name)
    print("Units Consumed:", units)
    print("Bill Amount:", bill_amount)
    print("Contact details of electricity office:")
    print("Electricity Office")
    print("Kathmandu, Nepal")
    print("Phone: 01-7654321")
    print("Email:infoelectrcity@gmail.com")
    print("Note: Last date to submit bill is 20th June 2026 otherwise a late fee will be applied Rs. 1000.")
    
electricity_bill(units);   
  
