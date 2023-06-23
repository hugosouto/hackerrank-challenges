# TODO: #1 Create artificial input data for this script.

# Original version
# 
# It uses a for loop to print each value in separated line.

if __name__ == '__main__':

    names = []
    scores = []

    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))

    second_lowest = sorted(list(set(scores)))[1]

    indices = [index for index, score in enumerate(scores) if score == second_lowest]
    result = [names[index] for index in indices]

    for name in sorted(result):
        print(name)

# Refactored version
#
# It uses a list comprehension to print each value in separated line.
# 
#  The code does the following:
# 1. Create a list of names and scores
# 2. Find the second lowest score
# 3. Create a list of indices of the second lowest score
# 4. Create a list of names for the second lowest score
# 5. Sort the names and print each name on a new line """

if __name__ == '__main__':

    # Artifitial data
    n = 5
    names0 = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    scores0 = [37.21, 37.21, 37.2, 41, 39]

    names = []
    scores = []

    for i in range(n):

        names.append(names0[i])
        scores.append(scores0[i])

    second_lowest = sorted(list(set(scores)))[1]

    indices = [index for index, score in enumerate(scores) if score == second_lowest]
    result = [names[index] for index in indices]

    print(*sorted(list(result)), sep="\n")