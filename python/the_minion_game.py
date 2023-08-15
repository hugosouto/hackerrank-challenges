'''
Challenge: The Minion Game
Difficulty: Medium
Topic: Python (Basic)
Max Score: 40
Success Rate: 86.75%
Task: Given a string, judge the winner of the minion game.
Problem: https://www.hackerrank.com/challenges/the-minion-game/problem
'''

# Imports
from io import StringIO

# Data
raw_data = "BANANA" # Expected output: Stuart 12
raw_data = "BAANANAS" # Expected output: Kevin 19
raw_data = "AANANAS" # Expected output: Kevin 12

# Simulate User Input
input = StringIO(raw_data)

# Solution
def minion_game(string):
    
    s, k = [], []
    for i in range(len(string)):
        # print(i)

        for j in range(len(string)):

            if j > i:
                if string[i].upper not in ['A', 'E', 'I', 'O', 'U']:
                    s.append(string[i:j])
                else:
                    k.append(string[i:j])

    s = set(s)
    k = set(k)
    
    s_score, k_score = 0, 0
    for i in s:
        if i in string:
            s_score += 1
    
    for i in k:
        if i in string:
            k_score += 1

    if s_score == k_score:
        result = 'Draw'
    elif s_score > k_score:
        result = f'Stuart {s_score}'
    else:
        result = f'Kevin {k_score}'
    
    return print(result)

# Main
if __name__ == '__main__':
    s = input.readline()
    minion_game(s)