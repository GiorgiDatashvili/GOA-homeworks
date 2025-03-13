def series_sum(n):
    answer = 1
    if n > 1:
        for i in range(1,n):
            answer += (1/(1+(i*3)))
    elif n == 1:
        answer == 1
    if n >= 1:
        return f"{answer:.2f}"
    else:        
        return "0.00"
    
# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python