def geometric_sequence_elements(a, r, n):
    list = []
    for i in range(n):
        list.append(str(a))
        a *= r
    return ", ".join(list)

# https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python