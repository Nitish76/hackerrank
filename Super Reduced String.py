#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the super_reduced_string function below.
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
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
