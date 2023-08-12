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
    
    # s, k = []
    for i in string:

        # print(i)

        # TODO: Make the condition: 'if i is not equal to vowels:'.
        if str(i).upper == ['A', 'E', 'I', 'O', 'U']:
            # TODO: Multiply each letter for each letter.
            print(i*i)
            # s.append(a)
        # elif str(i).upper != ['A', 'E', 'I', 'O', 'U']:
            # print(i*i)

    return

# Main
if __name__ == '__main__':
    s = input.readline()
    minion_game(s)