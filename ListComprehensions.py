if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    # Data input for testing purposes
    x, y, z, n = 1, 2, 3, 3

    a, b, c = '', '', ''

    list = [[a, b, c] for a in [0, x, y, z] for b in [0, x, y, z] for c in [0, x, y, z] if sum([a, b, c]) != n]
    
    print(list)

    # Backlog:
        # Eliminate duplicates
        # Order list