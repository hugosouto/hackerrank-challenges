if __name__ == '__main__':
    
    n = 5
    names0 = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    scores0 = [37.21, 37.21, 37.2, 41, 39]
    
    names = []
    scores = []

    for i in range(int(n)):
           
        names.append(names0[i])
        scores.append(scores0[i])

    second_lowest = sorted(list(set(scores)))[1]

    indices = [index for index, score in enumerate(scores) if score == second_lowest]
    result = [names[index] for index in indices]
    
    for name in sorted(result):
        print(name)
