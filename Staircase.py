#!/bin/python3

import math
import os
import random
import re
import sys

# A fucntion to print a staircase (right oriented) with no spaces preceding the last line.
def staircase(n):
    totchar = n
    for i in range(1,n+1):
        space=totchar - i
        print(space*' '+i*'#')
    return()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
