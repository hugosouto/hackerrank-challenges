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
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    steps = int(input.readline().strip())

    path = input.readline()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    