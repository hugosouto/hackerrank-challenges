'''
Challenge: Introduction to Sets
Difficulty: Easy
Topic: Python (Basic)
Max Score: 10
Success Rate: 98.53% 
Task: Use the set tool to compute the average.
Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''

# Imports
from io import StringIO

# Simulate input from HackerRank
raw_data = '''10
161 182 161 154 176 170 167 171 170 174
'''
    # Expected Output:
    # 169.375

# Data
input = StringIO(raw_data)

# Function
def average(array):
    distinct_heights = set(array)
    n_distinct_heights = len(distinct_heights)
    result = sum(distinct_heights)/n_distinct_heights
    return result

# Main
if __name__ == '__main__':
    n = int(input.readline())
    arr = list(map(int, input.readline().split()))
    result = average(arr)
    print(result)