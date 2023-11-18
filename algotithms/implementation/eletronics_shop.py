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
    '''
    Calculates the maximum amount of money that can be spent on a keyboard and a USB drive,
    given a budget 'b' and the prices of available keyboards and drives.
    
    Parameters:
    keyboards (list): A list of integers representing the prices of available keyboards.
    drives (list): A list of integers representing the prices of available USB drives.
    b (int): The budget for the purchase.
    
    Returns:
    int: The maximum amount of money that can be spent, or -1 if it is not possible to buy both items within the budget.
    '''
    
    totals = []
    
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                totals.append(keyboard + drive)
    
    if len(totals) == 0:
        totals = [-1]

    return max(totals)

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