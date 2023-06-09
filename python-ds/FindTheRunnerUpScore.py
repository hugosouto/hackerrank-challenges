if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list = sorted(list(set(arr)))
    
    print(list[-2])