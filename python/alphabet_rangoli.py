# Imports
import random
import string
from io import StringIO

# Data
# size = random.randint(1, 26)
# size = random.randint(5, 10)
size = 10

input = StringIO(str(size))

# Solution
def print_rangoli(size):
    
    letters = string.ascii_lowercase
    dash = "-"
    paddding = (size-1)*2
    # letters = [dash]
    # letters.extend(string.ascii_lowercase)
    # print(letters)
    
    print(
            str(dash*(paddding)).rjust(paddding) + 
            str(letters[size-1]) +
            str(dash*(paddding)).ljust(paddding)
        )
    
    for i in range(1, size-1):

        print(
            str(dash*(paddding-i*2)).rjust(paddding-i*2) + 
            dash.join(reversed(letters[i-1]*(i))) +
            dash + str(letters[size-1-i]) + dash +
            dash.join(letters[i-1]*(i)) +
            str(dash*(paddding-i*2)).ljust(paddding-i*2)
        )

    print(dash.join(reversed(letters[:size])) + dash + dash.join(letters[1:size]))

    for i in reversed(range(1, size-1)):

        print(
            str(dash*(paddding-i*2)).rjust(paddding-i*2) + 
            dash.join(reversed(letters[i-1]*(i))) +
            dash + str(letters[size-1-i]) + dash +
            dash.join(letters[i-1]*(i)) +
            str(dash*(paddding-i*2)).ljust(paddding-i*2)
        )
    
    print(
        str(dash*(paddding)).rjust(paddding) + 
        str(letters[size-1]) +
        str(dash*(paddding)).ljust(paddding)
    )

    return

# Main
if __name__ == '__main__':
    n = int(input.readline())
    print_rangoli(n)