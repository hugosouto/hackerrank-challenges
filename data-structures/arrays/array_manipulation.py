
 
'''
Challenge: Array Manipulation
Difficulty: Hard
Topic: Problem Solving (Intermediate)
Max Score: 60
Success Rate: 60.55%
Task: Perform m operations on an array and print the maximum of the values.
Problem: https://www.hackerrank.com/challenges/crush/problem
'''

# Imports
import math
import os
import random
import re
import sys
import tempfile
import time
from io import StringIO

# Simulate input from HackerRank
raw_data = '''5 3
1 2 100
2 5 100
3 4 100
'''
    # Expected Output:
    # 200

# Import txt files as string
raw_data = open('C:\\Users\\Hugo\\GitHub\\hackerrank-challenges\\data-structures\\arrays\\array_manipulation_test_case_3.txt', 'r').read()
    # Expected Output:
    # 6314
# raw_data = open('C:\\Users\\Hugo\\GitHub\\hackerrank-challenges\\data-structures\\arrays\\array_manipulation_test_case_6.txt', 'r').read()
    # Expected Output:
    # 7515267971

# Data
input = StringIO(raw_data)

# Function
def recAddQuery(remaining, query, arr):
    if remaining == 0:
        return arr
    else:
        num_to_add = queries[query][2]
        slice = arr[queries[query][0]-1:queries[query][1]]
        arr[queries[query][0]-1:queries[query][1]] = [i + num_to_add for i in slice]
    return recAddQuery(remaining-1, query+1, arr)

def arrayManipulation(n, queries):
    '''
    Perform `n` operations on an array and return the maximum of the values.
    '''
    
    # Version 1
    # arr = [0 for _ in range(n)]
    # for q in queries:
    #     for i in range(q[0]-1, q[1]):
    #         arr[i] += q[2]
    #         # print(arr)

    # Version 2
    # arr = [0] * n
    # for q in range(len(queries)):
    #     slice = arr[queries[q][0]-1:queries[q][1]]
    #     add = queries[q][2]
    #     arr[queries[q][0]-1:queries[q][1]] = [i + add for i in slice]
    
    # Version 3
    # arr = [0] * n
    # for q in range(len(queries)):
        # slice = arr[queries[q][0]-1:queries[q][1]]
        # add = queries[q][2]
        # arr[queries[q][0]-1:queries[q][1]] = map(lambda x: x + add, slice)

    # Version Extra (with NumPy)
    # import numpy as np
    # arr = np.zeros(n, dtype=int)
    # # arr = [1, 2, 3, 4, 5]
    # # print(arr)
    # for q in range(len(queries)):
    #     slice = arr[queries[q][0]-1:queries[q][1]]
    #     number_to_add = queries[q][2]
    #     # print(np.array(arr[queries[q][0]-1:queries[q][1]]).sum())
    #     arr[queries[q][0]-1:queries[q][1]] = list(map(lambda x: x + number_to_add, slice))
    
    # Version 4 - Recursive Function
        
    arr = [0] * n
    query = 0
    remaining = len(queries) - query

    recAddQuery(remaining, query, arr)
        
    result = max(arr)
    return result

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()