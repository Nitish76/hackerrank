#!/bin/python3

import math
import os
import random
import re
import sys

# Calculate the fractions of an arry's elements that are positive, negative, and are zeros
def plusMinus(arr):
    neg = 0; pos = 0; zer = 0
    # loop to calculate number of positive, negative and zero elements
    for i in arr:
        if i==0:
            zer += 1
        elif i>0:
            pos += 1
        else:
            neg +=1
    neg =neg/float(n); pos = pos/float(n); zer = zer/float(n)       # fraction calculation
    
    # Output commands
    print(pos)
    print(neg)
    print(zer)   
    return()

# Input commands
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
