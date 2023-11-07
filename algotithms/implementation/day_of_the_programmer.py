'''
Challenge: Day of the Programmer
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 15
Success Rate: 90.48%
Task: Given year, determine date of the 256th day of the year.
Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
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
raw_data = '''2017'''
    # Expected Output:
    # 13.09.2017

# raw_data = '''2016'''
    # Expected Output:
    # 12.09.2016

# raw_data = '''1800'''
    # Expected Output:
    # 12.09.1800

# Data
input = StringIO(raw_data)

# Function
def dayOfProgrammer(year):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    year = int(input.readline().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

    print(result)