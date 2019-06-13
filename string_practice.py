"""
title: string_practice
author: Ahmed
date: 2019-06-11 13:45
"""

#print(answer.lower()in "qwertyuiopasdfghjklzxcvbnm")

#short = input("Enter a letter")

#short = short.lower().replace("and", "&")
#short = short.lower().replace("too", "2")
#short = short.lower().replace("you", "U")
#short = short.lower().replace("for", "4")
#short = short.lower().replace("a", "")
#short = short.lower().replace("e", "")
#short = short.lower().replace("i", "")
#short = short.lower().replace("o","")
#short = short.lower().replace("u",)



phrase =input("Enter a phrase: ")

phrase =phrase.replace("'", "").replace(" ", "").replace("!", "").replace(".", "").replace("?", "").replace("&", "")

print(phrase)

def removing(check):
    #check = check.lower().replace(" ", "")
     #return check

def palindrome(check):
    check = removing(check)
    return check == check [::-1]
print(palindrome("Computer"))