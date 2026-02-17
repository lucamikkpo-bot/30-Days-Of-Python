Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Enter base: 20
Enter height: 10
 The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


age = int(29)
height = float(1.75)
complex = complex(4, 3)

---
       
bbase = int(input("Enter base: "))
heighTr = int(input("Enter height: "))
area = float(0.5) * base * heighTr

print("The area of the triangle gives: ", area)

---

side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimeter = (side_a + side_b + side_c)
print("The primeter is: ", perimeter)

---
print("Calcule area and perimeter")
length = int(input("Introduce the length: "))
width = int(input("Introduce the width: "))
area = length * width
perimeter = int(2) * (length + width)
print("The area is: ", area)
print("The perimeter is: ", perimeter)

---
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

print("Length and width of a rectangle")
length = input("Introduce length: ")
width = input("Introduce width: ")
area = int(length) * int(width)
perimeter = 2 * (int(length) + int(width))

print("The Area is:", str(area) + " and Perimeter is:", str(perimeter))

---

import math # Puntos x1, y1 = 2, 2 x2, y2 = 6, 10 # Slope slope = (y2 - y1) / (x2 - x1) # Euclidean distance distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) print("Slope:", slope) print("Euclidean distance:", distance)

print(len("python"))
print(len("dragon"))

print("python" < "dragon")

if 'on' in "python" and 'on' in "dragon":
    print("It is")
if 'jargon' in "python" and "dragon":
    print("And jargo here")

python = len("python")
float(python)
str(python)
print(python)

a = 7 b = 3 floor_division = a // b 
print("Floor division:", floor_division) 
print("Comparison result:", floor_division == int(2.7))

if type('10') == type('10'):
    print("same")

if int(9.80) == int(10):
    print("same too")
else:
    print("no")

print("Welcome to pay calculator")
hours = int(input("Enter your hours: "))
rate = int(input("Enter you rate per hour: "))
earning = hours * rate

print("Your weekly earning is: ", earning)

years = int(input("Introduce tus años: "))
seconds_per_year = 365 * 24 * 60 * 60
max_years = 100
second_lived = years * seconds_per_year
print(second_lived)



print(" 1 1 1 1 1")
print(" 2 1 2 4 8")
print(" 3 1 3 9 27")
print(" 4 1 4 16 64")
print(" 5 1 5 25 125")


  
  


  
