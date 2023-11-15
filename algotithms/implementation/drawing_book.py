'''
Challenge: Drawing Book
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 89.76%
Task: How many pages does a student need to turn to get to page p?
Problem: https://www.hackerrank.com/challenges/drawing-book/problem
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
raw_data = '''6
5
'''
    # Expected Output:
    # 1

# raw_data = '''5
# 4
# '''
    # Expected Output:
    # 0

# raw_data = '''5
# 4
# '''
    # Expected Output:
    # 0

# Data
input = StringIO(raw_data)

# Function
def pageCount(n, p):
    '''
    Returns the minimum number of page turns required to reach a given page number in a book.

    Args:
    - n (int): The total number of pages in the book.
    - p (int): The page number to reach.

    Returns:
    - int: The minimum number of page turns required to reach the given page number.
    '''
    # Check if last page is even
    if n % 2:
        result = min(p//2, (n+1-p)//2)
    else:
        result = min(p//2, (n-p)//2)
    return result

    # Editorial version
    # if not n%2:
    #     n += 1
    # return min(p//2, (n-p)//2)

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    n = int(input.readline().strip())

    p = int(input.readline().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
