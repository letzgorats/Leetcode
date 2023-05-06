import math
import os
import random
import re
import sys
input = sys.stdin.readline
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    pcnt, zcnt, ncnt = 0,0,0
    for a in arr:
        if a>0: # positive
            pcnt += 1
        elif a == 0:    # zero
            zcnt += 1
        else:   # negative
            ncnt += 1
    
    answer1 = "{:.6f}".format(pcnt/len(arr))
    answer2 = "{:.6f}".format(ncnt/len(arr))
    answer3 = "{:.6f}".format(zcnt/len(arr))
    print(answer1)
    print(answer2)
    print(answer3)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
