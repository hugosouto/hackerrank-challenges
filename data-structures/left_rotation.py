#!/bin/python3

# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Input Simulation
raw_input = '''5 4
1 2 3 4 5'''

# Data
input = StringIO(raw_input)

# Solution
def rotateLeft(d, arr):

    # Iterates d times
    for _ in range(d):
        # Create copy for index searching while numbers are changing
        temp = arr.copy()

        # Iterate each position on arr
        for i in range(len(arr)):
            # If condition to solve the last position
            if i == (len(temp)-1):
                arr[i] = temp[0]
            else:
                arr[i] = temp[i+1]
        print(arr)

    return arr

# Main
if __name__ == '__main__':
    
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input.readline().rstrip().split()))

    result = rotateLeft(d, arr)
    # print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
