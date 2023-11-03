'''
Challenge: Migratory Birds
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 91.87%
Task: Determine which type of bird in a flock occurs at the highest frequency.
Problem: https://www.hackerrank.com/challenges/[...]/problem
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
# raw_data = '''6
# 1 4 4 4 5 3
# '''
#     # Expected Output:
#     # 4

raw_data = '''11
1 2 3 4 5 4 3 2 1 3 4
'''
    # Expected Output:
    # 3

# Data
input = StringIO(raw_data)

# Function
def migratoryBirds(arr):
    '''
    Given an array of bird sightings where every element represents a bird type
    id, determine the id of the most frequently sighted type. If more than 1
    type has been spottedthat maximum amount, return the smallest of their ids.

    Args:
    arr (list): A list of integers representing bird sightings.

    Returns:
    int: The id of the most frequently sighted bird type.
    '''
    count = dict.fromkeys(list(range(1,6)), 0)
        # Alternative from: count = {1:0, 2:0, 3:0, 4:0, 5:0}
    for x in arr:
        if x in count:
            count[x] += 1
    count_list = list(count.items())
    
    for x in count_list:
        if x[1] == max(count.values()):
            result = x[0]
            break

    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    arr_count = int(input.readline().strip())

    arr = list(map(int, input.readline().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)