#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# Simulate input:
from io import StringIO

raw_input = ('''Hugo
Souto''')

input = StringIO(raw_input)

# Solution:
def print_full_name(first, last):
    return print(f"Hello {first.rstrip()} {last.rstrip()}! You just delved into python.")

if __name__ == '__main__':
    first_name = input.readline()
    last_name = input.readline()
    print_full_name(first_name, last_name)