import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHO', 5: 'GO', 6: 'ROKU'}

print("""In this traditional Japanese dice game,
two dice are rolled in a bamboo cup by the
dealer. The player must guess if the dice total
to an even (cho) or odd (han) number.""")

purse = 5000
while True:
    print(f'You have {purse} mon.How much do you bet? (or (q)uit)')
    while True:
        bet = input('> ')
        if bet.upper() == 'q':
            print('Thanls for playing!')
            break
        elif not bet.isdecimal():
            print('Bet is not a number.')
        elif int(bet) > purse:
            print('You don\'t have enough to make that bet')
        else:
            bet = int(bet)
            break
    house_cut = bet * 0.1

    print("""he dealer swirls the cup and you hear
    the rattle of the dice. The dealer slams the cup
    on the floor, still covering the dice and ask for your bet.""")

    print('CHO (even) or HAN (odd)?')
    guess = input('> ')


    dice1_value = random.randint(1, 6)
    dice2_value = random.randint(1, 6)

    dice1_japanese = JAPANESE_NUMBERS[dice1_value]
    dice2_japanese = JAPANESE_NUMBERS[dice2_value]

    total_sum = dice1_value + dice2_value

    print(f'The deal lifts the cup to reveal:\n{dice1_japanese} - {dice2_japanese}')
    print(f'{dice1_value} - {dice2_value}')

    roll_even = total_sum % 2 == 0

    if roll_even:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    player_won = bet == correct_bet

    if player_won:
        print(f'You won! You get {bet - house_cut} mon.')
        purse += bet
        print(f'The house collects a {bet * 0.1} mon fee.')
        purse -= house_cut
    else:
        print(f'You lost {bet} mon.')
        purse -= bet

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        break
        

