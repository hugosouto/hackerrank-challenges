#!/bin/python3

# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Sample Input
raw_data = "chris alan"

# Data
input = StringIO(raw_data)

# Solution
def solve(s):
    return ''

# Main
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    s = input.readline()

    result = solve(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
