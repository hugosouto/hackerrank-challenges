'''
Challenge: A Very Big Sum
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 98.80%
Task: Calculate and print the sum of an array, keeping in mind that some of those integers may be quite large.
Problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem
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
def generate_data(length):
    data = []
    for _ in range(length):
        data.append(random.randint(1, 1000000000))
    return data

def create_raw_data(length):
    data = generate_data(length)
    raw = f"{length}\n{' '.join(str(num) for num in data)}"
    return raw

raw_data = create_raw_data(random.randint(1, 11))

# Data
input = StringIO(raw_data)

# Function
def aVeryBigSum(ar):
    return sum(ar)

# Main
if __name__ == '__main__':
    # Simulates the original 'fptr = open(os.environ['OUTPUT_PATH'], 'w')' command with a temporary file
    fptr = tempfile.NamedTemporaryFile(mode='w')

    ar_count = int(input.readline().strip())

    ar = list(map(int, input.readline().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
