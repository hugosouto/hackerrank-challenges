'''
Challenge: Bot saves princess
Difficulty: Easy
Max Score: 13
Success Rate: 74.04%
Task: An introduction to bot challenges. Rescue the princess trapped in the corner of the grid.
Problem: https://www.hackerrank.com/challenges/saveprincess
'''

# Imports
from io import StringIO

# Simulate input from HackerRank
raw_data = ('''3
---
-m-
p--
''')
    # Expected Output
    # DOWN
    # LEFT

raw_data = ('''5
-----
-----
--m--
-----
----p
''')
    # Expected Output
    # RIGHT
    # RIGHT
    # DOWN
    # DOWN

# Data
input = StringIO(raw_data)

# Function
def displayPathtoPrincess(n, grid):
    # Set start position at the center
    start_line, start_column = n//2, n//2
    # Set current line and column
    line, column = start_line, start_column
    # Set initial position
    position = grid[line][column]

    # Walks to right edge than to bottom
    if position != 'p':
        for _ in range(start_column):
            print('RIGHT')
            column += 1
            position = grid[line][column]
        for _ in range(start_line):
            print('DOWN')
            line += 1
            position = grid[line][column]
    # Walks from right to left in the last row
    if position != 'p':
        for _ in range(n):
            print('LEFT')
            column -= 1
            position = grid[line][column]
    # Walks from bottom to top in the firt column
    if position != 'p':
        for _ in range(n):
            print('UP')
            line -= 1
            position = grid[line][column]
    # Walks from left to right in the first row
    if position != 'p':
        for _ in range(n):
            print('RIGHT')
            column += 1
            position = grid[line][column]

m = int(input.readline())
grid = [] 
for i in range(0, m): 
    grid.append(input.readline().strip())

displayPathtoPrincess(m, grid)