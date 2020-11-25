from . import tokens, finite_state_machines as fsm

def identify_token(string_input, index, length):
    
    largest_match_count = [index[0]] # turned into a list with one element so it may be passed as reference

    float_match_count = fsm.float(string_input, largest_match_count, index, length)
    int_match_count = fsm.integer(string_input, largest_match_count, index, length)
    char_match_count = fsm.character(string_input, largest_match_count, index, length)
    str_match_count = fsm.string(string_input, largest_match_count, index, length)
    id_match_count = fsm.identifier(string_input, largest_match_count, index, length)
    op_match_count = fsm.operator(string_input, largest_match_count, index, length)
    space_match_count = fsm.whitespace(string_input, largest_match_count, index, length)
    equals_match_count = fsm.equals(string_input, largest_match_count, index, length)
    sem_match_count = fsm.semicolon(string_input, largest_match_count, index, length)

    # check which function received the largest_match count and set token to appropriate token value
    if largest_match_count[0] == int_match_count:
        token = tokens.INT
    elif largest_match_count[0] == float_match_count:
        token = tokens.FLOAT
    elif largest_match_count[0] == char_match_count:
        token = tokens.CHAR
    elif largest_match_count[0] == str_match_count:
        token = tokens.STRING
    elif largest_match_count[0] == id_match_count:
        token = tokens.IDENTIFIER
    elif largest_match_count[0] == op_match_count:
        token = tokens.OPERATOR
    elif largest_match_count[0] == space_match_count:
        token = tokens.WHITESPACE
    elif largest_match_count[0] == equals_match_count:
        token = tokens.EQUALS
    elif largest_match_count[0] == sem_match_count: 
        token = tokens.SEMICOLON
    
    # index moves to last_index of the longest matching token
    index[0] = largest_match_count[0] 

    return token

