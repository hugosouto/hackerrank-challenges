# Imports
import tempfile
from io import StringIO

# Sample Input
raw_data = '07:05:45PM'

# Data
input = StringIO(raw_data)

# Solution
def timeConversion(s):
    
    if s[8:10] == 'AM' and s[0:2] == '12':
        s = s.replace(s[0:2], str(int(s[0:2]) - 12).zfill(2))
    
    if s[8:10] == 'PM' and s[0:2] == '12':
        s = s.replace(s[0:2], str(int(s[0:2]) - 12).zfill(2))

    if s[8:10] == 'PM':
        s = s.replace(s[0:2], str(int(s[0:2]) + 12).zfill(2))
    
    s = s[0:8]

    return s

# Main
if __name__ == '__main__':

    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    s = input.readline()
    
    result = timeConversion(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()