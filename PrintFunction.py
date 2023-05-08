if __name__ == '__main__':
    n = int(input())

    seq = ''
    for i in range(n):
        seq += str(n-(n-i-1))
    
    print(seq)