'''
Task:

• Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n 
    integers. Then compute and print the result of hash(t).

'''

# Deveopment:

# Imports the required libraries
from io import StringIO

## Creates raw artificial data
raw = (f'''2
1 2''')

## Simulates a user input
input = StringIO(raw)

# Solution:
if __name__ == '__main__':

    n = int(input.readline())
    integer_list = map(int, input.readline().split())
    
    integer_tuple = tuple(integer_list)

    print(hash(integer_tuple))