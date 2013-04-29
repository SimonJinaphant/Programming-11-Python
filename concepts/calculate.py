from sys import argv
precedence = {'*':3, '/':3, '+':2, '-':2, '(':1}

def toPostfix(expression):
    operator_stack = []
    postfix_stack = []

    for symbol in expression.split():
        if symbol.isdigit():
            postfix_stack.append(symbol)
            
        elif symbol == '(':
            operator_stack.append(symbol)
            
        elif symbol == ')':
            symbol = operator_stack.pop()
            
            while symbol != '(':
                postfix_stack.append(symbol)
                symbol = operator_stack.pop()

        else:
            if operator_stack and precedence[operator_stack[-1]] >= precedence[symbol]:
                postfix_stack.append(operator_stack.pop())
                
            operator_stack.append(symbol)
         
        print "Postfix Stack = {0}\nOperator Stack = {1}\n".format(postfix_stack, operator_stack)
     
    
    postfix_stack.extend(operator_stack[::-1])
    print "Postfix = {0}\n".format(postfix_stack)
    return postfix_stack


def calculate(postfix_expression):
    number_stack = []    

    for symbol in postfix_expression:
        if symbol.isdigit():
            number_stack.append(int(symbol))
        else:
            result = operate(symbol)(number_stack.pop(), number_stack.pop())
            number_stack.append(result)
        print "Number Stack = {0}".format(number_stack)

    return number_stack[0]


def operate(operator):
    if operator == '+':
        return lambda x, y : x + y
        
    elif operator == '-':
    	#Subtraction is un-commutative
        return lambda x, y : y - x
        
    elif operator == '*':
        return lambda x, y : x * y
        
    else:
    	#Division is also un-commutative
        return lambda x, y : y / x

print calculate(toPostfix(argv[1]))
