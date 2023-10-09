
'''
Challenge: Between Two Sets
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 90.67%
Task: Find the number of integers that satisfies certain criteria relative to two sets.
Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
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
raw_data = '''2 3
2 4
16 32 96
'''
    # Expected Output:
    # 3

raw_data = '''2 2
3 4
24 48
'''
    # Expected Output:
    # 2

# Data
input = StringIO(raw_data)

# Function
def getTotalX(a, b):
    '''
    Given two lists of integers, a and b, find the number of integers 
    that satisfy certain criteria relative to the two sets.
    '''

    max_a = max(a)
    min_b = min(b)

    # Original code
    # rng = range(max_a, min_b + 1)
    # condition_1, condition_2 = [], []
    # for number in rng:
    #     if all(number % item == 0 for item in a):
    #         condition_1.append(number)
    # 
    # for number in condition_1:
    #     if all(item % number == 0 for item in b):
    #         condition_2.append(number)
    # 
    # total = len(condition_2)

    # ChatGPT Assisted Refactoring
    numbers_meeting_criteria = [number for number in range(max_a, min_b + 1) 
                                if all(number % item == 0 for item in a) 
                                and all(item % number == 0 for item in b)]

    total = len(set(numbers_meeting_criteria))

    return total

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input.readline().rstrip().split()))

    brr = list(map(int, input.readline().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)

    fptr.write(str(total) + '\n')

    fptr.close()