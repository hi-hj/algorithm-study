import pprint


def grade(score):
    if 90<=score: return 'A'
    elif 80<=score<90: return 'B'
    elif 70<=score<80: return 'C'
    elif 50<=score<70: return 'D'
    else: return 'F'

def solution(scores):
    answer = ''
    n = len(scores)
    for j in range(n):
        score = []
        for i in range(n):
            score.append(scores[i][j])

        if score[j] == max(score) and score.count(score[j])==1:
            score.pop(j)
        elif score[j] == min(score) and score.count(score[j])==1:
            score.pop(j)

        avg = sum(score) / len(score)

        answer += grade(avg)

    print(answer)


solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])