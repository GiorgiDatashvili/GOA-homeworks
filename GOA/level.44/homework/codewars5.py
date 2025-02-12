def divisors(integer):
    result = list()

    for i in range (2,integer):
        if integer%i==0:
            result.append(i)
    
    if len(result) == 0:
        return str(integer) + " is prime"
    
    return result

# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python