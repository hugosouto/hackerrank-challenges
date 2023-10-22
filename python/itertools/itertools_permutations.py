'''
Challenge: itertools.permutations()
Difficulty: Easy
Topic: Python (Basic)
Max Score: 10
Success Rate: 97.98%
Task: Find all permutations of a given size in a given string.
Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
'''

# Imports
from io import StringIO
from itertools import permutations

# Simulate input from HackerRank
raw_data = '''HACK 2'''
    # Expected Output:
    # AC
    # AH
    # AK
    # CA
    # CH
    # CK
    # HA
    # HC
    # HK
    # KA
    # KC
    # KH

# Data
input = StringIO(raw_data)

# Function
def permute(string, size):
    perms = sorted(list(permutations(string, size)))
    result = [print(*i, sep='') for i in perms]
    return result

# Main
if __name__ == '__main__':
    S, k = input.readline().split()
    permute(S, int(k))