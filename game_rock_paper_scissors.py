from random import randint

def win():
    return ('You win!')

def lose():
    return ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move=randint(0,2)
    moves=["rock","paper","scissors"]
    computer_choice=(moves[random_move])

    if player_choice == computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice== 'scissors':
        print(win())
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print(lose())
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print(win())
    elif player_choice == 'scissors' and computer_choice== 'rock':
        print((lose))
    elif player_choice == 'paper' and computer_choice == 'rock':
        print(win())
    elif player_choice == 'rock' and computer_choice == 'rock':
        print(lose())
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'n':
        break