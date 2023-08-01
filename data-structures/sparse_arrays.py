#!/bin/python3

'''
Sparse Arrays
Topic: Problem Solving (Basic)
Task: Determine the number of times a string has previously appeared.
Difficulty: Medium
Success Rate: 97.32%
Max Score: 25
Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem
'''

# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO
#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

# Data
raw_data = '''4
aba
baba
aba
xzxb
3
aba
xzxb
ab'''

# Input Simulation
input = StringIO(raw_data)

# Solution
def matchingStrings(stringList, queries):
    # Write your code here
    return ''

# Main
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    stringList_count = int(input.readline().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input.readline()
        stringList.append(stringList_item)

    queries_count = int(input.readline().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input.readline()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
