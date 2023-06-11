# Imports
import math
import os
import random
import re
import sys

import tempfile
from io import StringIO


# Artificial data
input = ('''4
1 4 3 2''')

print(input)


# Convert the string data to a file-like object
data_io = StringIO(input)


# Solution
def reverseArray(a):
    return a[::-1]
    # Alternative solution
    # a.reverse()
    # return a
    

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.

    # Create a temporary file
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    arr_count = int(data_io.readline().strip())
    arr = list(map(int, data_io.readline().split()))
    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()

    print(res)