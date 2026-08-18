import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
#sqrt() is a function that gets the square root of a number.
#pow() is a function that raises a number to a given power.

print("The distance between the two points is:", round(distance, 2))

#Reflection
#I learned that using a library is more efficient and convinient compared to writing all of your calculations from scratch, because  it provides functions that make calculations easier and it helps save your time when writing a program, therefore being able to get it done with faster. 
#The sqrt() and pow() functions helped me calculate the square root and powers  of the numbers without me having to write in those functions myself which is quite efficient if you were to write a very long code.
#Without these functions, I would need to write additional lines of code to perform the calculations from scratch, which would take up more of my time.
