
 
'''
Challenge: Array Manipulation
Difficulty: Hard
Topic: Problem Solving (Intermediate)
Max Score: 60
Success Rate: 60.55%
Task: Perform m operations on an array and print the maximum of the values.
Problem: https://www.hackerrank.com/challenges/crush/problem
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
raw_data = '''5 3
1 2 100
2 5 100
3 4 100
'''
    # Expected Output:
    # 200

# Data
input = StringIO(raw_data)

# Function
def arrayManipulation(n, queries):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()