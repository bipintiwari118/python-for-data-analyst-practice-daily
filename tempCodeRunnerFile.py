name=input("Enter a student's name: ")
math=float(input("Enter the marks in Math: "))
science=float(input("Enter the marks in Science: "))
social=float(input("Enter the marks in Social: "))
english=float(input("Enter the marks in English: "))
nepali=float(input("Enter the marks in Nepali: "))
total_marks=math+science+social+english+nepali
percentage=(total_marks/500)*100
print(f"{name}'s percentage is: {percentage:.2f}%")