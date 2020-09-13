# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:03:01 2020

@author: Ihsaan

Daily Byte #2 : Palidrome


Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical
characters. 

Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

Ex: Given the following strings...
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true

"""

def palindrome(string):
    
    leftptr = 0 #start of string
    rightptr = len(string) -1  #end of string
    
    while(leftptr < rightptr):
        
        while (leftptr < rightptr) and not(string[leftptr].isalnum()):
            
            leftptr += 1 #increment left ptr because character is not alphanumeric
            
        while (leftptr < rightptr) and not(string[rightptr].isalnum()):
            
            rightptr -= 1 # decrement right ptr because character is not alphanumeric
        
        if (leftptr < rightptr) and string[leftptr].lower() != string[rightptr].lower():
            
            return False    #if ever character for both pointers do not match return false
            
        else:
           
            leftptr += 1    #increment both pointer characters is a match/ is a palindrom so far
            rightptr -= 1       
    
    return True
            
            

print(palindrome('A man, a plan, a canal: Panama.'))
print(palindrome('A dog barks'))
print(palindrome('LEvel'))