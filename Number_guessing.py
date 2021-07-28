from random import randint

def number_guessing(user_number, rand_number):
    flag = False
    while flag == False:
        if user_number == rand_number:
            print("\n \t\t\t\tYou are amazing!. You're number is correct.")
            flag = True
        elif user_number < rand_number:
            user_number = int(input("\n \t\t\t\tYour number is lower than my number \n\t\t\t\t Please choose another number: "))
        elif user_number > rand_number:
            user_number = int(input("\n \t\t\t\tYour number is higher than my number\n\t\t\t\t Please choose another number: "))

def robot_guessing(rand_number):
    flag = False
    count = 0
    while flag == False:
        computer_guess= randint(1, rand_number)
        if computer_guess < rand_number:
            count +=1
        elif computer_guess > rand_number:
            count +=1
        else:
            flag = True
            print('{} times to find the correct number!'.format(count))

def Run():
    limit = int(input('Please input the limit of your number: '))
    rand_number = randint(1, limit)
    user_number = int(input('Please input your number: '))

    number_guessing(user_number, rand_number)
    robot_guessing(rand_number)
Run()