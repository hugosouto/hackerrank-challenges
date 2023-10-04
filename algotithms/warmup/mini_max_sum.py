#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

raw_input = "7 69 2 221 8974"

input = StringIO(raw_input)

def miniMaxSum(arr):
    min = sum(sorted(arr)[:4])
    max = sum(sorted(arr)[1:])
    return print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input.readline().rstrip().split()))

    miniMaxSum(arr)
