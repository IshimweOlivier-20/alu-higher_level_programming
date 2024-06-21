#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_sign = "-" if number < 0 else ""
output_message = f"Last digit of {number} is {last_digit_sign}{last_digit} and is "
if last_digit > 5:
    print(output_message + "greater than 5")
elif last_digit == 0:
    print(output_message + "0")
else:
    print(output_message + "less than 6 and not 0")
