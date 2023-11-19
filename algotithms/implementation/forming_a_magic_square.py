'''
Challenge: Forming a Magic Square
Difficulty: Medium
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 78.30%
Task: Find the minimum cost of converting a 3 by 3 matrix into a magic square.
Problem: https://www.hackerrank.com/challenges/magic-square-forming/problem
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
raw_data = '''5 3 4
1 5 8
6 4 2
'''
    # Expected Output:
    # 8 3 4
    # 1 5 9
    # 6 7 2

# Data
input = StringIO(raw_data)

# Function
def formingMagicSquare(s):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    s = []

    for _ in range(3):
        s.append(list(map(int, input.readline().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)