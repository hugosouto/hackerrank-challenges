# Imports
import random
import string
import textwrap
from io import StringIO

# Function for Input Generation
def get_random_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))

str_lenth = random.randint(1, 100)
result_str = get_random_string(str_lenth)
max_width = random.randint(1, str_lenth)  # Make sure max_width is not larger than the string length

# Input Simulation
raw_data = (f'{result_str}\n{max_width}')

input = StringIO(raw_data)

# Solution
def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)

# Main
if __name__ == '__main__':
    string, max_width = input.readline(), int(input.readline())
    result = wrap(string, max_width)
    print(result)