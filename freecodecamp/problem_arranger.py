
# !!! SUCCESS !!!
# CODE NEEDS ORGANIZED

def arithmetic_arranger(problems, showsum=True):


    #DECLARING ROW VARIABLES
    top = []
    bottom = []
    operator = []
    allsums = [] #optional sum row
    

    #CHECKS ERRORS
    errors = ""
    if len(problems) > 5: #check if maximum problems are reached
        return "Error: Too many problems."
    for problem in problems: #splits each problem into workable sections
        section = problem.split()

        if not section[0].isnumeric() or not section[2].isnumeric():
            errors = "Error: Numbers must only contain digits."
            return errors
        if len(section[0]) > 4 or len(section[2]) > 4:
            errors = "Error: Numbers cannot be more than four digits."
            return errors
        if section[1] != '+' and section[1] != '-':
            errors = "Error: Operator must be '+' or '-'."
            return errors

        sum = 0
        if section[1] == '+': #calculates sums for later
            sum = int(section[0]) + int(section[2])
        elif section[1] == '-':
            sum = int(section[0]) - int(section[2])
        else:
            continue
            
        top.append(section[0]) #store values in their correct rows
        operator.append(section[1])
        bottom.append(section[2])
        allsums.append(sum)


    #FIND LENGTHS OF ROWS
    top_length = []
    bottom_length = []
    full_length = [] #problem + operator max character length

    for i in top:
        top_length.append(len(i))

    for i in bottom:
        bottom_length.append(len(i))

    for i in range(len(top_length)): #finds max length and adds spaces
        if top_length[i] >= bottom_length[i]:
           full_length.append(top_length[i])
        else:
            full_length.append(bottom_length[i])

        full_length[i] = int(full_length[i]) + 2


    #CONVERT ROW LISTS TO STRINGS
    top_string = ''
    bottom_string = ''
    flat_string = ''
    sum_string = ''

    for i in range(len(problems)): #arranging and building the strings
        top_string += str(top[i]).rjust(full_length[i]) + '    ' 
        bottom_string += str(operator[i]) + str(bottom[i]).rjust(full_length[i] - 1) + '    ' #adds operator and space to bottom row
        flat_string += '-' * full_length[i] + '    '
        sum_string += str(allsums[i]).rjust(full_length[i]) + '    ' #also adds column spacing between problems
        
    top_string = top_string.rstrip() #strips the end of white spaces
    bottom_string = bottom_string.rstrip()
    flat_string = flat_string.rstrip()
    sum_string = sum_string.rstrip()
    arranged_problems = top_string + '\n' + bottom_string + '\n' + flat_string #builds complete string
    if showsum is True: #checks for show answer option
        arranged_problems += '\n' + sum_string
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))