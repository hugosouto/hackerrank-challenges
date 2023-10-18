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
raw_data = '''9
10 5 20 20 4 5 2 25 1
'''
    # Expected Output:
    # 2 4

raw_data = '''10
3 4 21 36 10 28 35 5 24 42
'''
    # Expected Output:
    # 4 0

# Data
input = StringIO(raw_data)

# Function
def breakingRecords(scores):
    print('scores:', scores)
    print('scores[0]:', scores[0])
    max_record, min_record = scores[0], scores[0]
    max_count, min_count = 0, 0

    for score in scores[1:]:
        print('score:', score, '| max_record:', max_record, '| min_record:', min_record)
        
        if score > max_record:
            max_record = score
            max_count += 1
        
        elif score < min_record:
            min_record = score
            min_count += 1
    
    return max_count, min_count

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
