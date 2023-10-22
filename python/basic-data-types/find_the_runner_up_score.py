# TODO: #1 Create artificial input data for this script.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list = sorted(list(set(arr)))
    
    print(list[-2])