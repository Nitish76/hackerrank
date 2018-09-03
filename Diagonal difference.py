#!/bin/python3

import math
import os
import random
import re
import sys

# Function to calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(a):
    sum1 = 0; sum2 = 0
    #n = max(len(a))
    for i in range(n):
        sum1 += a[i][i]             # sum of left to right diagonal
        sum2 += a[i][n-i-1]         # sum of right to left diagonal
    return(abs(sum1-sum2))

#Input and output commands
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
