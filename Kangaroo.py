#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1==x2:
        if v1==v2:
            return('YES')
        else:
            return('NO')
    elif v1==v2:
        return('NO')
    else:
        a= [x1,v1] ; b = [x2,v2]
        if (a[0]<b[0] and a[1]<b[1]) or (b[0]<a[0] and b[1]<a[1]):
            return('NO')
        else:
            k1=x1; k2=x2;
            ini_d= k1-k2; i=1; d=k1-k2        
            while ini_d*d>0:
                k1=x1 + (i*v1)
                k2=x2 + (i*v2)
                d=k1-k2
                if d==0:
                    return('YES')
                else:
                    i += 1
            return('NO')
        
        
        

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
