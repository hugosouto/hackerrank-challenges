
 
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
from io import StringIO

# Simulate input from HackerRank
raw_data = '''5 3
1 2 100
2 5 100
3 4 100
'''
    # Expected Output:
    # 200

# Data
input = StringIO(raw_data)

# Function
def arrayManipulation(n, queries):
    '''
    Perform `n` operations on an array and return the maximum of the values.
    '''
    print(n, queries)
    
    arr = [0] * n
    # arr = [0 for _ in range(n)]
    # arr = [10, 20,  30, 40, 50]
    print('arr:', arr)
    
    for q in range(len(queries)):
        print('\nquery:', queries[q])
        slice = arr[queries[q][0]-1:queries[q][1]]
        print('slice:', slice)
        add = queries[q][2]

        # print('slice 1:', slice)
        print('add:', add)
        arr[queries[q][0]-1:queries[q][1]] = [e + add for e in slice]
        print('arr:', arr)

        # for i in arr[queries[q][0]:queries[q][2]]:
            # slice += queries[q][2]


        # print(arr[queries[q][0]:queries[q][2]])
        # print(queries[q][2])

        # for i in range(2):
            # print('i:', i)
            # print(queries[q][i]) # += queries[q][2]
            # print(arr)

    result = max(arr)
    return result

    # print(n, queries)
    
    # arr = [0 for _ in range(n)]
    # print(arr)
    
    # for q in queries:
    #     for i in range(q[0]-1, q[1]):
    #         arr[i] += q[2]
    #         print(arr)

    # result = max(arr)
    # return result

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