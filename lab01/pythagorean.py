import math

number1 = input("What is the first number? ")
number2 = input("And the second? ")

if "." in number1:
    number1 = float(number1)
else:
    number1 = int(number1)

if "." in number2:
    number2 = float(number2)
else:
    number2 = int(number2)

hypotenuse = math.sqrt(number1**2 + number2**2)
rounded_answer = round(hypotenuse, 2)
print(f"The hypotenuse is around {rounded_answer}.")