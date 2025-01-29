import math

user_input = input("What is the distance or weight you would like to convert? ")
num, unit = user_input.split(" ", 1)

if "." in num:
    num = float(num)
else:
    num = int(num)

if unit == "in":
    converted = num * 2.54
    converted = round(converted, 2)
    print(f"{num} inches is around {converted} centimeters.")
elif unit == "cm":
    converted = num / 2.54
    converted = round(converted, 2)
    print(f"{num} centimeters is around {converted} inches.")
elif unit == "yd":
    converted = num * 0.9144
    converted = round(converted, 2)
    print(f"{num} yards is around {converted} meters.")
elif unit == "m":
    converted = num / 0.9144
    converted = round(converted, 2)
    print(f"{num} meters is around {converted} yards.")
elif unit == "oz":
    converted = num * 28.3495
    converted = round(converted, 2)
    print(f"{num} ounces is around {converted} grams.")
elif unit == "g":
    converted = num / 28.3495
    converted = round(converted, 2)
    print(f"{num} grams is around {converted} ounces.")
elif unit == "lb":
    converted = num * 0.453592
    converted = round(converted, 2)
    print(f"{num} pounds is around {converted} kilograms.")
elif unit == "kg":
    converted = num / 0.453592
    converted = round(converted, 2)
    print(f"{num} kilograms is around {converted} pounds.")
else:
    print("Invalid unit, please try again.")