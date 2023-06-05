if __name__ == '__main__':

    # Artificial data to simulate HackerRank input
    input = ('''3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika''')

    # Import package to simulate HackerHack input
    from io import StringIO

    # Convert the string data to a file-like object
    data_io = StringIO(input)

    # Modified HackerHack code stub
    n = int(data_io.readline())
    student_marks = {}

    for _ in range(n):
        name, *line = data_io.readline().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = data_io.readline().strip()
    
    # Solution
    average_score = sum(student_marks[query_name])/len(student_marks[query_name])
    print("{:.2f}".format(average_score))