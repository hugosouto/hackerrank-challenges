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
# raw_data = '''6 5
# 1 2 3 4 5 6
# '''
    # Expected Output:
    # 3

raw_data = '''6 3
1 3 2 6 1 2
'''
    # Expected Output:
    # 5

# Data
input = StringIO(raw_data)

# Function
def divisibleSumPairs(n, k, ar):
    """
    Returns the number of pairs of integers in the list 'ar' whose sum is divisible by 'k'.

    Args:
    n (int): The length of the list 'ar'.
    k (int): The integer to divide the pair sum by.
    ar (list): A list of integers.

    Returns:
    int: The number of pairs of integers in the list 'ar' whose sum is divisible by 'k'.
    """
    # Copilot improved version
    pairs = sum(1 for i in range(n) for j in range(n) if i < j and (ar[i] + ar[j]) % k == 0)

    return pairs

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
