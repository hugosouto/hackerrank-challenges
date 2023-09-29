'''
Challenge: Polar Coordinates
Difficulty: Easy
Topic: Python (Basic)
Max Score: 10
Success Rate: 96.42%
Task: Convert complex numbers to polar coordinates.
Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
'''

# Imports
from io import StringIO
from cmath import phase

# Simulate input from HackerRank
raw_data = '  1+2j'
    # Expected Output:
    #  2.23606797749979 
    #  1.1071487177940904

raw_data = '-1-5j'
    # Expected Output
    # 5.09901951359
    # -1.76819188664

# Data
input = StringIO(raw_data)

# Function
def polar_coordinates(x, y):
    r = phase(complex(x, y))
    phi = abs(complex(x, y))
    return print(round(r, 3), round(phi, 3), sep='\n')

# Main
if __name__ == '__main__':
    x, y = input.readline().split('1')
    y, j = y.split('')
    x, y = int(x), int(y)

    polar_coordinates(x, y)