# Original Stub Code by HackerRank
# 
# if __name__ == '__main__':
#     N = int(input())

# Artificial data to simulate HackerRank input
input = ('''12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
''')

# Import package to simulate HackerHack input
from io import StringIO

# Convert the string data to a file-like object
data_io = StringIO(input)

# My Solution
if __name__ == '__main__':
    N = int(data_io.readline())