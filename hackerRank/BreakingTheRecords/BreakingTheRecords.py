import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    breaking_cnt = [0,0]
    minimum_maximum = [scores[0],scores[0]]
    for s in scores[1:]:
        if s < minimum_maximum[0]:
            breaking_cnt[0] += 1
            minimum_maximum[0] = s
        elif s > minimum_maximum[1]:
            breaking_cnt[1] += 1
            minimum_maximum[1] = s
    return breaking_cnt[::-1]   #  Index  is for breaking most points records, and index  is for breaking least points records.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
