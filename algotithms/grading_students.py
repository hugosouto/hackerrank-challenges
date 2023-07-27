#!/bin/python3

# Imports
import tempfile
from io import StringIO

# Data
raw_data = '''4
73
67
38
33'''

# Input Simulation
input = StringIO(raw_data)

# Solution
def gradingStudents(grades):
    return ''

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    grades_count = int(input.readline().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input.readline().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
