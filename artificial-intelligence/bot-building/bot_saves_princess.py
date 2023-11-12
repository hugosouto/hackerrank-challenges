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
# raw_data = ('''3
# ---
# -m-
# p--
# ''')
    # Expected Output
    # DOWN
    # LEFT

raw_data = ('''3
---
-m-
--p
''')
    # Expected Output
    # UP
    # RIGHT

# raw_data = ('''5
# -----
# -----
# --m--
# -----
# ----p
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
    
    # Set start position at the center
    start_line, start_column = n//2, n//2
    
    def SetToStart(n, grid, start_line=start_line, start_column=start_line):
        # Set current line and column
        line, column = start_line, start_column
        # Set initial position
        position = grid[start_line][start_column]
        # Walks to upper left
        return line, column, position
    
    # print(line, column, position)

    # Set position on the center
    line, column, position = SetToStart(n, grid)

    # Walks to bottom right
    if grid[n-1][n-1] == 'p':
        while position != 'p':
            for _ in range(start_line):
                print('DOWN')
                line += 1
                position = grid[line][column]
            for _ in range(start_column):
                print('RIGHT')
                column += 1
                position = grid[line][column]
    
    # Set position on the center
    line, column, position = SetToStart(n, grid)
    
    # Walks to bottom left
    if grid[n-1][0] == 'p':
        while position != 'p':
            for _ in range(start_line):
                print('DOWN')
                line += 1
                position = grid[line][column]
            for _ in range(start_column):
                print('LEFT')
                column -= 1
                position = grid[line][column]

    # Set position on the center
    line, column, position = SetToStart(n, grid)
    
    # Walks to up left
    if grid[0][n-1] == 'p':
        while position != 'p':
            for _ in range(start_line):
                print('UP')
                line -= 1
                position = grid[line][column]
            for _ in range(start_column):
                print('LEFT')
                column -= 1
                position = grid[line][column]

    # Set position on the center
    line, column, position = SetToStart(n, grid)
    
    # Walks to up right
    if grid[0][n-1] == 'p':
        while position != 'p':
            for _ in range(start_line):
                print('UP')
                line -= 1
                position = grid[line][column]
            for _ in range(start_column):
                print('RIGHT')
                column += 1
                position = grid[line][column]
            
m = int(input.readline())
grid = [] 
for i in range(0, m): 
    grid.append(input.readline().strip())

displayPathtoPrincess(m, grid)