
"""
An attempt at writing a Scheme Lisp interpreter
"""

class interpreter:
    __current_str = ""

    def __init__(self):
        self.__current_str = ""

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

    
    """
    Parse the current input string. Will need to keep track of nested
    parentheses
    """
    def parse_string(self, inp:str) -> None:
        # this stack will contain tuples corresponding to parentheses
        # type as well as string index. This will allow nested parentheses
        # to be easily split and evaluated

        stack = []
        inp_len = len(inp)
        


        

    """
    Get input from the user, a line to parse
    """
    def get_input(self) -> None:
        self.__current_str = input();

    
