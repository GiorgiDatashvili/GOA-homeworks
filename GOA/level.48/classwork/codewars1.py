def xo(s):
    new_str = s.lower()
    if new_str.count("x") == new_str.count("o"):
        return True
    else:
        return False
# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python