'''
Challenge: Picking Numbers
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 90.10%
Task: What's the largest size subset can you choose from an array such that the difference between any two integers is not bigger than 1?
Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
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
4 6 5 3 3 1
'''
# Expected Output:
# 3

raw_data = '''6
1 2 2 3 1 2
'''
# Expected Output:
# 5

# Data
input = StringIO(raw_data)

# Function
def pickingNumbers(a):
    numbers = sorted(a)
    print(numbers)

    lenghts = []
    sub = []

    print(range(len(numbers)))

    for slice_begin in range(0, len(numbers) - 1):
        print('slice_begin', numbers[slice_begin])
        # cursor = numbers[slice_begin + 1]
        for slice_end in range(slice_begin + 1, len(numbers) - 1):
            if slice_end - slice_begin <= 1:
                slice_end += 1
                print('slice_end', slice_end)
            else:
                lenghts.append(len(numbers[slice_begin:slice_end]))
        # print(sub)
    print('lenghts', lenghts)

    return max(lenghts)

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')

    n = int(input.readline().strip())

    a = list(map(int, input.readline().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
