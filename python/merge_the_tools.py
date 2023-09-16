'''
Challenge: Merge the Tools!
Difficulty: Medium
Topic: Python (Basic)
Max Score: 40
Success Rate: 93.72%
Task: Split a string into subsegments of length $k$, then print each subsegment
with any duplicate characters stripped out.
Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

# Imports
from io import StringIO

# Simulate HackerRank Input Data

# Problem example data:
raw_data = '''AAABCADDE
3'''
# Expected output:
# A
# BCA
# DE

# Test case data:
# raw_data = '''AABCAAADA
# 3'''

input = StringIO(raw_data)

# Solution
def merge_the_tools(string, k):
    print(string, k)

# Main
if __name__ == '__main__':
    string, k = input.readline(), int(input.readline())
    merge_the_tools(string, k)