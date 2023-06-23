#!/bin/python3

# Imports the required libraries

import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# About the challenge:
# 
# Complete the 'aVeryBigSum' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.


# Artificial data to simulate HackerRank input

def generate_data(length):
    data = []
    for _ in range(length):
        data.append(random.randint(1, 1000000000))
    return data

def create_raw_data(length):
    data = generate_data(length)
    raw = f"{length}\n{' '.join(str(num) for num in data)}"
    return raw

raw = create_raw_data(random.randint(1, 11))


# Convert the string data to a file-like object

input = StringIO(raw)

def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    # Simulates the original 'fptr = open(os.environ['OUTPUT_PATH'], 'w')' command with a temporary file
    fptr = tempfile.NamedTemporaryFile(mode='w')

    ar_count = int(input.readline().strip())

    ar = list(map(int, input.readline().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
