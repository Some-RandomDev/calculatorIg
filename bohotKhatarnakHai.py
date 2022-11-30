def Calc(string):
    
    expression = []
    num = ''
    for char in string:
        if char == '+' or char == '-' or char == '*' or char == '/':
            expression.append(int(num))
            expression.append(char)
            num = ''
        else:
            num += char
    expression.append(int(num))
    offset = 1
    if '/' in expression:
        for i in range(len(expression)):
            if expression[i-offset] == '/':
                expression[i-offset] = expression[i-offset-1]/expression[i-offset+1]
                expression.pop(i-offset-1)
                expression.pop(i-offset)
                offset +=2
    offset = 1
    if '*' in expression:
        for i in range(len(expression)):
            if expression[i-offset] == '*':
                expression[i-offset] = expression[i-offset-1]*expression[i-offset+1]
                expression.pop(i-offset-1)
                expression.pop(i-offset)
                offset +=2
    offset = 1
    if '+' in expression:
        for i in range(len(expression)):
            if expression[i-offset] == '+':
                expression[i-offset] = expression[i-offset-1]+expression[i-offset+1]
                expression.pop(i-offset-1)
                expression.pop(i-offset)
                offset +=2
    offset = 1
    if '-' in expression:
        for i in range(len(expression)):
            if expression[i-offset] == '-':
                expression[i-offset] = expression[i-offset-1]-expression[i-offset+1]
                expression.pop(i-offset-1)
                expression.pop(i-offset)
                offset +=2
        
    return expression[0]

