# Expected Output

# Size 3
# 
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# Size 5
# 
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# Size 10
# 
# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

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
    
    print(
            str(dash*(paddding)).rjust(paddding) + 
            str(letters[size-1]) +
            str(dash*(paddding)).ljust(paddding)
        )
    
    for i in range(1, size-1):

        print(
            str(dash*(paddding-i*2)) + 
            dash.join(reversed(letters[size-1-i:size])) +
            dash +
            dash.join(letters[size-i:size]) +
            str(dash*(paddding-i*2)).ljust(paddding-i*2)
        )

    print(dash.join(reversed(letters[:size])) + dash + dash.join(letters[1:size]))

    for i in reversed(range(1, size-1)):

        print(
            str(dash*(paddding-i*2)) + 
            dash.join(reversed(letters[size-1-i:size])) +
            dash +
            dash.join(letters[size-i:size]) +
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