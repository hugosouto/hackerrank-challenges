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

if __name__ == '__main__':

    # Artificial data
    l1 = str('3')
    l2 = str('Krishna 67 68 69')
    l3 = str('Arjun 70 98 63')
    l4 = str('Malika 52 56 60')
    l5 = str('Malika')

    n = l1
    student_marks = {}
    for _ in 'l' + str(_) in range(2, 5):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = l5

    print(student_marks)