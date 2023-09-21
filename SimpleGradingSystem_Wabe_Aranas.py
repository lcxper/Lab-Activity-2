# Ask the student  details
print("Student's Full Name: ")
name = input()
print("ID No.: ")
id_number = input()
print("Course: ")
course = input()
print("Section: ")
section = input()


#ask the student of their grades

number1 = eval(input("Enter First Quarter Grade: "))
number2 = eval(input("Enter Second Quarter Grade: "))
number3 = eval(input("Enter Third Quarter Grade: "))
number4 = eval(input("Enter Fourth Quarter Grade: "))

#Compute the average of 4 Quarter Grades

average = (number1 + number2 + number3 + number4) / 4

#display result

print("The average grade of", number1, number2, number3, number4, "is", average)

print("Full Name:" + name)
print("ID No." + id_number)
print("Course:" + course)
print("Section:" + section)

print("1st Quarter Grade:", number1)
print("2nd Quarter Grade:", number2)
print("3rd Quarter Grade:", number3)
print("4th Quarter Grade:", number4)
print("Your Average Grade is:", average)