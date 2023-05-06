import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == "AM": 
        if s[:2]=='12':
            s = ''.join('00'+ s[2:])
    elif s[-2:] == "PM":
        s = ''.join(str(int(s[:2])+12) + s[2:])
        if s[:2] == '24':
            s = ''.join(str(int(s[:2])-12) + s[2:])
    s = s[:-2]
    return s 
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
