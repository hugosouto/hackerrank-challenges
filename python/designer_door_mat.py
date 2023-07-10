'''
# Problem

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, and M is 3 times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

# Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

# Input Format

A single line containing the space separated values of N and M.

# Constraints

5 < N < 101
15 < M < 303

# Output Format

Output the design pattern.

# Sample Input

9 27

# Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''

# Read input from STDIN. Print output to STDOUT

# Imports
import random
from io import StringIO

# Data
n = random.randrange(7, 99, 2)
m = n * 3

raw_data = f'{n} {m}'

input = StringIO(raw_data)

# Solution
N, M = map(int, input.readline().split())

dash = '-'
dot = '.|.'

for i in range(N//2):
    print(str(dash*((M//2)-1-3*i)).rjust(((M//2)-1-3*i)) + 
          dot * (i+1) + dot * (i) +
          str(dash*((M//2)-1-3*i)).ljust(((M//2)-1-3*i)))

print(str(dash*((M//2)-3)).rjust(((M//2)-3)) + 
      'WELCOME' +
      str(dash*((M//2)-3)).ljust(((M//2)-3)))

for i in reversed(range(N//2)):
    print(str(dash*((M//2)-1-3*i)).rjust(((M//2)-1-3*i)) +
          dot * (i+1) + dot * (i) +
          str(dash*((M//2)-1-3*i)).ljust(((M//2)-1-3*i)))
