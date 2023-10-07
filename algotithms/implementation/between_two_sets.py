
'''
Challenge: Between Two Sets
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 90.67%
Task: Find the number of integers that satisfies certain criteria relative to two sets.
Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
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
raw_data = '''2 3
2 4
16 32 96
'''
    # Expected Output:
    # 3

# Data
input = StringIO(raw_data)

# Function
def getTotalX(a, b):
    return total

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input.readline().rstrip().split()))

    brr = list(map(int, input.readline().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    fptr.write(str(total) + '\n')

    fptr.close()