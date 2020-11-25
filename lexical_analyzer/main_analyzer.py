from .token_identifier import identify_token
from . import tokens
def analyze(string_list):

    validation_results = []

    table = [
        (1, 5, 5, 5, 5, 5, 5, 5, 0, 5),
        (5, 2, 5, 5, 5, 5, 5, 5, 1, 5),
        (3, 5, 3, 3, 3, 3, 5, 5, 2, 5),
        (5, 5, 5, 5, 5, 5, 2, 4, 3, 5),
        (5, 5, 5, 5, 5, 5, 5, 5, 4, 5),
        (5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    ]

    for string in string_list:

        index = [0] # int index wrapped in a list to be passed as reference
                    # python does not allow passing by reference of primitive data types such as int and float
        state = 0
        length = len(string)

        while index[0] != length:

            token = identify_token(string, index, length)

            if token == tokens.IDENTIFIER:
                input = 0
            elif token == tokens.EQUALS:
                input = 1
            elif token == tokens.INT:
                input = 2
            elif token == tokens.CHAR:
                input = 3
            elif token == tokens.FLOAT:
                input = 4
            elif token == tokens.STRING:
                input = 5
            elif token == tokens.OPERATOR:
                input = 6
            elif token == tokens.SEMICOLON:
                input = 7
            elif token == tokens.SPACE:
                input = 8
            else: 
                input = 9

            state = table[state][input]
            if (state == 5):
                break

        validation_results.append('Valid' if state == 4 else 'Invalid')

    return validation_results
