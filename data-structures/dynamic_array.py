#!/bin/python3

# Imports
from io import StringIO

# Sample Input
raw_data = """2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1"""

# Data
input = StringIO(raw_data)

# Solution
def dynamicArray(n, queries):
    
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
    
        if query[0] == 1:
           idx = (query[1] ^ lastAnswer) % n
           arr[idx].append(query[2])

        if query[0] == 2:
            idx = (query[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            print(lastAnswer)

# Main
if __name__ == '__main__':

    first_multiple_input = input.readline().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = [list(map(int, input.readline().rstrip().split())) for _ in range(q)]

    dynamicArray(n, queries)