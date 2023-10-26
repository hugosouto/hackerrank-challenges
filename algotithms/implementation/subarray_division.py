'''
Challenge: Subarray Division
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 94.09%
Task: Given an array of integers, find the number of subarrays of length k having sum s.
Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
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
raw_data = '''5
1 2 1 3 2
3 2
'''
    # Expected Output:
    # 2

raw_data = '''6
1 1 1 1 1 1
3 2
'''
    # Expected Output:
    # 0

raw_data = '''1
4
4 1
'''
    # Expected Output:
    # 1

# Data
input = StringIO(raw_data)

# Function
def birthday(s, d, m):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')

    n = int(input.readline().strip())

    s = list(map(int, input.readline().rstrip().split()))

    first_multiple_input = input.readline().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)