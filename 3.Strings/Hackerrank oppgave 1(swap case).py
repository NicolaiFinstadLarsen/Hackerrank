# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:59:21 2020

@author: nicolai
"""

'''
def hello(s):
    
    balle=s.swapcase()
    
    print(balle)
hello(input())
'''

def swap_case(s):
    nystring = s.swapcase()
    s = nystring 
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



