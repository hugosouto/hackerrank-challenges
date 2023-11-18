'''
Challenge: Electronics Shop
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 15
Success Rate: 92.83%
Task: Determine the most expensive Keyboard and USB drive combination one can purchase within her budget.
Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
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
raw_data = '''10 2 3
3 1
5 2 8
'''
    # Expected Output:
    # 9

# raw_data = '''5 1 1
# 4
# 5
# '''
    # Expected Output:
    # -1

# Data
input = StringIO(raw_data)

# Function
def getMoneySpent(keyboards, drives, b):
    

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    bnm = input.readline().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input.readline().rstrip().split()))

    drives = list(map(int, input.readline().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

    print(moneySpent)