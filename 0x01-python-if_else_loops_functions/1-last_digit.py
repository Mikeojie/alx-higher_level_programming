#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
if i < 0:
    i = -1 * i
    i = i % 10
else:
    i = i % 10

if i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i ==0:
    print(f"Last digit of {number} is {i} and is zero")
else:
    print(f"Last digit of {number} is {i} and is less than 5")
