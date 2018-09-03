#!/bin/python3

import os
import sys


# A function to find the sume of elements of an array.
# The elements are integers that are possibly very large
# For languages like C++ this function would require the use of long int

def aVeryBigSum(n, ar):
    total = 0
    for i in range(n):
        total += ar[i]
    print(total)
    return(total)
    
# Input and output statements

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
