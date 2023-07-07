import random


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('Enter your choice (rock/paper/scissors): ')
    print(f'You chose {user_choice}.')
    print(f'The computer chose {computer_choice}.')
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print('You lose!')
        else:
            print('You win!')
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print('You lose!')
        else:
            print('You win!')
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print('You lose!')
        else:
            print('You win!')
    else:
        print('Invalid input. Please try again.')

while True:
    rock_paper_scissors()
    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break
#Main DEV : Yousef Mohamad
