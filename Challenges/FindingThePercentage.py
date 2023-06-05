# Code stub
# 
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

# Artificial data
input = ('''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika''')

from statistics import mean
from io import StringIO

# Convert the string data to a file-like object
data_io = StringIO(input)

if __name__ == '__main__':
    
    # n = int(input())
    n = int(data_io.readline())
    student_marks = {}

    for _ in range(n):
        # name, *line = input().split()
        name, *line = data_io.readline().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = data_io.readline().strip()
    
    average_score = mean(student_marks[query_name])
    print("{:.2f}".format(average_score))