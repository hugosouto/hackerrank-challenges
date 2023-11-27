'''
Challenge: Picking Numbers
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 90.10%
Task: What's the largest size subset can you choose from an array such that the difference between any two integers is not bigger than 1?
Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
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
4 6 5 3 3 1
'''
    # Expected Output:
    # 3

raw_data = '''6
1 2 2 3 1 2
'''
    # Expected Output:
    # 5

# Data
input = StringIO(raw_data)

# Function
def pickingNumbers(a):

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')

    n = int(input.readline().strip())

    a = list(map(int, input.readline().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
