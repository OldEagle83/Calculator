# write your code here
# Message initialization
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
yes = ['y', 'Y']
no = ['n', 'N']
mem = ['m', 'M']

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

def is_one_digit(v):
    if 10 > v > -10 and float(v).is_integer():
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and v3 in ['*', '+', '-']:
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)




while not flag:
    flag_1 = False
    string = input(msg_0)
    string_list = string.split()
    x = is_num(string_list[0])
    y = is_num(string_list[2])
    oper = is_oper(string_list[1])
    if x[1] in mem:
        x[0] = True
        x[1] = memory
    if y[1] in mem:
        y[0] = True
        y[1] = memory
    if not x[0] or not y[0]:
        print(msg_1)

    if x[0] and y[0] and oper[0]:
        x = x[1]
        y = y[1]
        oper = oper[1]
        check(x, y, oper)
        flag = True

        if y == 0 and oper == '/':
            print(msg_3)
            flag = False
        else:
            result = oper_ac(x, oper, y)
            print(result)
            answer_4 = input(msg_4)
            while not flag_1:
                if answer_4 in yes:
                    memory = result
                    answer_5 = input(msg_5)
                    if answer_5 in yes:
                        flag = False
                        flag_1 = True
                    elif answer_5 in no:
                        break
                elif answer_4 in ['n', 'N']:
                    answer_5 = input(msg_5)
                    if answer_5 in yes:
                        flag = False
                        flag_1 = True
                    elif answer_5 in no:
                        break

