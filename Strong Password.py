#!/bin/python3

import math
import os
import random
import re
import sys

'''The website considers a password to be strong if it satisfies the following criteria:
    Its length is at least 6
    It contains at least one digit
    It contains at least one lowercase English character
    It contains at least one uppercase English character
    It contains at least one special character. The special characters are: !@#$%^&*()-+ '''

# The functionbelow checks if the given password is strong
# If not, then it returns the minimum number of characters to be added to make it strong
# 1<= n <=100   (n is length of input password)

def minimumNumber(n, password):
    num = "0123456789"; is_num = 0                  #digits and their counter
    lc = "abcdefghijklmnopqrstuvwxyz"; is_lc = 0    #lowercase letters and their counter
    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; is_uc = 0    #uppercase letters and their counter
    sc = "!@#$%^&*()-+"; is_sc = 0                  #special characters and their counter
    for i in password:
        if i in num:
            is_num +=1
        if i in lc:
            is_lc += 1
        if i in uc:
            is_uc += 1
        if i in sc:
            is_sc += 1
    total = 0;                                      # variable to count min no. of characters needed 
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

#input and output statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
