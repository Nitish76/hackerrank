#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = 0
    for i in arr:
        total += i
    mini = total - max(arr)
    maxi = total - min(arr)
    print(mini,maxi)
    return()
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
