'''
Challenge: itertools.product()
Difficulty: Easy
Topic: Python (Basic)
Max Score: 10
Success Rate: 98.16%
Task: Find the cartesian product of 2 sets.
Problem: https://www.hackerrank.com/challenges/itertools-product/problem
'''

# Imports
from io import StringIO
from itertools import product

# Simulate input from HackerRank
raw_data = '''1 2
3 4'''
# Expected Output
# (1, 3) (1, 4) (2, 3) (2, 4)

# Data
input = StringIO(raw_data)

# Solution
def cartesian_product(x, y):
    lst = list(product(x, y))

    for i in lst:
        print(i, end=' ')

# Main
if __name__ == "__main__":
    A = list(map(int, input.readline().split()))
    B = list(map(int, input.readline().split()))

    cartesian_product(A, B)