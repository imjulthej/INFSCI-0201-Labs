import math

radius = input("What is the radius of your circle? ")

if radius.isdigit():
    if "." in radius:
        radius = float(radius)
    else:
        radius = int(radius)
else:
    while radius.isdigit() == False:
        print("Invalid input, please try again.")
        radius = input("What is the radius of your circle? ")

area = math.pi * radius**2
perimeter = 2 * math.pi * radius

rounded_area = round(area, 2)
rounded_perimeter = round(perimeter, 2)

print(f"The area of a circle with a radius of {radius} your circle is {rounded_area} and the perimeter is {rounded_perimeter}.")