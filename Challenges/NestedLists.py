if __name__ == '__main__':
    
    n = 5
    names0 = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    scores0 = [37.21, 37.21, 37.2, 41, 39]
    
    names = []
    scores = []

    for i in range(int(n)):
           
        names.append(names0[i])
        scores.append(scores0[i])

    # scores_set = sorted(list(set(scores)))
    # second_lowest = scores_set[1]
    second_lowest = sorted(list(set(scores)))[1]
    
    # print('scores_set: ' + str(scores_set))
    print('second_lowest: ' + str(second_lowest))
    
    # if second_lowest in scores:
        # print(names)


    # print(names[scores(second_lowest)])
    # print(x for names in n names[scores(second_lowest)])