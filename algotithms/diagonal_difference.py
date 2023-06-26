#!/bin/python3

import math
import os
import random
import re
import sys
import tempfile
from io import StringIO


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

raw_input = ('''3
11 2 4
4 5 6
10 8 -12''')

input = StringIO(raw_input)

def diagonalDifference(arr):

    diagonal_1 = []
    diagonal_2 = []
    
    for i in range(len(arr)):
        diagonal_1.append(arr[i][i])
        diagonal_2.append(arr[i][len(arr)-i-1])
    
    return abs(sum(diagonal_1) - sum(diagonal_2))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    n = int(input.readline().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input.readline().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()