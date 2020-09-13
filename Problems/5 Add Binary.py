# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:42:43 2020

@author: Ihsaan

Add Binary



Given two binary strings (strings containing only 1s and 0s) return their sum 
(also as a binary string). 
Note: neither binary string will contain leading 0s unless the string itself is 0 

Ex: Given the following binary strings...
"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
'1010' + '1011', return '10101'
"""

def add_binary(string1, string2):
    '''
    

    Parameters
    ----------
    string1 : TYPE
        DESCRIPTION.
    string2 : TYPE
        DESCRIPTION.

    Returns
    -------
    reversed_binary_Sum : TYPE
        DESCRIPTION:
            This is more of  a walk through on how to calculate it, with python, 
            there are built in funcitons that will make the code simpler
    '''
    
    binary_sum=''
    
    i = len(string1) - 1
    j = len(string2) - 1
    carry = 0
    
    while i > 0 or j > 0: #iterate backwards os you add the lest significant digit first
        
        sum_of_string = carry
        sum_of_string += ord(string1[i]) - ord('0')
        sum_of_string += ord(string2[j]) - ord('0')
        binary_sum += str(sum_of_string % 2) # 1+1 = 10 in binary, thus the mod 2 gets the 0
        carry = sum_of_string / 2  # 1+1 = 2 is standard numeric. but in binary its 10, this will get the 1 in 10 aka the carry digit
                
        #because append, appends to the end of a string, we have to reverse the string
        
    reversed_binary_Sum = ''
    
    for i in range(1,len(binary_sum)+1):
        
        reversed_binary_Sum.append(binary_sum[len(binary_sum)]-i)
    
    return reversed_binary_Sum      

def add_binary2(string1,string2):
    output = int(string1,2) + int(string2,2)
    
    return'{:b}'.format(output)


print(add_binary2('100','1'))
print(add_binary2('11','1'))
print(add_binary2('1','0'))    
print(add_binary2('1010','1011'))    
    