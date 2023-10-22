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
size = random.randint(1, 26)
# size = 1

input = StringIO(str(size))

# Solution
def print_rangoli(size):
    alphabet = [chr(i) for i in range(97,123)]
    alphabet = alphabet[:size]
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1]
    
    for i in indices:
        start_index = i + 1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = "-".join(row)
        width = size * 4 - 3
        row = row.center(width,"-")
        print(row)

# Main
if __name__ == '__main__':
    n = int(input.readline())
    print_rangoli(n)