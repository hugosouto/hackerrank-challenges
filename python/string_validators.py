from io import StringIO

raw_data = "qA2"

input = StringIO(raw_data)

if __name__ == '__main__':
    s = input.readline()

    v = 'False'
    for _ in s:
        if str.isalnum(s) == True: 
            v = 'True'
    print(v)
    
    v = 'False'
    for _ in s:
        if str.isalpha(s) == True:
            v = 'True'
    print(v)
    
    v = 'False'
    for _ in s:
        if str.isdigit(s) == True:
            v = 'True'
    print(v)
    
    v = 'False'
    for _ in s:
        if str.islower(s) == True:
            v = 'True'
    print(v)
    
    v = 'False'
    for _ in s:
        if str.isupper(s) == True:
            v = 'True'
    print(v)
    