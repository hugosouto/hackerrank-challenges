# Imports
import random
import string
from io import StringIO

# Data
# size = random.randint(1, 26)
size = random.randint(5, 10)

input = StringIO(str(size))

# Solution
def print_rangoli(size):
    
    letters = string.ascii_lowercase
    dash = "-"
    paddding = (size-1)*2
    # letters = [dash]
    # letters.extend(string.ascii_lowercase)
    # print(letters)
    
    for i in range(size-1):
        
        print(str(dash*(paddding)).rjust(paddding) + 

            letters[size-1-i] +
            
            str(dash*(paddding)).ljust(paddding)
        )
    
    print(dash.join(reversed(letters[:size])) + dash + dash.join(letters[1:size]))

    for i in reversed(range(size-1)):

        print(str(dash*(paddding)).rjust(paddding) + 
            
            letters[size-1-i] +
            
            str(dash*(paddding)).ljust(paddding)
        )
    return

# Main
if __name__ == '__main__':
    n = int(input.readline())
    print_rangoli(n)