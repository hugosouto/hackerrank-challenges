from io import StringIO

raw_input = ('''ABCDCDC
CDC''')

input = StringIO(raw_input)

def count_substring(string, sub_string):    
    
    indexes = []

    for i in range(0, len(string)):
        indexes.append(string.find(sub_string, i, i+len(sub_string)))

    valid_indexes = [i for i in indexes if i != -1]

    return len(valid_indexes)

if __name__ == '__main__':
    
    string = input.readline().strip()
    sub_string = input.readline().strip()
    
    count = count_substring(string, sub_string)
    print(count)