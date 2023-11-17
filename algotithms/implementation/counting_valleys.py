'''
Challenge: Counting Valleys
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 15
Success Rate: 95.03%
Task: Count the valleys encountered during vacation.
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
raw_data = '''8
UDDDUDUU
'''
    # Expected Output:
    # 1

# Explanation
# If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:
# _/\      _
#    \    /
#     \/\/
# The hiker enters and leaves one valley.

# Data
input = StringIO(raw_data)

# Function
def countingValleys(steps, path):
    '''
    Counts the number of valleys in a given path.

    Parameters:
    steps (int): The number of steps taken.
    path (str): The path taken, consisting of 'U' for uphill and 'D' for downhill.

    Returns:
    int: The number of valleys encountered.
    '''
    log = []
    level = 0
    for step in path:
        if step == 'U':
            level += 1
        if step == 'D':
            level -= 1
        if level < 0:
            on_valley = '1'
        else:
            on_valley = '0'
        log.append(on_valley)
    
    log_string = ''.join(log)
    
    valleys = len(re.findall('/*10/*', log_string))
    return valleys

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    steps = int(input.readline().strip())

    path = input.readline()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    