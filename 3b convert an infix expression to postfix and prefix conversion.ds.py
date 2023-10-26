OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities

def infix_to_postfix(expression):  # input expression
    stack = []  # initially stack empty
    output = ''  # initially output empty

    for ch in expression:
        if ch not in OPERATORS:  # if an operand, put it directly in the postfix expression
            output += ch
        elif ch == '(':  # else operators should be put in stack
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            # Lesser priority can't be on top of higher or equal priority, so pop and put in output
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output

def reverse(string):
    string = string[::-1]
    return string

expression = input('Enter infix expression:\n')
print('Infix expression: ', expression)
postfix = infix_to_postfix(expression)
print('Postfix expression: ', postfix)
prefix = reverse(postfix)
print('Prefix expression:', prefix)
