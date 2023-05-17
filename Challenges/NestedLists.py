# Original version
# 
# It uses a for loop to print each value in separated line.

if __name__ == '__main__':
    
    names = []
    scores = []
    
    for x in range(int(input())):
        names.append(input())
        scores.append(float(input()))
    
    second_lowest = sorted(list(set(scores)))[1]

    indices = [index for index, score in enumerate(scores) if score == second_lowest]
    result = [names[index] for index in indices]
    
    for name in sorted(result):
        print(name)