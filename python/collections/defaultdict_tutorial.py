'''
Challenge: DefaultDict Tutorial
Difficulty: Easy
Topic: Python (Basic)
Max Score: 20
Success Rate: 92.99%
Task: Create dictionary value fields with predefined data types.
Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''

# Example
# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# Imports
from collections import defaultdict
from io import StringIO

# Simulate input from HackerRank
raw_data = '''5 2
a
a
b
a
b
a
b
'''
    # Expected Output:
    # 1 3
    # -1

# Data
input = StringIO(raw_data)

# Function
d = defaultdict(list)
def function(word, lst):
    for i in A:
        if word is in lst:
            d['A'].append(A[i])

# Main
if __name__ == '__main__':
    n, m = map(int, input.readline().split())
    n_inputs = (n+m)

    A = []

    for i in range(n_inputs):
        word = str(input.readline().strip())
        if i < n:
            A.append(word)

        function(word, A)

    print(d['A'])