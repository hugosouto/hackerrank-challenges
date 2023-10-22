# Full Path: https://www.hackerrank.com/challenges/python-division/problem
# 
# Task:
# The provided code stub reads two integers, a and b, from STDIN.
# 
# Add logic to print two lines. The first line should contain the result of integer division, a // b.
# The second line should contain the result of float division, a / b.
# 
# No rounding or formatting is necessary.


# Code Stub:
# 
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())


# Solution:

# Data

## Import package to simulate HackerHack input
from random import randint
from io import StringIO

## Artificial data to simulate HackerRank input
raw_data = (f'''{randint(1, 100)}
{randint(1, 100)}''')

## Convert the string data to a file-like object
input = StringIO(raw_data)

# Main
if __name__ == '__main__':
    a = int(input.readline())
    b = int(input.readline())

    # print(f'a = {a}, b = {b}')
    print(a // b, a / b, sep='\n')