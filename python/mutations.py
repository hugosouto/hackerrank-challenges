from io import StringIO

raw_input = ('''abracadabra
5 k''')

input = StringIO(raw_input)

def mutate_string(string, position, character):
    return string[0:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input.readline()
    i, c = input.readline().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)