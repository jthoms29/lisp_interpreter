
"""
An attempt at writing a Scheme Lisp interpreter
"""

class interpreter:
    __current_str = ""
    __operations = {}
    
    def __init__(self):
        self.__current_str = ""
        self.__operations: dict[str, function] = \
                {'+': self.add, '-': self.subtract, '*': self.multiply, \
                 '/': self.divide}


    """
    Implementation of the addition operator
    """
    def add(self, a, b) -> int:
        return a + b

    """
    Implementation of the subtraction operator
    """
    def subtract(self, a, b) -> int:
        return a - b

    """
    Implementation of the multiplication operator
    """
    def multiply(self, a, b) -> int:
        return a * b

    """
    Implementation of the division operator
    """
    def divide(self, a, b) -> float:
        return a * b
    
    

    def evaluate(self, statement:list):
        keys = self.__operations.keys()
        oper_key:str = ''
        arg1:int = 0
        arg2:int = 0
        for c in statement:
            if c in keys and oper_key == '':
                oper_key = c
            elif arg1 == '':
                arg1 = int(c)
            elif arg2 == '':
                arg2 = int(c)

        operation:function =  self.__operations.get(oper_key)
        return operation(arg1, arg2)




    
    """
    Parse the current input string. Will need to keep track of nested
    parentheses
    """
    def parse_string(self, inp:str) -> None:
        inp_split = inp.split()
        # this stack will contain tuples corresponding to parentheses
        # type as well as string index. This will allow nested parentheses
        # to be easily split and evaluated
        stack = []
        inp_len = len(inp_split)

        for i in range(inp_len):
            if inp_split[i] == '(':
                stack.append(i)
            if inp_split[i] == ')':
                open_paren = stack.pop()
                nested_statement = inp_split[open_paren, i]
                val = evaluate(nested_statement)


    """
    Get input from the user, a line to parse
    """
    def get_input(self) -> None:
        self.__current_str = input();

    
