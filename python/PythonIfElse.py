#!/bin/python3

import math
import os
import random
import re
import sys

from io import StringIO  # Import package to simulate HackerHack input

# Artificial data to simulate HackerRank sample input


class RandomNumbers:
    def random_numbers():

        n = random.randint(1, 20)
        print(f'Number of samples: {n}')

        list = []
        for _ in range(n):
            number = random.randint(1, 101)
            # Print without new line
            print('number', number)

        return


random_numbers()


# sample_input = str(random_numbers())
# print(f'The sample input is:\n{random_numbers()}\n\nThe output is:')

# """

# Convert the string data to a file-like object
data_io = StringIO(sample_input)

# Number of test cases
n_tests = int(data_io.readline().strip())

# Conditions
# 1 < n < 100
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Solution
if __name__ == '__main__':

    @RandomNumbers.random_numbers
    def evaluate_numbers():
        for _ in range(n_tests):

            n = int(data_io.readline().strip())
            print(f'{n} is', end=' ')

            if n % 2 == 1:
                print('Weird')
            elif n >= 2 and n <= 5:
                print('Not Weird')
            elif n >= 6 and n <= 20:
                print('Weird')
            elif n > 20:
                print('Not Weird')
