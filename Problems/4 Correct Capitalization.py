# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:13:35 2020

@author: Ihsaan

Correct Capitalization


Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization if all letters are capitalized, 
no letters are capitalized, or only the first letter is capitalized.

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true

"""

def correct_Capitalization(string):
    upper_case_count = 0
    upper_case_index = None
    for i in range(len(string)):
        if string[i] == string[i].upper():
            upper_case_count += 1
            
            if  upper_case_index == None :
                
                upper_case_index = i
            
    if upper_case_count == 0 or (upper_case_count == 1 and upper_case_index == 0) or (upper_case_count == len(string)):
        
        return True
    
    else:
        return False
    
    
    
print(correct_Capitalization("USA"))
print(correct_Capitalization("Calvin"))
print(correct_Capitalization("compUter"))
print(correct_Capitalization("coding"))
