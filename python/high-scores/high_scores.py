def latest(scores):
    return scores[-1]


def personal_best(scores):
    highest = 0
    for score in scores:
        if score > highest:
            highest = score
    return highest


def personal_top_three(scores):
    # using reverse blob algorith
    n = len(scores)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if scores[j] < scores[j+1]:
                temp = scores[j]
                scores[j] = scores[j+1]
                scores[j+1] = temp
    return scores[:3]
