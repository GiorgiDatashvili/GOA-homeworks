def abbrev_name(name):
    new_name = name.split()
    initial = []
    for i in new_name:
        initial.append(i[0])
    init = ".".join(initial)
    return init.upper()

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python