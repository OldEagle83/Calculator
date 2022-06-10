# write your code here
# Message initialization
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

# Variable initialization
operators = ['+', '-', '*', '/']
flag = False
flag_1 = False
memory = 0

# Needs commenting

def is_num(x):
    '''Accepts x and checks if it's a number. Returns a LIST: [True/False, x]'''
    try:
        x = float(x)
    except:
        print(msg_1)
        return [False, x]
    return [True, x]

def oper_ac(x, oper, y):
    '''Handles +, -, *, / (oper) between two floats x, y and returns the result. Will produce an error if / 0!'''
    if oper == '/':
        result = x / y
    if oper == '+':
        result = x + y
    if oper == '-':
        result = x - y
    if oper == '*':
        result = x * y
    return result

def is_oper(oper):
    '''Checks if the input is an operator provided in the operators list.'''
    if oper not in operators:
        print(msg_2)
        return [False, oper]
    else:
        return [True, oper]


while flag == False:
    string = input(msg_0)
    string_list = string.split()
    x = is_num(string_list[0])
    y = is_num(string_list[2])
    oper = is_oper(string_list[1])
    if x[1] == 'M':
        x[0] = True
        x[1] = memory
    if y[1] == 'M':
        y[0] = True
        y[1] = memory

    if x[0] and y[0] and oper[0]:
        x = x[1]
        y = y[1]
        oper = oper[1]
        flag = True

    if flag == True:
        if y == 0 and oper == '/':
            print(msg_3)
            flag = False
        else:
            result = oper_ac(x, oper, y)
            print(result)
            answer = input(msg_4)
            while not flag_1:
                if answer == 'y' or answer == 'Y':
                    memory = result
                    answer = input(msg_5)
                    if answer == 'y' or answer == 'Y':
                        flag = False
                    elif answer == 'n' or answer =='N':
                        break


