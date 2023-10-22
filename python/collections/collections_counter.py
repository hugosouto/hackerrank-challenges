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

    if size in shoes.keys():
        if shoes[str(size)] > 0:
            total_amount += int(value)
            shoes[str(size)] -= 1

    return total_amount

# Main
if __name__ == '__main__':
    X = int(input.readline().strip())
    sizes = list(input.readline().split())
    N = int(input.readline().strip())
    shoes = dict(Counter(sizes))

    total_amount = 0
    sizes, values = [], []
    for i in range(N):
        size, value = input.readline().split()
        sizes.append(size)
        values.append(value)
        total_amount = total_sales(total_amount, shoes, size, value)

    print(total_amount)