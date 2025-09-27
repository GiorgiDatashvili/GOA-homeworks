def maskify(cc):
    if len(cc) > 4:
        h = len(cc) - 4 
        masked_part = "#" * h  
        visible_part = cc[-4:]  
        cc = masked_part + visible_part  

    return cc

# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python