#!/bin/python3

import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Artificial data to simulate HackerRank's input
raw_input = ('''1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0''')

# Convert the string data to a file-like object
input = StringIO(raw_input)

# Solution
def hourglassSum(arr):
    
    sums = []

    for i in range(6-2):
        for j in range(6-2):
            sums.append(sum(arr[i][j:j+3]) + sum(arr[i+1][j+1]) + sum(arr[i+2][j:j+3]))
    return sum(sums)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input.readline().rstrip().split())))

    result = hourglassSum(arr)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
