'''
Challenge: Subarray Division
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 94.09%
Task: Given an array of integers, find the number of subarrays of length k having sum s.
Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
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
# raw_data = '''5
# 2 2 1 3 2
# 4 2
# '''
    # Expected Output:
    # 2

# raw_data = '''5
# 1 2 1 3 2
# 3 2
# '''
    # Expected Output:
    # 2

# raw_data = '''6
# 1 1 1 1 1 1
# 3 2
# '''
    # Expected Output:
    # 0

raw_data = '''1
4
4 1
'''
    # Expected Output:
    # 1

# Data
input = StringIO(raw_data)

# Function
def birthday(s, d, m):
    """
    Counts the number of ways to divide the list s into subarrays of length equal to a month
    number m such that the sum of the elements in each subarray is equal to the birth day d.

    Args:
    s (list): A list of integers representing the numbers on each of the squares of chocolate.
    d (int): An integer representing a birth day.
    m (int): An integer representing a birth month.

    Returns:
    int: The number of ways to divide the list s into subarrays of length m such that the sum of
    the elements in each subarray is equal to d.
    """
    
    ways = 0                                                                                       # Initialize the variable that will count the number of ways to divide the list s.
    for initial_size in range(len(s) + 1):                                                         # Iterate over all possible starting indices of subarrays.
        for end_size in range(len(s) + 1):                                                         # Iterate over all possible ending indices of subarrays.
            if initial_size < end_size in range(len(s) + 1):                                       # Check if the starting index is less than the ending index and both are within the bounds of the list s.
                if sum(s[initial_size:end_size]) == d and len(s[initial_size:end_size]) == m:      # Check if the sum of the elements in the subarray is equal to d and the length of the subarray is equal to m.
                    ways += 1                                                                      # If both conditions are true, increment the ways variable.
    
    return ways

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')

    n = int(input.readline().strip())

    s = list(map(int, input.readline().rstrip().split()))

    first_multiple_input = input.readline().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)