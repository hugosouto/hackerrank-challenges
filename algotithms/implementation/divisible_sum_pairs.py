'''
Challenge: Divisible Sum Pairs
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 97.69%
Task: Count the number of pairs in an array having sums that are evenly divisible by a given number.
Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
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
raw_data = '''6 3
1 3 2 6 1 2
'''
    # Expected Output:
    # 5

# Data
input = StringIO(raw_data)

# Function
def divisibleSumPairs(n, k, ar):
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input.readline().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)