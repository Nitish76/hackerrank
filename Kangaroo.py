#!/bin/python3

import math
import os
import random
import re
import sys

# Problem statement :
'''You are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show'''

# Input format: A single line of four space-separated integers denoting the respective values of x1, x2, v1 and v2

#Constraints: 0<= x1,x2 <= 10,000   and     1<= v1,v2 <= 10,000

def kangaroo(x1, v1, x2, v2):
    if x1==x2:                                  # When both kangaroo's start at same position
        if v1==v2:
            return('YES')                       # They will meet only if their speeds are the same
        else:
            return('NO')
    elif v1==v2:                                # If starting points are different but speeds are the same then they will never meet
        return('NO')
    else:
        a= [x1,v1] ; b = [x2,v2]
        if (a[0]<b[0] and a[1]<b[1]) or (b[0]<a[0] and b[1]<a[1]):  
            return('NO')                        # If the kangaroo starting behind is slower, then they will never meet
        else:
            k1=x1; k2=x2;
            ini_d= k1-k2; i=1; d=k1-k2        
            while ini_d*d>0:                    # The condition will falsify as soon as the two kangaroos cross each other
                k1=x1 + (i*v1)
                k2=x2 + (i*v2)
                d=k1-k2
                if d==0:
                    return('YES')
                else:
                    i += 1
            return('NO')
        
        
        
# Input statements
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
