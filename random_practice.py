"""
title: random_practice
author: Ahmed
date: 2019-06-12 09:53
"""

import random

name = input("Enter your name")

salary = int(input("Enter your salary"))

raise_per = random.randint(0, 100)

raise_amount = salary+((salary/100)*raise_per)

print(f"{name} and salary is {salary} ")

print(f"Your raise is {raise_per}% of ${salary} ")

print(f"{name} your new salary is {raise_amount}")
