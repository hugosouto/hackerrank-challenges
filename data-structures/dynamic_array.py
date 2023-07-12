#!/bin/python3

import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Sample Input

raw_data = """2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1"""

input = StringIO(raw_data)

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    return n, queries

if __name__ == '__main__':
    # Create a temporary file
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True) 
    # Original code: fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input.readline().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
