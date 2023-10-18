'''
Challenge: Breaking the Records
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 98.54%
Task: Given an array of Maria's basketball scores all season, determine the number of 
      times she breaks her best and worst records.
Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
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
raw_data = '''10
3 4 21 36 10 28 35 5 24 42
'''
    # Expected Output:
    # 4 0

# Data
input = StringIO(raw_data)

# Function
def breakingRecords(scores):
    return result

# Main
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    n = int(input.readline().strip())

    scores = list(map(int, input.readline().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
