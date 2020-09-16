# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:10:27 2020

@author: Ihsaan

Longest Common Prefix


Given an array of strings, return the longest common prefix that is shared amongst all strings. 
Note: you may assume all strings only contain lowercase alphabetical characters. 

Ex: Given the following arrays...
["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"


"""

def longest_common_prefix(string_list):
    #iterate though the characters of the first string, next iterate through each word
#so we compare if the index of characters if they are in the same location to all the strings -> same prefix
# time = O(n) *O(m) when n is all the characters in the first word and m is the number of words in the list
    lcp = ''
    
    if len(string_list) == 0:
        return lcp
    

    index =0
    
    for characters in string_list[0]:
        for i in range(1,len(string_list)):
           
            if index >= len(string_list[i]) or characters != string_list[i][index]:
                return lcp
        lcp += characters
        index += 1
    
    return lcp #if the first word is the shortest, loop will end without other conditions hitting

        


print(longest_common_prefix(["colorado", "color", "cold"]))
print(longest_common_prefix(["a", "b", "c"]))
print(longest_common_prefix(["spot", "spotty", "spotted"]))        
        
    