'''
Challenge: Bill Division
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 98.01%
Task: Determine whether or not Brian overcharged Anna for their split bill.
Problem: https://www.hackerrank.com/challenges/bon-appetit/problem
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
raw_data = '''4 1
3 10 2 9
12
'''
    # Expected Output:
    # 5

# raw_data = '''4 1
# 3 10 2 9
# 7
# '''
    # Expected Output:
    # Bon Appetit

# Data
input = StringIO(raw_data)

# Function
def bonAppetit(bill, k, b):
    """
    Calculates the amount of money that Anna owes Brian or vice versa after splitting the bill.

    Parameters:
    bill (list): A list of integers representing the cost of each item ordered.
    k (int): An integer representing the zero-based index of the item Anna doesn't eat.
    b (int): An integer representing the amount of money that Anna contributed to the bill.

    Returns:
    None: The function prints either the amount of money that Anna owes Brian or 'Bon Appetit' if they split the bill evenly.
    """
    # anna = sum([sum(bill[:k]), sum(bill[k+1:])])/2
    anna = (sum(bill) - bill[k])/2

    if b == anna:
        result = 'Bon Appetit'
    else:
        result = int(b-anna)
        
    return print(result)

# Main
if __name__ == '__main__':
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input.readline().rstrip().split()))

    b = int(input.readline().strip())

    bonAppetit(bill, k, b)
