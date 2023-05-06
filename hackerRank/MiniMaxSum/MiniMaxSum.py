import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    print(sum(arr[:4]),sum(arr[1:]))


if __name__ == '__main__':

    arr = sorted(list(map(int, input().rstrip().split())))
    
    miniMaxSum(arr)
