# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:58:19 2020

@author: Ihsaan
"""

'''
Today's Byte is Reverse a String

ex: - cat, return tac
    - The Daily Byte, return etyB ylaD ehT

'''

String1= 'cat'

String2 = 'The Daily Byte'

def reverse_string(string):
    
    reversed_string = string[::-1]
    
    return reversed_string


def reverse_string2(string):
    
    reversed_string = ''
    
    for i in range(1,len(string)+1):
        
        reversed_string += string[len(string)-i]
        
    return reversed_string
    


print(reverse_string(String1))
print(reverse_string2(String2))