def validate_pin(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    elif len(pin) == 6 and pin.isdigit():
        return True
    else:
        return False
    
# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python