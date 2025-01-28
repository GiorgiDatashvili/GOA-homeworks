def points(games):
    result = 0
    for i in games:
        if i[0] > i[-1]:
            result += 3
        elif i[0] == i[-1]:
            result += 1
        else:
            continue
    return result

# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python