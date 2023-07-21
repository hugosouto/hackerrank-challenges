#!/bin/python3


# Imports
import math
import os
import random
import re
import sys
from io import StringIO

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Sample Input
raw_data = ''

# Data
input = StringIO(raw_data)

# Solution
def timeConversion(s):
    # *Write your code here
    return ''

# Main
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input.readline()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
