from io import StringIO

raw_input = ('''ABCDCDC
CDC''')

input = StringIO(raw_input)

def count_substring(string, sub_string):
    return

if __name__ == '__main__':
    string = input.readline().strip()
    sub_string = input.readline().strip()
    
    count = count_substring(string, sub_string)
    print(count)