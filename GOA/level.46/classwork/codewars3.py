def descending_order(num):
    num_str = str(num)
    num_list = list(num_str)
    num_list.sort(reverse=True) 
    sorted_string = "".join(num_list)
    return int(sorted_string)

# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python