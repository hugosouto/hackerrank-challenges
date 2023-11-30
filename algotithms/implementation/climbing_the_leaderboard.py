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
    '''
    Calculates the rank of each player in the leaderboard based on their scores.

    Parameters:
    ranked (list): A list of integers representing the scores of the players in the leaderboard.
    player (list): A list of integers representing the scores of the players to be ranked.

    Returns:
    list: A list of integers representing the ranks of the players in the leaderboard.
    '''
    def rerank(ranked):
        return (sorted(list(set(ranked)), reverse=True))

    score, scores = 0, []
    for p in player:
        for r in ranked:
            if p == r:
                score = ranked.index(r)+1
            if p < r:
                score = ranked.index(r)+2
            ranked.append(p)
            ranked = rerank(ranked)
        print(ranked)
        print(scores)
        scores.append(score)

    return scores

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