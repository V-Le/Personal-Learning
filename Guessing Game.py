import random

rannum = random.randint(0, 10)
print(rannum)
x = True

while x:
    try:
        user_guess = int(input('Guess the correct number between 1-9: '))
        while user_guess != rannum:
            if user_guess < rannum:
                print('Your number is too low!')
                user_guess = int(input('Guess again: '))
            elif user_guess > rannum:
                print('Your number is too high!')
                user_guess = int(input('Guess again: '))
        else:
            print('Correct Answer!')
            x = False
    except ValueError:
        print('Not a number.')
