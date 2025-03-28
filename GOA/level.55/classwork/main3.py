def vashlebi(sia):
    result = []
    last_word = None
    for word in sia:
        if word != last_word:  
            result.append(word)
            last_word = word  
    return result
