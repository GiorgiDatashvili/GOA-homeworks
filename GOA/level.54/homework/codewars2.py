def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    if begin_number==end_number:
        return end_number
    else:
        return begin_number + sequence_sum(begin_number+step,end_number,step)
# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python