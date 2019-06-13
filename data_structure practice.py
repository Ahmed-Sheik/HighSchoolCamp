"""
title: data_structure practice
author: Ahmed
date: 2019-06-13 11:32
"""

import random

def shake_ball():

    options = ["Yes definitely", "As I see it", "yes", "Ask again later", "Cannot predict now", "Don't count on it", "Very doubtful,You wish", "Maybe another time", "Ofcourse!"]
    input("Enter a question: ")
    return random.choice(options)



 print(shake_ball())
