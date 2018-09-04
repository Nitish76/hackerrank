#!/bin/python3

import math
import os
import random
import re
import sys

# A function to calculate the minimum and maximum sum that can be calculated using exactly 4 out of 5 given integers
def miniMaxSum(arr):
    total = 0
    for i in arr:
        total += i
    mini = total - max(arr)
    maxi = total - min(arr)
    print(mini,maxi)
    return()
        
# input statements
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
