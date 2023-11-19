'''
Challenge: Forming a Magic Square
Difficulty: Medium
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 78.30%
Task: Find the minimum cost of converting a 3 by 3 matrix into a magic square.
Problem: https://www.hackerrank.com/challenges/magic-square-forming/problem
'''

# Imports
import math
import os
import random
import re
from ssl import enum_certificates
import sys
import tempfile
from io import StringIO

# Simulate input from HackerRank
raw_data = '''\
5 3 4
1 5 8
6 4 2
'''
    # Expected Output:
    # 7

# raw_data = '''\
# 4 9 2
# 3 5 7
# 8 1 5
# '''
    # Expected Output:
    # 1

# raw_data = '''\
# 4 8 2
# 4 5 7
# 6 1 6
# '''
    # Expected Output:
    # 4

# raw_data = '''\
# 4 5 8
# 2 4 1
# 1 9 7
# '''
    # Expected Output:
    # 14

# Data
input = StringIO(raw_data)

# Function
def formingMagicSquare(s):
    
    original_matrix = s

    magic_sum = sum(list(range(1,10)))
    print('Magic Matrix Sum:', magic_sum)
    matrix_sum = sum([sum(row) for row in s])
    print('Matrix Sum:      ', matrix_sum)

    cost = 0
    
    numbers_used = []
    for row in s:
        if sum(row) < 15: # 15 is the Magic Number
            row_sum = sum(row)
            sorted_row = sorted(row, reverse=True)
            max_value = sorted_row[0]
            if max_value in numbers_used:
                max_value = sorted_row[1]
                if max_value in numbers_used:
                    max_value = sorted_row[2]
            max_index = row.index(max_value)
            row_cost = 15 - row_sum
            row[max_index] += row_cost
            cost += row_cost
            numbers_used += row

        if sum(row) > 15: # 15 is the Magic Number
            row_sum = sum(row)
            sorted_row = sorted(row, reverse=True)
            max_value = sorted_row[0]
            if max_value in numbers_used:
                max_value = sorted_row[1]
                if max_value in numbers_used:
                    max_value = sorted_row[2]
            max_index = row.index(max_value)
            row_cost = row_sum - 15
            row[max_index] -= row_cost
            cost += row_cost
            numbers_used += row

    c = 0
    for column in zip(*original_matrix):
        print(f"Column {c}: {sum(column)}")
        c += 1

    return cost

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    s = []

    for _ in range(3):
        s.append(list(map(int, input.readline().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)