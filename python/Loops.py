'''
# Task
The provided code stub reads and integer, n, from STDIN. 
For all non-negative integers i < n, print i^2.

# Example
The list of non-negative integers that are less than n = 3 is [0, 1, 2]. 
Print the square of each number on a separate line.
'''

# Solution
import random

# if __name__ == '__main__':
if __name__ == '__main__':
    
    # Artificial data
    n = random.randint(1, 21)
    print(f'The number is: {n}.')

    # Print the square of each number on a separate line
    for i in range(n):
        print(i**2)