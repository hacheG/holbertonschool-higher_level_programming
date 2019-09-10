#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
str2 = "and is less than 6"

if number < 0:
    lastDig = number % -10
elif number >= 0:
    lastDig = number % 10


if lastDig == 0:
    print('{} {} is {} and is 0'.format(str, number, lastDig))

elif lastDig > 5:
    print('{} {} is {} and is greater than 5'.format(str, number, lastDig))

elif lastDig < 6:
    print('{} {} is {} {} and not 0'.format(str, number, lastDig, str2))
