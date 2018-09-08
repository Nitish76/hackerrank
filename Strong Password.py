#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    num = "0123456789"; is_num = 0
    lc = "abcdefghijklmnopqrstuvwxyz"; is_lc = 0
    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; is_uc = 0
    sc = "!@#$%^&*()-+"; is_sc = 0
    for i in password:
        if i in num:
            is_num +=1
        if i in lc:
            is_lc += 1
        if i in uc:
            is_uc += 1
        if i in sc:
            is_sc += 1
    total = 0;
    if is_num>0:
        pass
    else:
        total +=1
    if is_lc>0:
        pass
    else:
        total +=1
    if is_uc>0:
        pass
    else:
        total +=1
    if is_sc>0:
        pass
    else:
        total +=1
    if n+total>5:
        pass
    else:
        total += (6-n-total) 
    return(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
