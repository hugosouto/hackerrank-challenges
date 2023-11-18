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
    '''
    Determines which cat will reach the mouse first or if the mouse will escape.

    Parameters:
    x (int): The position of cat A.
    y (int): The position of cat B.
    z (int): The position of the mouse.

    Returns:
    str: The result indicating which cat will reach the mouse first or if the mouse will escape.
    '''
    distance_A = abs(z-x)
    distance_B = abs(z-y)

    if distance_A < distance_B:
        result = 'Cat A'
    elif distance_A > distance_B:
        result = 'Cat B'
    elif distance_A == distance_B:
        result = 'Mouse C'

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
