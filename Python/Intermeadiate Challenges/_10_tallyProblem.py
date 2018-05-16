# 5 Friends (let's call them a, b, c, d and e) are playing a game
# and need to keep track of the scores. Each time someone
# scores a point, the letter of his name is typed in lowercase.
# If someone loses a point, the letter of his name is typed in
# uppercase. Give the resulting score (from highest to lowest).


players = ['a', 'b', 'c', 'd', 'e']
scores = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
scoreInput = 'dbbaCEDbdAacCEAadcB'


def getScore(list):
    scoreList = []
    for chr in list:
        scoreList.append(chr)
    count = 0
    while len(scoreList) > 0:
        for player in players:
            for score in scoreList:
                if score == player:
                    count += 1
                    scoreList.remove(score)
                    scores[score] += count
                elif score == player.upper():
                    scores[score.lower()] -= 1
                    scoreList.remove(score)
                count = 0

    return scores


print(getScore(scoreInput))
