'''
Challenge: Climbing the Leaderboard
Difficulty: Medium
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 60.71%
Task: Help Alice track her progress toward the top of the leaderboard!
Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
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
raw_data = '''7
100 100 50 40 40 20 10
4
5 25 50 120
'''
    # Expected Output:
    # 6
    # 4
    # 2
    # 1

raw_data = '''6
100 90 90 80 75 60
5
50 65 77 90 102
'''
    # Expected Output:
    # 6
    # 5
    # 4
    # 2
    # 1
# Data
input = StringIO(raw_data)

# Function
def climbingLeaderboard(ranked, player):
    return 'result'

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    ranked_count = int(input.readline().strip())

    ranked = list(map(int, input.readline().rstrip().split()))

    player_count = int(input.readline().strip())

    player = list(map(int, input.readline().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    print(result)