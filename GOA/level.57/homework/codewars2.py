def reduce_fraction(fraction):
    b, a = sorted(fraction)
    while b:
        a, b = b, a % b
    return fraction[0] // a, fraction[1] // a

# https://www.codewars.com/kata/576400f2f716ca816d001614/train/python