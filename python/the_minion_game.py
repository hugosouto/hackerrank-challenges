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
import string
from io import StringIO

# Data
raw_data = "BANANA"

# Simulate User Input
input = StringIO(raw_data)

# Solution
def minion_game(string):
    
    s, k = [], []
    for i in string:
        for j in string:
            # print(i+j)

            # TODO: Make the condition: 'if i is not equal to vowels' work properly.
            # print(j)
            if str(j) == str(any(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])):
                # TODO: Multiply each letter for each letter.
                # print(i*i)
                k.append(i)
            else: # i.upper != ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                s.append(j)
        print('s:', ''.join(s), 'k:', ''.join(k))
    return

# Main
if __name__ == '__main__':
    s = input.readline()
    minion_game(s)