'''
Challenge: itertools.product()
Difficulty: Easy
Topic: Python (Basic)
Max Score: 10
Success Rate: 98.16%
Task: Find the cartesian product of 2 sets.
Problem: https://www.hackerrank.com/challenges/itertools-product/problem
'''

# Data
A = [1, 2]
B = [3, 4, 5]


# Exploration Exercises

# For Loop concatenation
print('For Loop iteration:')
lst = []
for a in A:
    for b in B:
        lst.append(str(a) + str(b))
print(lst)

# List Comprehension concatenation
print('List Comprehension iteration:')
print([str(a) + str(b) for a in A for b in B])

# Generator concatenation
print('Generator iteration:')
gen = (str(a) + str(b) for a in A for b in B)
print(list(gen))

# Itertools Product concatenation
from itertools import product
print('Itertools Product iteration:')
prd = product(A, B)
prd_lst = list(prd)
temp1 = []
for i in prd_lst:
    temp2 = []
    for j in list(i):
        temp2.append(str(j))
    temp1.append(''.join(temp2)) 
print(temp1)

# (x,y) for x in A for y in B)
# product(A, B) returns the same as (