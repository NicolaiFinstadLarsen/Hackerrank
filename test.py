# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:54:12 2020

@author: nicolai
"""

def smaller_num(x,y):

    if x>y:
        number= y
    else:
        number= x
    return number


x = input("Enter first number:-")

y = input("Enter second number:-")

smaller = smaller_num(x,y)

print("The smaller number between " +  str(x) + " and " + str(y) + " is " + str(smaller))