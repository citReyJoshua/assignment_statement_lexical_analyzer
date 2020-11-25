'''
    Every function modifies largest_match_count value.
    largest_match_count receives the count of which state_machine matched the most.
'''
def identifier(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2, 1, 2),
        (1, 1, 1, 2),
        (2, 2, 2, 2),
    ]    

    while i != length:
        if string_input[i].isalpha():
            input = 0
        elif string_input[i].isdigit():
            input = 1
        elif string_input[i] == '_':
            input = 2
        else:
            input = 3
        
        state = table[state][input]
        
        if state == 2:
            break
        
        i += 1
    
    if i > largest_match_count[0]:
         largest_match_count[0] = i
    
    return i

def operator(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2),
        (2, 2),
        (2, 2)
    ]
    
    
    while i != length:
        if string_input[i] in ['+', '-', '/', '*', '%']:
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        
        if state == 2:
            break
        
        i += 1
        
    
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def integer(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2),
        (1, 2),
        (2, 2)
    ]
    
    while i != length:
        if string_input[i].isdigit():
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        if state == 2:
            break
        i += 1
        
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i
    
def float(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0
    
    table = [
        (1, 0, 3),
        (3, 2, 3),
        (3, 2, 3),
        (3, 3, 3),
    ]

    while i != length:
        if string_input[i] == '.':
            input = 0
        elif string_input[i].isdigit():
            input = 1
        else:
            input = 2
    
        state = table[state][input]
        if state == 3:
            break
        i += 1
    
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def character(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 4),
        (4, 2),
        (3, 4),
        (4, 4),
        (4, 4)
    ]

    while i != length:
        if string_input[i] == "'":
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        
        if state == 4:
            break
        
        i += 1
    
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def string(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 3),
        (2, 1),
        (3, 3),
        (3, 3)
    ]

    while i != length:
        if string_input[i] == '"':
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        if state == 3:
            break
        
        i += 1
        
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def whitespace(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2),
        (1, 2),
        (2, 2),
    ]

    while i != length:
        if string_input[i] == ' ':
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        if state == 2:
            break
        
        i += 1
        
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def equals(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2),
        (2, 2),
        (2, 2),
    ]

    while i != length:
        if string_input[i] == '=':
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        if state == 2:
            break
        
        i += 1
        
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i

def semicolon(string_input, largest_match_count, index, length):
    i = index[0]
    state = 0

    table = [
        (1, 2),
        (2, 2),
        (2, 2),
    ]

    while i != length:
        if string_input[i] == ';':
            input = 0
        else:
            input = 1
        
        state = table[state][input]
        if state == 2:
            break
        
        i += 1
        
    if i > largest_match_count[0]:
        largest_match_count[0] = i
    
    return i