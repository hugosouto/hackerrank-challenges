# Imports
import textwrap
from io import StringIO

# Data
raw_data = """ABCDEFGHIJKLIMNOQRSTUVWXYZ
4"""

input = StringIO(raw_data)

# Solution
def wrap(string, max_width):
    return

# Main
if __name__ == '__main__':
    string, max_width = input.readline(), int(input.readline())
    result = wrap(string, max_width)
    print(result)