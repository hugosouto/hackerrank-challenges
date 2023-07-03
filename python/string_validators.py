from io import StringIO

raw_data = "qA2"

input = StringIO(raw_data)

if __name__ == '__main__':
    s = input.readline()

    alnum, alpha, digit, lower, upper = 'False', 'False', 'False', 'False', 'False'

    for _ in s:

        if str.isalnum(s) == True:
            alnum = 'True'
            break

        if str.isalpha(s) == True:
            alpha = 'True'
            break
  
        if str.isdigit(s) == True:
            digit = 'True'
            break

        if str.islower(s) == True:
            lower = 'True'
            break

        if str.isupper(s) == True:
            upper = 'True'
            break
    
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)