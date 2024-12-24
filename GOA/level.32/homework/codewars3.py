def fake_bin(x):
    result = ""
    for i in x:
        if int(i) >= 5:
            result += "1"
        else:
            result += "0"
    return result

#https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python