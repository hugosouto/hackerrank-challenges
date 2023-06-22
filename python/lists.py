'''
Instructions

Consider a list (list = []). You can perform the following commands:
- insert i e: Insert integer  at position .
- print: Print the list.
- remove e: Delete the first occurrence of integer .
- append e: Insert integer  at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.


Challenge

Initialize your list and read in the value of  followed by  lines of commands
where each command will be of the  types listed above. Iterate through each 
command in order and perform the corresponding operation on your list.


Original Stub Code by HackerRank

if __name__ == '__main__':
    N = int(input())
'''

# Import package to simulate HackerHack input
from io import StringIO

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
coco
print
''')

# Convert the string data to a file-like object
data_io = StringIO(input)

# My Solution
if __name__ == '__main__':
    N = int(data_io.readline())

    list = []

    for _ in range(N):
        command = data_io.readline().split()

        if command[0] == 'insert':
            list.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(list)
        elif command[0] == 'remove':
            list.remove(int(command[1]))
        elif command[0] == 'append':
            list.append(int(command[1]))
        elif command[0] == 'pop':
            list.pop()
        elif command[0] == 'reverse':
            list.reverse()
        elif command[0] == 'sort':
            list.sort()
        else:
            print(f"Command not recognized: '{command[0]}'")