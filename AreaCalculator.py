import math
import random
print("=====================================")
print("         Area Calculator 📐         ")
print("=====================================")

print(f"{1}) Triangle   {5}) Parallelogram")
print(f"{2}) Rectangle  {6}) Trapezoid")
print(f"{3}) Square     {7}) Rhombus")
print(f"{4}) Circle     {8}) Equilateral Triangle")
print("=====================================")



shape = int(input("What shape would you like to calculate: "))
print("=====================================")
length = 0
width = 0
height = 0
base = 0
side = 0
radius = 0
base1 = 0 
base2 = 0
diagonal1 = 0
diagonal2 = 0
area = 0

response = [
"Oops! That number\'s not on the list.",
"Want to pick one from the ones showing?",
"That number isn\'t displayed.",
"Please select one from the list.",
"Could you pick a number from those shown?",
"That number isn\'t part of the options.",
"Please choose one of the 8 numbers on the screen.",
"Take another look and pick one from the ones shown."
]
random_response = random.choice(response)
while shape > 8:
  print("=====================================")
  print(random_response)
  print("=====================================")
  shape = int(input("What shape would you like to calculate: "))
  print("=====================================")
if shape == 1:
  base = float(input("Base: "))
  height = float(input("Height: "))
  area = 1/2 * base * height
  print("Area of the triangle: ",area)
elif shape == 2:
  length = float(input("Length: "))
  width = float(input("Width: "))
  area = length * width
  print("Area of the Rectangle: ",area)
elif shape == 3:
  side = float(input("Side: "))
  area = side * side
  print("Area of the Square: ",area)
elif shape == 4:
  radius = float(input("Radius: "))
  area = math.pi * radius
  print("Area of the Circle: ",area)
elif shape == 5:
  base = float(input("Base: "))
  height = float(input("Height: "))
  area = base * height
  print("Area of the Parallelogram: ",area)
elif shape == 6:
  base1 = float(input("Base 1: "))
  base2 = float(input("Base 2: "))
  height = float(input("Height: "))
  area = 1/2 * (base1 + base2) * height
  print("Area of the Trapezoid: ",area)
elif shape == 7:
  diagonal1 = float(input("First Diagonal: "))
  diagonal2 = float(input("Second Diagonal: "))
  area = 1/2 * diagonal1 * diagonal2
  print("Area of the Rhombus: ",area)
elif shape == 8:
  side = float(input("Side: "))
  area = 3 ** 0.5 * 1/4 * side * side
  print("Area of the Rectangle: ",area)
else:
  print(random_response)
  shape = int(input("What shape would you like to calculate: "))

