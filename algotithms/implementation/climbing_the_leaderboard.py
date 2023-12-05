'''
Challenge: Climbing the Leaderboard
Difficulty: Medium
Topic: Problem Solving (Basic)
Max Score: 20
Success Rate: 60.71%
Task: Help Alice track her progress toward the top of the leaderboard!
Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
'''

# Imports
import requests
import tempfile
from time import time
from io import StringIO

# Simulate input from HackerRank
raw_data = '''7
100 100 50 40 40 20 10
4
5 25 50 120
'''
    # Expected Output:
    # 6
    # 4
    # 2
    # 1

raw_data = '''6
100 90 90 80 75 60
5
50 65 77 90 102
'''
    # Expected Output:
    # 6
    # 5
    # 4
    # 2
    # 1

raw_data = '''100
295 294 291 287 287 285 285 284 283 279 277 274 274 271 270 268 268 268 264 260 259 258 257 255 252 250 244 241 240 237 236 236 231 227 227 227 226 225 224 223 216 212 200 197 196 194 193 189 188 187 183 182 178 177 173 171 169 165 143 140 137 135 133 130 130 130 128 127 122 120 116 114 113 109 106 103 99 92 85 81 69 68 63 63 63 61 57 51 47 46 38 30 28 25 22 15 14 12 6 4
200
5 5 6 14 19 20 23 25 29 29 30 30 32 37 38 38 38 41 41 44 45 45 47 59 59 62 63 65 67 69 70 72 72 76 79 82 83 90 91 92 93 98 98 100 100 102 103 105 106 107 109 112 115 118 118 121 122 122 123 125 125 125 127 128 131 131 133 134 139 140 141 143 144 144 144 144 147 150 152 155 156 160 164 164 165 165 166 168 169 170 171 172 173 174 174 180 184 187 187 188 194 197 197 197 198 201 202 202 207 208 211 212 212 214 217 219 219 220 220 223 225 227 228 229 229 233 235 235 236 242 242 245 246 252 253 253 257 257 260 261 266 266 268 269 271 271 275 276 281 282 283 284 285 287 289 289 295 296 298 300 300 301 304 306 308 309 310 316 318 318 324 326 329 329 329 330 330 332 337 337 341 341 349 351 351 354 356 357 366 369 377 379 380 382 391 391 394 396 396 400
# '''
    # Expected Output:
    # 88
    # 88
    # 87
    # 85
    # ...
    # 1
    # 1
    # 1
    # 1

# raw_data = requests.get('https://hr-testcases-us-east-1.s3.amazonaws.com/29530/input07.txt?response-content-type=text%2Fplain&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAR6O7GJNX5DNFO3PV%2F20231205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231205T195021Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=c9592693ddb39d4b296fbece58b2cdfe7b2dc1f4bd0883f62b15291b4769a31e').text


# Data
input = StringIO(raw_data)

# Function
def climbingLeaderboard(ranked, player):
    '''
    Calculates the rank of each player in the leaderboard based on their scores.

    Parameters:
    ranked (list): A list of integers representing the scores of the players in the leaderboard.
    player (list): A list of integers representing the scores of the players to be ranked.

    Returns:
    list: A list of integers representing the ranks of the players in the leaderboard.
    '''
    def rerank(rank, cut=0):
        rank = rank[cut:]
        return sorted(set(rank))

    ranked = rerank(ranked)
    print('player:', player)
    print('ranked:', ranked)

    score, scores = 0, [0]
    for p in range(len(player)):
        # print(p, player[p])
        if player[p] < ranked[0]:
            score = len(ranked)+1
        elif player[p] == ranked[0]:
            score = len(ranked)
        else:
            for r in range(len(ranked)):
                if player[p] >= ranked[r]:
                    score = len(ranked)-r
        scores.append(score)
        ranked.append(player[p])
        ranked = rerank(ranked, -scores[-1])
        print('ranked', ranked)
        print('scores:', scores[1:])
        print('')

    return scores[1:]

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    ranked_count = int(input.readline().strip())

    ranked = list(map(int, input.readline().rstrip().split()))

    player_count = int(input.readline().strip())

    player = list(map(int, input.readline().rstrip().split()))

    tic = time()
    result = climbingLeaderboard(ranked, player)
    print(ranked[:10])
    tac = time()

    print('Runtime:', tac-tic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    print(result)