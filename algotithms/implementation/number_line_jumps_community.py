'''
Challenge: Number Line Jumps
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 89.44%
Task: Can two kangaroo meet after making the same number of jumps?
Problem: https://www.hackerrank.com/challenges/kangaroo/problem
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
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

# Simulate input from HackerRank
raw_data = '''0 2 5 3'''
    # Expected Output:
    # NO

# raw_data = '''21 6 47 3'''
    # Expected Output:
    # NO

# raw_data = '''9 3 0 6'''
    # Expected Output:
    # YES

# Data
input = StringIO(raw_data)

# Function
def kangaroo(x1, v1, x2, v2):

    X = [x1, v1]
    Y = [x2, v2]
    back = min(X, Y)
    fwd = max(X, Y)
    dist = fwd[0] - back[0]

    while back[0] < fwd[0]:
        back[0] += back[1]
        fwd[0] += fwd[1]
        if fwd[0] - back[0] >= dist:
            break
    
    result = ["NO", "YES"][back[0] == fwd[0]]

    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w')

    first_multiple_input = input.readline().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    
    print(result)

    fptr.write(result + '\n')

    fptr.close()
