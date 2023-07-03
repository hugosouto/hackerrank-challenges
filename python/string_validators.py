from io import StringIO

raw_data = "qA2"

input = StringIO(raw_data)

if __name__ == '__main__':
    s = input.readline()

    alnum, alpha, digit, lower, upper = 'False', 'False', 'False', 'False', 'False'

    for i in s:
        if str.isalnum(i) == True:
            alnum = 'True'
            break

    for i in s:
        if str.isalpha(i) == True:
            alpha = 'True'
            break

    for i in s:
        if str.isdigit(i) == True:
            digit = 'True'
            break

    for i in s:
        if str.islower(i) == True:
            lower = 'True'
            break

    for i in s:
        if str.isupper(i) == True:
            upper = 'True'
            break
    
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)