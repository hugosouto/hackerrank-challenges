# TODO: #1 Create artificial input data for this script.

if __name__ == '__main__':
    n = int(input())

    seq = ''
    for i in range(n):
        seq += str(n-(n-i-1))
    
    print(seq)