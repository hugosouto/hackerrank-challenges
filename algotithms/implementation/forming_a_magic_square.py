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
import sys
import tempfile
from itertools import permutations
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

    print('s', s)
    original_list = [i for sub in s for i in sub]
    print('original_list', original_list)

    perms = [list(p) for p in sorted(permutations(range(1, 10), 9))]
    # print('perms[:5]', perms[:5])

    magic_squares = []
    for p in perms:
        if  sum(p[:3])  == 15 \
        and sum(p[3:6]) == 15 \
        and sum(p[6:])  == 15 \
        and sum([p[0],p[3],p[6]]) == 15 \
        and sum([p[1],p[4],p[7]]) == 15 \
        and sum([p[2],p[5],p[8]]) == 15 \
        and sum([p[0],p[4],p[8]]) == 15 \
        and sum([p[2],p[4],p[6]]) == 15:
            magic_squares.append(p)

    print('magic_squares', magic_squares)

    costs = []
    for i in original_list:
        for magic_square in magic_squares:
            cost = []
            for number in magic_square:
                cost.append(abs(i - number))
                # print('cost:', cost)
        costs.append(sum(cost))
        print('costs:', costs)

    print(costs)
    print(min(costs))

    # return min(costs)

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
