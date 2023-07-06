# Imports
import tempfile
from io import StringIO

# Data
raw_data = """4
3 2 1 3"""

input = StringIO(raw_data)

# Solution
def birthdayCakeCandles(candles):
    highest_num = max(candles)
    return candles.count(highest_num)

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
        
    candles_count = int(input.readline().strip())

    candles = list(map(int, input.readline().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
