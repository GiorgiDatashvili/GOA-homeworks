def rps(p1, p2):
    if len(p1) == 8 and len(p2) == 5:
        return "Player 1 won!"
    elif len(p1) == 8 and len(p2) == 4:
        return "Player 2 won!"
    elif len(p1) == 5 and len(p2) == 4:
        return "Player 1 won!"
    elif len(p1) == 4 and len(p2) == 5:
        return "Player 2 won!"
    elif len(p1) == 4 and len(p2) == 8:
        return "Player 1 won!"
    elif len(p1) == 5 and len(p2) == 8:
        return "Player 2 won!"
    elif p1 == p2:
        return "Draw!"
    
# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
