import re

def parsemath(statement):
    pattern = re.compile("^(\-?\d+(\.\d+)?)\s*([+*/-])\s*(\-?\d+(\.\d+)?)$")
    m = pattern.match(statement)
    if m:
        operand1 = float(m.group(1))
        operator = m.group(3)
        operand2 = float(m.group(4))
        if operator == "+":
            return operand1 + operand2
        if operator == "-":
            return operand1 - operand2
        if operator == "*":
            return operand1 * operand2
        if operator == "/":
            if operand2 == 0:
                raise ValueError("Division durch 0 ist verboten.")
            return operand1 / operand2
    else:
        raise ValueError("Invalid statement.")

if __name__ == '__main__':
    print("Rechenaufgaben im Format <Operand1> <+,-,*,/> <Operand2> oder x = Ende.")
    while True:
        statement = input("> ")
        if statement == "x":
            break
        try:
            print(parsemath(statement))
        except ValueError as e:
            print(e)
