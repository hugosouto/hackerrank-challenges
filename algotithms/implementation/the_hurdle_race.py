'''
Challenge: The Hurdle Race
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 15
Success Rate: 98.85%
Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
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
raw_data = '''5 4
1 6 3 5 2
'''
    # Expected Output:
    # 2

raw_data = '''5 7
2 5 4 5 2
'''
    # Expected Output:
    # 0

# Data
input = StringIO(raw_data)

# Function
def hurdleRace(k, height):
    '''
    Calculates the minimum number of potions needed to overcome the hurdles.

    Parameters:
    k (int): The maximum height the character can jump without consuming a potion.
    height (list): A list of integers representing the heights of the hurdles.

    Returns:
    int: The minimum number of potions needed to overcome the hurdles.
    '''
    potions = 0
    if max(height) > k:
        potions = max(height)-k
    return potions

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')

    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input.readline().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
