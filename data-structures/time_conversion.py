#!/bin/python3


# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Sample Input
raw_data = '07:05:45PM'

# Data
input = StringIO(raw_data)

# Solution
def timeConversion(s):
    # *Write your code here
    return ''

# Main
if __name__ == '__main__':

    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    s = input.readline()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
