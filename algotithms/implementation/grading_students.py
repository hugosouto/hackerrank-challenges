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
    """
    This function receives a list of grades and returns a new list with the rounded grades according to the following rules:
    - If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    - If the value of grade is less than 38, no rounding occurs.
    :param grades: list of integers representing the grades.
    :return: list of integers representing the rounded grades.
    """
    new_grades = []

    for i in grades:
        if i >= 38 and i % 5 >= 3:
            i = i + 5-(i % 5)
        else:
            i = i
        new_grades.append(i)

    return new_grades

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    grades_count = int(input.readline().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input.readline().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
