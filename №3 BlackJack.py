'''BlackJack'''

import random, sys

HEARTS = chr(9829) # Символ 9829
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print('''BlackJack, by Xsibiter!
    Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
How much money do you want to start with?''')

    # Validate money input
    money = None  # Initialize money to None
    while money is None:
        try:
            money = int(input('Write down the number: '))
            if money < 500:  # Ensure the user starts with at least 500
                print("You must start with at least 500.")
                money = None  # Reset money to None to repeat the loop
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Main game loop
    while True:
        if money <= 0:
            print("You're broke!!!")
            print("Good thing you weren't playing with real money:)")
            print("Thanks for playing!")
            sys.exit()

        # Continue with the rest of the game logic...
        print('Money:', money)
        bet = getBet(money)

        # Give a dealer and a player two cards from a deck:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet:', bet)
        while True:  # Cycle ends when there is "stand" or overdecking
            displayHands(playerHand, dealerHand, False)
            print()

            # Check for overdecking
            if getHandValue(playerHand) > 21:
                break

            # Get player move: H, S, or D
            move = getMove(playerHand, money - bet)

            if move == 'D':
                # Player doubles down
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit or double down
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # Overdecking
                    continue

            if move in ('S', 'D'):
                # Stand or double down: end player's turn
                break

        # Dealer's moves
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # Dealer takes another card
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # Dealer overdecked
                input('Press Enter to continue...')
                print('\n\n')

        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # Check for Win/Loss
        if dealerValue > 21:
            print('You WIN!')
            money += bet
        elif (playerValue > 21) or (plaopsie, YOU lose!')
            money -=yerValue < dealerValue):
            print('O bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It is a tie. Half of the bet is gone.')
            money -= bet / 2

        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):
    min_bet = 500
    '''Спрашиваем у игрока, сколько он ставит на этот раунд'''
    while True: # KEEP ASKING
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('>').upper().strip()

        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()


        if not bet.isdecimal():
            continue

        bet = int(bet)
        if bet < min_bet:
            print(f'Bet must be at least {min_bet}.')
        elif bet > maxBet:
            print(f'Bet cannot be more than {maxBet}.')
        else:
            return bet

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet
        if bet < 0:
            print('Bet cannot be negative.')
def getDeck():
    '''Return a list of tuples(nominal)'''
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))  # Исправлено: убраны скобки после suit
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    '''Show dealer's and player's cards concealing one of the dealer's cards'''
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)  # Исправлено: вызов displayCards вместо displayHands
    else:
        print('Dealer: ???')
        #Concealing first card
        displayCards([BACKSIDE] + dealerHand[1:])  # Исправлено: скрываем только первую карту
    # Show player's cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)
def getHandValue(cards):
    '''Return values of cards. Figure cards '''
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        #if we can add 10 more with overdecking
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    #Show all of the cards from the list of cards
    rows = ['','','',''] # The text

    for i, card in enumerate(cards):
        rows[0] += '___' #Show the upper string of a card
        if card == BACKSIDE:
            # Show the backside
            rows[1] += '|## |  '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #Show the suit
            rank, suit = card # a card - a tuple
            rows[1] += '|{} |  '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}|  '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Спрашиваем, какой ход хочет сделать игрок, и возвращаем 'H', если он
     хочет взять еще карту, 'S', если ему хватит, и 'D', если он удваивает."""
    while True: #Wait for a needed turn
        moves =['(H)it', 'S(tand)']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):  # Исправлено: опечатка в переменной move
            return move
        if move == "D" and '(D)ouble down' in moves:
            return move

#If the program doesn't import but launches, initiating launch:
if __name__ == '__main__':
    main()
