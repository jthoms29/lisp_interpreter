
"""
An attempt at writing a Scheme Lisp interpreter
"""

class interpreter:
    current_str = ""
    operations = {}
    
    def __init__(self):
        self.current_str = ""
        self.operations = \
                {'+': self.add,
                 '-': self.subtract,
                 '*': self.multiply,
                 '/': self.divide}


    """
    Implementation of the addition operator
    """
    def add(self, a, b):
        return a + b

    """
    Implementation of the subtraction operator
    """
    def subtract(self, a, b):
        return a - b

    """
    Implementation of the multiplication operator
    """
    def multiply(self, a, b):
        return a * b

    """
    Implementation of the division operator
    """
    def divide(self, a, b):
        return a // b
   

    def define(self, a):
        a = 3


    def evaluate(self, statement:list) -> int:
        keys = self.operations.keys()
        oper_key:str = ''
        arg1:int = 0
        arg2:int = 0

        for c in statement:
            if c in keys:
                oper_key = c
                continue

            if oper_key == '':
                print("Invalid")
                return 0

            if arg1 == 0:
                arg1 = int(c)

            elif arg2 == 0:
                arg2 = int(c)

        ret = self.operations[oper_key](arg1, arg2)
        print(ret)
        return ret


    """
    Parse the current input string. Will need to keep track of nested
    parentheses
    """
    def parse_string(self, inp:str) -> None:
        # separate opening/closing terms from parentheses,
        # split the input string at spaces, 
        inp = inp.replace('(', '( ')
        inp = inp.replace(')', ' )')
        inp_split = inp.split(" ")

        # this stack will contain tuples corresponding to parentheses
        # type as well as string index. This will allow nested parentheses
        # to be easily split and evaluated
        stack: list[int] = []

        i:int = 0
        while i < len(inp_split):
            if inp_split[i] == '(':
                stack.append(i)
            if inp_split[i] == ')':
                open_paren = stack.pop()
                nested_statement = inp_split[open_paren+1:i]
                nest_len = len(nested_statement)
                val = self.evaluate(nested_statement)
                del inp_split[open_paren:i]
                i -= nest_len + 1
                inp_split[i] = str(val)
            
            i+= 1

    """
    Get input from the user, a line to parse
    """
    def get_input(self) -> None:
        strn = input();
        self.parse_string(strn)


test = interpreter()
test.__init__()
while True:
    test.get_input()
