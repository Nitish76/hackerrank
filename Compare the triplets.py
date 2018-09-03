#!/bin/python3

import math
import os
import random
import re
import sys

# A function that compares Alice and Bob's rating and assigns them points accordingly.
# +1 point to the person with higher rating
# no points to both people if their ratings are the same
def solve(a, b):
    A=0; B=0
    for i in range(3):
        if a[i]>b[i]:
            A +=1
        elif b[i]>a[i]:
            B +=1
        else:
            A=A
            B=B
    return(A,B)

#input and output statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))  #Alice's ratings

    b = list(map(int, input().rstrip().split()))  # Bob's ratings

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
