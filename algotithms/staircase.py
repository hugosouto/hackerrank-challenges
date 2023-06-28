#!/bin/python3

import math
import os
import random
import re
import sys
import random

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

input = random.randint(1, 101)

def staircase(n):
    
    for i in range(n):
        print(" " * (n - 1 - i) + "#" * (i + 1))

if __name__ == '__main__':
    n = int(input)

    staircase(n)