from random import randint

def user_choice(options):
    for index,option in enumerate(options):
        print(f'{index} = {option}')
    user_input = int(input("What do you choose: "))
    return user_input

def computer_choice(options):
    computer_chose = randint(0,len(options)-1)
    return computer_chose

def check_results(options, player, computer):
    if(player==computer):
        return 'It\'s a tie'
    elif ((player==0 and computer==len(options)-1) or (player > computer and not(player==len(options)-1 and computer==0))):
        return 'You Won...'
    else:
        return 'You Lost...'
   
def play():
    print('''--------------------------------
Welcome to Rock, Paper, Scissor.
Please pick your weapon.
--------------------------------''')
    options_list = ['Rock', 'Paper' , 'Scissor']
    player_result = user_choice(options_list)
    if(player_result>=3):
        print("\nInvalid choice!!!!!!!\n")
    else:
        computer_result = computer_choice(options_list)

        print(f'Player selects: {options_list[player_result]}')
        print(f'Computer selects: {options_list[computer_result]}')

        result = check_results(options_list, player_result, computer_result)
        print(f'\n{result}\n')

def main():
    play_again = ""
    while play_again.lower() != 'n':
        play()
        print("Want to play again?")
        play_again = input("Press \'y\' for YES OR \'n\' for NO: ")
        print('\n')
main()
