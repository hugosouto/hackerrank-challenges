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
--p
''')
    # Expected Output
    # DOWN
    # RIGHT

raw_data = ('''3
--p
-m-
---
''')
    # Expected Output
    # UP
    # RIGHT

# raw_data = ('''5
# p----
# -----
# --m--
# -----
# -----
# ''')
    # Expected Output
    # RIGHT
    # RIGHT
    # DOWN
    # DOWN

# Data
input = StringIO(raw_data)

# Function
def displayPathtoPrincess(n, grid):
    m = int((n-1)/2)
    path = ''
    search = []
    
    for position in grid:
        search.append(list(position))

    for row in range(n):
        for col in range(n):
            if search[row][col]=='p' and row==0 and col==0:
                path += m*'UP\n'
                path += m*'LEFT\n'
            elif search[row][col]=='p' and row==0 and col==n-1:
                path += m*'UP\n'
                path += m*'RIGHT\n'
            elif search[row][col]=='p' and row==n-1 and col==0:
                path += m*'DOWN\n'
                path += m*'LEFT\n'
            elif search[row][col]=='p' and row==n-1 and col==n-1:
                path += m*'DOWN\n'
                path += m*'RIGHT\n'
    
    return print(path)
            
m = int(input.readline())
grid = [] 
for i in range(0, m): 
    grid.append(input.readline().strip())

displayPathtoPrincess(m, grid)