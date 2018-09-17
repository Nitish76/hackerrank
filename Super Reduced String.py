#!/bin/python3

import math
import os
import random
import re
import sys
''' This program reduces a given string(s) to its shortest length by doing a series of operations. 
    In each operation a pair of adjacent lowercase letters that match are deleted. 
    This operation is repeated until there none of the adjacent letters are matching or the string becomes empty.'''
#   1<= s <= 100

# This function returns the super reduced string or 'Empty String' if the string is empty
def super_reduced_string(s):
    l = list(s)
    d = False; i = 0
    while d==False:
        if l[i]!=l[i+1]:
            i+=1
        else:
            l1 = l[:i]
            l2 = l[i+2:]
            l = l1+l2              
            if i>0:
                i -= 1
            else:
               i = 0
        if len(l)-1==i:
            d=True
            return(''.join(l))
        if len(l)==0:
            d=True
            return('Empty String')
            
        
# Input and Output statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
