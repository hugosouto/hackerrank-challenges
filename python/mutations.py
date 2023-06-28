from io import StringIO

raw_input = ('''abracadabra
5 k''')

input = StringIO(raw_input)

def mutate_string(string, position, character):
    return string[0:position] + character + string[position + 1:]

def mutate_string_alt(string, position, character):
    l = list(string)
    l[position] = str(character)
    new_string = ''.join(l)
    return new_string

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string

if __name__ == '__main__':
    s = input.readline()
    i, c = input.readline().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    s_new_alt = mutate_string_alt(s, int(i), c)
    print(s_new_alt)