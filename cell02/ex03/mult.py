#!/bin/python3
first_number = int(input("Enter the first number:"))
seconds_number = int(input("Enter the second number:"))
result = first_number * seconds_number
print(first_number, "x" , seconds_number, "=",result)
if result > 0 :
    print("This result is positive.")
else :
    print("This result is negative.")
