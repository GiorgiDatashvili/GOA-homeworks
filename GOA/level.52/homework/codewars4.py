def remove_consecutive_duplicates(s : str) -> str:
    words = s.split()
    result = []
    last_word = None
    for word in words:
        if word != last_word:  
            result.append(word)
            last_word = word  
    return ' '.join(result)

# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python