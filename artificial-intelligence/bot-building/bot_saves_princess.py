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

# Data
input = StringIO(raw_data)

# Function
def displayPathtoPrincess(n,grid):
    # Print all the moves here:
    print('Test')

m = int(input.readline())
grid = [] 
for i in range(0, m): 
    grid.append(input.readline().strip())

displayPathtoPrincess(m,grid)