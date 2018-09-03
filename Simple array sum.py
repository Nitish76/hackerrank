#!/bin/python3

import os
import sys

#
# Function to compute sum of elements of an array
#
def simpleArraySum(ar):
    total = 0 
    for i in range(ar_count):
        total += ar[i]
    return(total)
        
# input and output statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
