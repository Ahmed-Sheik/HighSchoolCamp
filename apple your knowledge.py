"""
title: apple your knowledge
author: Ahmed
date: 2019-06-13 13:42
"""

nums = [89,73,90,41]

for i in nums:
    print(i)

for x in range (5, 15):
    print(x)

for o in range (100, 210, 10):
    print(o)

for t in range (80, 31, -8):
    print(t)

for k in range (3):
    print("alright")

num = 10

while num > 0:
    print(num, end="-")
    num -= 1

i_input = int(input("Enter a number greater than 0: "))

while i_input < 0:
    print("Waiting")
    i_input = int(input("Enter a number greater than 0: "))

print("Thank you for entering a number!")

first = int(input("Enter a first number: "))
second = int(input("Enter a second number: "))

while second < first:
    second = int(input("Invalid response. Enter a second number: "))

while first < second:
    print(first)
    first += 1

x = input ("Enter response ('Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'):")

while x not in ['Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO']


