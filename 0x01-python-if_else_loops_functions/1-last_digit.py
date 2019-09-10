#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number1 = (number * -1) % 10
elif number >= 0:
    number1 = number % 10


if number1 == 0:
    print("last digit of {: d} is {} and is 0" .format(number, number1))

elif number1 > 5:
    print("last digit of {: d} is {} and is greater than 5"\
.format(number, number1))

elif number1 < 6:
    print("last digit of {: d} is {} and is less than 6 \
and not 0" .format(number, number1))
