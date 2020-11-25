from lexical_analyzer.main_analyzer import analyze

if __name__ == '__main__':

    assignment_statements = []

    # get string statements from file
    with open('test-cases.txt', 'r') as file:
        for line in file:
            assignment_statements.append(line.rstrip('\n'))
    
    # lexically analyze
    validation_results = analyze(assignment_statements)

    # display results
    for statement, validation in zip(assignment_statements, validation_results):
        
        print (f'\n{statement}   -> {validation}')
        print('-----------------------------------------')