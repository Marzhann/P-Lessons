# Practice 8
#Rock-Paper-Scissors game. Let`s have some fun

while True:
    in_1 = input('So, player 1...Rock, Paper or Scissors? : ')
    in_2 = input('Player 2, please...Rock, Paper, Scissors : ')
    if in_1 == 'Rock' and in_2 == 'Paper':
        print('Paper beats Rock! Player 2 you won! Yoohoo')
    elif in_1 == 'Rock' and in_2 == 'Scissors':
        print('Rock beats Scissors! Player 1 you won!')
    elif in_1 == 'Paper' and in_2 == 'Rock':
        print('Paper beats Rock! Player 1 won!')
    elif in_1 == 'Paper' and in_2 == 'Scissors':
        print('Scissors beats Paper! Player 2 win!')
    elif in_1 == 'Scissors' and in_2 == 'Rock':
        print('Rock beats Scissors! Player 2 win!')
    elif in_1 == 'Scissors' and in_2 == 'Paper':
        print('Scissors beats Paper! Player 1 win!')
    elif in_1 == in_2:
        print('Ooops! you have joint minds... Do it again')
    else:
        print('Come on... We have only Rock Paper and Scissors! No more weapon is allowed')
    in_again = input('Wanna fight again? Y/N :')
    if in_again == 'Y':
        print('Let`s start!')
    elif in_again == 'N':
        break
    else:
        print('WTF?')

