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
from time import time
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

raw_data = '''100
8602686 8546271 8526715 8519247 8415976 8361529 8342931 8303364 8291180 7848549 7847864 7823851 7773936 7699327 7602749 7540526 7385441 7366433 7337630 7272373 7187504 7175749 7023343 7016216 7010723 6889607 6863558 6591329 6531546 6426286 6407031 6365870 6311121 6221977 5801839 5747997 5730472 5724599 5424544 5354783 5296128 5295458 5238523 5149248 4850739 4791108 4763665 4750185 4719109 4526021 4494678 4449061 4362767 4237908 4213229 4207655 4169092 4138237 3938541 3790285 3766792 3754053 3632939 3617582 3608983 3521123 3330943 3279031 3227047 3094550 3025172 3009534 2943676 2904654 2809765 2551266 2428570 2301374 2254113 2231034 2228132 2208756 1810975 1702807 1698924 1668930 1654148 1536080 1477819 1328232 1000898 925673 874028 630208 524009 502548 387784 283346 59336 17498
50
391846 801454 932294 992081 1432552 1433244 1436692 1463582 1703613 1762894 1794359 1800192 1894975 1913203 1964838 2005948 2047999 2383858 2684319 2743219 2836582 3152591 3238095 3318511 3402656 3496157 3506024 3597120 3638481 3642843 3670712 3726377 4150638 4554272 4802824 4857664 4898431 5012543 5280270 5364626 5676136 5876874 6022361 6028227 6245061 6328848 6580175 6589494 6791072 6972786
'''
    # Expected Output:
    # 997
    # 994
    # 992
    # 992
    # ...
    # 19
    # 18
    # 16
    # 14
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
    def rerank(rank):
        return sorted(set(rank)) # , reverse=True

    ranked = rerank(ranked)
    # print('ranked:', ranked, len(ranked))
    # print('player:', player)

    score, scores = 0, []
    for p in range(len(player)):
        # print('p:', player[p])
        for r in range(len(ranked)):
            # print('r:', ranked[r])
            # print('len(ranked):', len(ranked))
            if player[p] > ranked[len(ranked)-1]:
                score = 1
                ranked = ranked[:] + [player[p]]
                break
            elif player[p] < ranked[r]:
                score = (len(ranked) - ranked.index(ranked[r])) + 1
                ranked = ranked[:r] + [player[p]] + ranked[r:]
                break
            elif player[p] == ranked[r]:
                score = len(ranked) - ranked.index(ranked[r])
                break
            # ranked.append(player[p])
            ranked = rerank(ranked)
        scores.append(score)
        # print(scores)
        # print(ranked)

    return scores

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    ranked_count = int(input.readline().strip())

    ranked = list(map(int, input.readline().rstrip().split()))

    player_count = int(input.readline().strip())

    player = list(map(int, input.readline().rstrip().split()))

    tic = time()
    result = climbingLeaderboard(ranked, player)
    tac = time()

    print('Runtime:', tac-tic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    print(result)