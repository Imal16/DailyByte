# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:02:02 2020

@author: Ihsaan

Valid Palindrome with removal

Given a string and the ability to delete at most one character, return whether or not it can form a palindrome. 
Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 

Ex: Given the following strings...
"abcba", return true
"foobof", return true (remove the first 'o', the second 'o', or 'b')
"abccab", return false
"vapppoav", return true
"""

def valid_palidrome_removal(string):
    #two ways of solving, 1) create every sigle permutation by removing one character and check if its a palindrome
    #2) check palindrome, if not try removing left character and check if palin, try removing right char and check if palin
    leftptr = 0
    rightptr = len(string) - 1
    
    while leftptr < rightptr:
        
        if string[leftptr] != string[rightptr]: #rightptr character can be removed or left ptr character can be removed
            return palindrome(string, leftptr+1, rightptr) or palindrome(string, leftptr, rightptr -1)
        

        
        rightptr -= 1
        leftptr += 1
    
    return True

def palindrome(string, leftindex, rightindex):
    
    while leftindex < rightindex:
        
        if string[leftindex] != string[rightindex]:
            return False
        
        leftindex += 1
        rightindex -= 1
    
    return True


print(valid_palidrome_removal('abcba'))
print(valid_palidrome_removal('foobof'))
print(valid_palidrome_removal('abccab'))
print(valid_palidrome_removal('vaopppav'))