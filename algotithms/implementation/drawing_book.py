'''
Challenge: Drawing Book
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 89.76%
Task: How many pages does a student need to turn to get to page p?
Problem: https://www.hackerrank.com/challenges/drawing-book/problem
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
raw_data = '''6
2
'''
    # Expected Output:
    # 1

raw_data = '''5
4
'''
    # Expected Output:
    # 0

# Data
input = StringIO(raw_data)

# Function
def pageCount(n, p):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    n = int(input.readline().strip())

    p = int(input.readline().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

    # print(result)