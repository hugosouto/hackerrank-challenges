'''
Challenge: collections.Counter()
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 10
Success Rate: 97.44%
Task: Use a counter to sum the amount of money earned by the shoe shop owner.
Problem: https://www.hackerrank.com/challenges/collections-counter/problem
'''

# Imports
from collections import Counter
from io import StringIO

# Simulate input from HackerRank
raw_data = '''10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
# Expected Output
# 200

# Data
input = StringIO(raw_data)

# Solution
def total_sales(total_amount, shoes, size, value):
    print(value)
    if shoes[size] > 0:
        total_amount += value
    return shoes, total_amount

# Main
if __name__ == '__main__':
    X = int(input.readline().strip())
    sizes = [int(i) for i in list(input.readline().split())]
    print('Sizes:', sizes)
    N = int(input.readline().strip())

    # print(X, N, shoes, sep='\n')
    shoes = dict(Counter(sizes))
    print('Shoes:', shoes)

    total_amount = 0
    for i in range(N):
        size, value = [int(i) for i in list(input.readline().split())]
        print(size, value)
        total_sales(total_amount, shoes, size, value)

    print(total_amount)