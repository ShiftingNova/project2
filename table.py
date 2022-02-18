'''
Jordan Walker
CSC 110
Project 2
This programs creates a exponent table
'''
def repeated(char, N):
    '''
    this function repeats a character a certain number of times
    :param char: is a string value that is going to be repeated
    :param N: is the number of times it is going to be repeated
    :return: the character repeated N times as a new string variable
    '''
    i = 0
    x = ""
    while i < N:
        x = x + char
        i = i + 1
    return x
def padded(x,width):
    '''
    This function checks the how many digits are in the 
    :param x:
    :param width:
    :return:
    '''
    number = str(x)
    answer = number
    if len(number) > width:
        answer = repeated("*",width)
    return answer
def power(base, exponent):
    '''
    This function solves for the base to the exponent power
    :param base: is the base number
    :param exponent: is the number the base is raised to
    :return: a new interger variable of base to the exponent power
    '''
    i = 0
    x = 1
    if exponent < 0:
        return (-1)
    while i < exponent:
        x = x * base
        i = i + 1
    return x
def print_row(n, max_power, column_width):
    '''
    this function uses the power function and the repeated function to print the rows of the table
    :param n: is the number you want to raise
    :param max_power: is the max number you want to raise to
    :param column_width: the length of each column
    :return:
    '''
    i = 1
    while i <= max_power:
        x = power(n,i)
        answer = padded(x,column_width)
        '''
        if x>10 and x<100:
            y= 2
        elif x>100 and x<1000:
            y = 3
        elif x>1000 and x<100000:
            y = 4
        if y >column_width:
            space=""
            x = repeated("*",column_width)
        else:'''
        z = column_width-len(answer)
        space = repeated(" ",z)
        print("|"+space,end="")
        print(answer,end="")
        i=i+1
    print("|")
def print_table(max_value,max_power,column_width):
    '''
    This is going to use the three previous functions to print the exponent table
    :param max_value: is the max number you want to be raised
    :param max_power: is the number you want to raise the numbers two
    :param column_width: is the size of each column
    :return:
    '''
    length = (column_width*max_power)+(max_power+1)
    print(repeated("-",length))
    i = 1
    while i<=max_value:
        print_row(i,max_power,column_width)
        i = i+1
    print(repeated("=", length))
def main():
    print_table(4, 3, 2)
    print_table(6, 4, 2)

main()
