# Imports
import tempfile
from io import StringIO


# Artificial data
input = ('''6
1 2 3 4 10 11''')

# print(input)

# Convert the string data to a file-like object
data_io = StringIO(input)


# Solution
def simpleArraySum(ar):
    # ar_sum = np.sum(ar)
    # return ar_sum
    return sum(ar)

if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w', delete=True)

    ar_count = int(data_io.readline().strip())
    ar = list(map(int, data_io.readline().split()))
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()

    print(result)