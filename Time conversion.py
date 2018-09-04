#!/bin/python3

import os
import sys


# A function to convert 12-hour AM/PM time to millitary time

def timeConversion(s):
    hr = (s[0:2]); min = s[3:5]; sec = s[6:8];ap = s[8:9]       # Extracting hours, minutes, seconds and AM/PM to different variables
    if ap == 'A':                                               # Conversion for AM case
        if int(hr)== 12:
            hr = str('00')
            time = hr +':'+min+':'+sec
        else:
            time = hr +':'+min+':'+sec
    else:                                                       # Conversion for PM case
        if int(hr) == 12:
            time = hr +':'+min+':'+sec
        else:
            hr = str(int(hr)+12)
            time = hr+':'+min+':'+sec
    return(time)
    
# Input statements
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result +'\n' )

    f.close()
