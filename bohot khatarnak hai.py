def Calc(string):
    String = []
    num = ''
    for char in string:
        if char == '+' or char == '-' or char == '*' or char == '/':
            String.append(int(num))
            String.append(char)
            num = ''
        else:
            num += char
    String.append(int(num))
    return String
