#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hr = (s[0:2]); min = s[3:5]; sec = s[6:8];ap = s[8:9]
    if ap == 'A':
        if int(hr)== 12:
            hr = str('00')
            time = hr +':'+min+':'+sec
        else:
            time = hr +':'+min+':'+sec
    else:
        if int(hr) == 12:
            time = hr +':'+min+':'+sec
        else:
            hr = str(int(hr)+12)
            time = hr+':'+min+':'+sec
    return(time)
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result +'\n' )

    f.close()
