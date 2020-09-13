# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:31:21 2020

@author: Ihsaan

Vacuum Cleaner Route

Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. The string will only 
contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...
"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

def vacuum_route(string):
    
    up = 0
    right = 0
    
    if len(string) == 0:
        return True
    
    else:
    
        for character in string:
            
            if character == 'R':
                right += 1
                
            elif character == 'L':
                right -= 1
                
            elif character == 'U':
                up += 1
                
            else:
                up -= 1
        
        if up == 0 and right == 0:
            return True
        
        else: 
            return False
            
    
print(vacuum_route('LR'))

print(vacuum_route("URURD"))

print(vacuum_route("RUULLDRD"))