# Imports
import random
import string
from io import StringIO

# Data
# size = random.randint(1, 26)
size = 5

input = StringIO(str(size))

# Solution
def print_rangoli(size):
    
    dash = "-"
    # letters = string.ascii_lowercase
    letters = [dash]
    letters.extend(string.ascii_lowercase)
    # print(letters)
    
    for i in range(size-1):
        print(dash.rjust(size//2) + 
            dash*(size//2) +
            letters[size-i] +
            dash*(size//2) +
            str(dash.ljust(size//2))
        )
    
    print(dash.join(reversed(letters[1:size+1])))

    for i in reversed(range(size-1)):
        print(dash.rjust(size//2) + 
            dash*(size//2) +
            letters[size-i] +
            dash*(size//2) +
            str(dash.ljust(size//2))
        )
    return

# Main
if __name__ == '__main__':
    n = int(input.readline())
    print_rangoli(n)