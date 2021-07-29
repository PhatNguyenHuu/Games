import random

# Check result
def check_result(user, machine_ans):
    if user == 'r' and machine_ans == 's' or user == 'p' and machine_ans == 'r' or user == 's' and machine_ans == 'p':
        return 'Congratualtion! You win!'
    elif user == 'r' and machine_ans == 'p' or user == 'p' and machine_ans == 's' or user == 's' and machine_ans == 'r':
        return 'Game over!'
    else:
        return 'Tie!'

def check_format(user, machine):
    for element in machine:
        if user in element:
            return True
    return False

def Rock_Paper_scissor():
    # Generate variables
    machine = (('r', 'rock'), ('p', 'paper'), ('s', 'scissor'))
    machine_ans = random.choice(machine)[0]
    user = input('Please choose:\n \n r: rock \t\t\t p: paper \t\t\t s:scissor \n Your choice: ')
    end = 0
    # Execute
    while end == 0:
        if check_format(user, machine) == False:
            user = input('Your input is not acceptable. Please change your input: ')
        else:
            for element in machine:
            # Convert user answer to the abbreviation form (r, p, s)
                if element[1] == user:
                    user = element[0]
            # If the result is tie. Do it again
            if check_result(user, machine_ans) == 'Tie!':
                user = input("We are tie! Let's do it again: ")
                machine_ans = random.choice(machine)[0]
            else:
                end = 1

    return check_result(user, machine_ans)
print(Rock_Paper_scissor())