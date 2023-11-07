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
# raw_data = '''2017'''
    # Expected Output:
    # 13.09.2017

# raw_data = '''2016'''
    # Expected Output:
    # 12.09.2016

raw_data = '''1800'''
    # Expected Output:
    # 12.09.1800

# Data
input = StringIO(raw_data)

# Function
def dayOfProgrammer(year):
    '''
    Given a year, this function returns the date of the 256th day of that year, 
    which is known as the Day of the Programmer. The function takes into account 
    the special case of the year 1918, when the 14th day of February was the 32nd 
    day of the year due to a shift in the calendar. 

    Args:
    - year: an integer representing the year for which to calculate the Day of the Programmer

    Returns:
    - a string representing the date of the Day of the Programmer in the format dd.mm.yyyy
    '''
    if year == 1918:
        result = '26.09.1918'
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        result = f'12.09.{year}'
    else:
        result = f'13.09.{year}'
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    year = int(input.readline().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

    print(result)