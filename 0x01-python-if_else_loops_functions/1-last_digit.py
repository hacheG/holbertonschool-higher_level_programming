#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDig = number % -10
elif number >= 0:
    lastDig = number % 10


if lastDig == 0:
    print('Last digit of {: d} is {} and is 0' .format(number, lastDig))

elif lastDig > 5:
    print('Last digit of {: d} is {: d} and is greater than 5'\
.format(number, lastDig))

elif lastDig < 6:
    print('Last digit of {: d} is {: d} and is less than 6 \
and not 0' .format(number, lastDig))
