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
    return ''

# Main
if __name__ == '__main__':
    
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input.readline().rstrip().split()))

    result = rotateLeft(d, arr)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
