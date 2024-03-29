
 
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
# raw_data = '''5 3
# 1 2 100
# 2 5 100
# 3 4 100
# '''
    # Expected Output:
    # 200

# Import txt files as string
# raw_data = open('C:\\Users\\Hugo\\GitHub\\hackerrank-challenges\\data-structures\\arrays\\array_manipulation_test_case_3.txt', 'r').read()
    # Expected Output:
    # 6314

raw_data = open('C:\\Users\\Hugo\\GitHub\\hackerrank-challenges\\data-structures\\arrays\\array_manipulation_test_case_6.txt', 'r').read()
    # Expected Output:
    # 7515267971

# raw_data = '''4 3
# 2 3 603
# 1 1 286
# 4 4 882
# '''
    # Expected Output:
    # 882

# Data
input = StringIO(raw_data)

# Function
# def recAddQuery(remaining, query, arr):
#     if remaining == 0:
#         return arr
#     else:
#         num_to_add = queries[query][2]
#         slice = arr[queries[query][0]-1:queries[query][1]]
#         arr[queries[query][0]-1:queries[query][1]] = (i + num_to_add for i in slice)
#     return recAddQuery(remaining-1, query+1, arr)

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
    # return max(arr)

    # Version 2
    # arr = [0] * n
    # for q in range(len(queries)):
    #     slice = arr[queries[q][0]-1:queries[q][1]]
    #     add = queries[q][2]
    #     arr[queries[q][0]-1:queries[q][1]] = [i + add for i in slice]
    # return max(arr)

    # Version 3
    # arr = [0] * n
    # for q in range(len(queries)):
        # slice = arr[queries[q][0]-1:queries[q][1]]
        # add = queries[q][2]
        # arr[queries[q][0]-1:queries[q][1]] = map(lambda x: x + add, slice)
    # return max(arr)

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
    # return max(arr)

    # Version 4 (with Recursive Function)
    # arr = [0] * n
    # query = 0
    # remaining = len(queries) - query
    # recAddQuery(remaining, query, arr)
    # return max(arr)

    # Version 5 (ChatGPT-based)
    # arr = [0] * n
    # for query in queries:
    #     a, b, k = query
    #     arr[a-1:b] = [i + k for i in arr[a-1:b]]
    # return max(arr)

    # Version 6 (ChatGPT-based)
    # arr = [0] * n
    # for query in queries:
    #     a, b, k = query
    #     for i in range(a-1, b):
    #         arr[i] += k
    # return max(arr)

    # Version 7 (ChatGPT-based)
    # arr = [0] * n
    # for query in queries:
    #     a, b, k = query
    #     for x in range(b-(a-1)):
    #         arr[(a-1) + x] += k
    # return max(arr)

    # Version 8 (with Prefix Sum, ChatGPT-assisted)
    arr = [0] * n
    for query in queries:
        a, b, k = query
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    
    max_value = 0
    current_sum = 0
    for val in arr[:]:
        current_sum += val
        max_value = max(max_value, current_sum)
    
    return max_value

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