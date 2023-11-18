'''
Challenge: Cats and a Mouse
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 15
Success Rate: 97.99%
Task: Which cat will catch the mouse first?
Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
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
raw_data = '''2
1 2 3
1 3 2
'''
    # Expected Output:
    # Cat B
    # Mouse C

# Data
input = StringIO(raw_data)

# Function
def catAndMouse(x, y, z):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    q = int(input.readline())

    for q_itr in range(q):
        xyz = input.readline().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        
        fptr.write(result + '\n')

        print(result)

    fptr.close()
