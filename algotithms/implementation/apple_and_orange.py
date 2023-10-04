#!/bin/python3

'''
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 96.28%
Task: Find the respective numbers of apples and oranges that fall on Sam's house.
Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
Author: https://github.com/hugosouto
Solution Score: 10.00
'''

# Imports
import math
import os
import random
import re
import sys
from io import StringIO

# Task
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges

# Input Format 
# The first line contains two space-separated integers denoting the respective values of s and t. 
# The second line contains two space-separated integers denoting the respective values of a and b. 
# The third line contains two space-separated integers denoting the respective values of m and n. 
# The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a. 
# The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

# Sample Input
raw_input = """7 11
5 15
3 2
-2 2 1
5 -6"""

# Data
input = StringIO(raw_input)

# Solution
def countApplesAndOranges(s, t, a, b, apples, oranges):
    y,z = 0,0
    for i in range(m):
        if s <= (a + apples[i]) <= t:
            y += 1
    for i in range(n):
        if s <= (b + oranges[i]) <= t:
            z += 1
    return print(y), print(z)

# Main
if __name__ == '__main__':
    first_multiple_input = input.readline().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input.readline().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input.readline().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input.readline().rstrip().split()))

    oranges = list(map(int, input.readline().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
