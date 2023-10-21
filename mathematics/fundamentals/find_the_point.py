
'''
Challenge: Find the Point
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 5
Success Rate: 89.08%
Task: Given two points P and Q, output the symmetric point of point P about Q.
Problem: https://www.hackerrank.com/challenges/find-point/problem
'''

# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Simulate input from HackerRank
raw_data = '''2
0 0 1 1
1 1 2 2
'''
    # Expected Output:
    # 2 2
    # 3 3

# Data
input = StringIO(raw_data)

# Function
def findPoint(px, py, qx, qy):
    rx = qx-px + qx-px + px
    ry = qy-py + qy-py + py
    return [rx, ry]

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w+',)
    
    n = int(input.readline().strip())

    for n_itr in range(n):
        first_multiple_input = input.readline().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)
        print(' '.join(map(str, result)))

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
        
    fptr.close()
