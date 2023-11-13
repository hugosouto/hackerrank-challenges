'''
Challenge: Sales by Match
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 92.47%
Task: How many pairs of socks can Alex sell?
Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
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
raw_data = '''9
10 20 20 10 10 30 50 10 20
'''
    # Expected Output:
    # 3

# Data
input = StringIO(raw_data)

# Function
def sockMerchant(n, ar):
    result = ''
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    n = int(input.readline().strip())

    ar = list(map(int, input.readline().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)