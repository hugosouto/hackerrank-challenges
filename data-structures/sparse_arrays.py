#!/bin/python3

'''
Sparse Arrays
Topic: Problem Solving (Basic)
Task: Determine the number of times a string has previously appeared.
Difficulty: Medium
Success Rate: 97.32%
Max Score: 25
Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem
'''

# Imports
import tempfile
from io import StringIO

# Data
raw_data = '''4
aba
baba
aba
xzxb
3
aba
xzxb
ab'''

# raw_data = '''13
# abcde
# sdaklfj
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# na
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# 5
# abcde
# sdaklfj
# asdjf
# na
# basdn'''

# Input Simulation
input = StringIO(raw_data)

# Solution
def matchingStrings(stringList, queries):
    """Determine the number of times a string has previously appeared."""
    
    # print(stringList)
    # print(queries)
    
    counts = []
    for q in queries:
        count = 0
        if q in stringList:
            count += 1 
        counts.append(count)
    # print(counts)

    return counts

# Main
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    stringList_count = int(input.readline().strip())

    stringList = []
    for _ in range(stringList_count):
        stringList_item = input.readline().strip()
        stringList.append(stringList_item)

    queries_count = int(input.readline().strip())
    
    queries = []
    for _ in range(queries_count):
        queries_item = input.readline().strip()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)
    print(res)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
