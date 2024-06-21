#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_sign = "-" if number < 0 else ""
if last_digit_sign == "":
    print(f"Last digit of {number} is {last_digit} and is ", end="")
else:
    print(f"Last digit of {number} is {last_digit_sign}{last_digit} and is ", end="")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
