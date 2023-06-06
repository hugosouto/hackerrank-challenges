# Initial code
# 
# #!/usr/bin/python
# 
# def displayPathtoPrincess(n,grid):
# #print all the moves here
# 
# m = int(input())
# grid = [] 
# for i in range(0, m): 
#     grid.append(input().strip())
# 
# displayPathtoPrincess(m,grid)

# Artificial data to simulate HackerRank input
input = ('''3
---
-m-
p--''')

# Import package to simulate HackerHack input
from io import StringIO

# Convert the string data to a file-like object
data_io = StringIO(input)

# Modified HackerHack code stub
def displayPathtoPrincess(n,grid):
    # Print all the moves here:
    print('Test')

m = int(data_io.readline())
grid = [] 
for i in range(0, m): 
    grid.append(data_io.readline().strip())

displayPathtoPrincess(m,grid)