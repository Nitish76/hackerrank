#!/bin/python3

import math
import os
import random
import re
import sys

''' Camel case is the concatenation of one or more english words such that
    the first word is all lower case and the consequent words have their
    first letter as upper case and rest as lower case'''
# The function below counts the number of words given a string(s) in Camel case
# 1<= s <= 10.0E+5

def camelcase(s):
    count = 0
    for i in s:
        if i.isupper():
            count +=1
    return(count+1)
        
            
# Input and output statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
