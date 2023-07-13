# Imports
import random

# Data
input = random.randint(1, 99)

# Solution
def print_formatted(number):
    padding = len(str(bin(number)[2:]))
    for i in range(1, number + 1):
        print(str(int(i)).rjust(padding),  
              str(oct(i))[2:].rjust(padding),
              str(hex(i)).upper()[2:].rjust(padding),
              str(bin(i))[2:].rjust(padding))

# Main
if __name__ == '__main__':
    n = int(input)
    print_formatted(n)