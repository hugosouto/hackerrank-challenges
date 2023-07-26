#!/bin/python3

# Imports
import math
import os
import random
import re
import sys
import tempfile
import string
from io import StringIO

# Sample Input
# raw_data = "chris alan"
# raw_data = "1 w 2 r  3g"
raw_data = "132 456 Wq  m e"

# Data
input = StringIO(raw_data)

# Solution
def solve(s):

    list = []
    for i in s.split(' '):
        
        if len(i) == 0:
            i = ''
        elif i[0] in string.digits:
            pass
        else:
            i = i.title()

        list.append(i)

    final_string = str(' '.join(list))

    return final_string

# Main
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    s = input.readline()

    result = solve(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
