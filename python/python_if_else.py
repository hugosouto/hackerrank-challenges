#!/bin/python3

import math
import os
import random
import re
import sys

# Given an integer, n, perform the following conditional actions:
# 1 < n < 100
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Solution:
if __name__ == '__main__':

    # Artificial data to simulate HackerRank sample input
    n = random.randint(1, 20)

    print(f'{n} is', end=' ')

    if n % 2 == 1:
        print('Weird')
    elif n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')