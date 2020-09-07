import random

#dealer has to hit until he has 17 or more

#creating deck and empty player hands
player_hand = []
dealer_hand = []
deck = [2,3,4,5,6,7,8,9,'K','Q','J','A'] * 4


def main():
    # making sure i can modify variables to reset when game is restarted
    global player_hand
    global dealer_hand
    global deck

    player_hand = []
    dealer_hand = []
    deck = [2,3,4,5,6,7,8,9,'K','Q','J','A'] * 4
    # setting the default choice value as hit
    choice = 'h'

    dealHand()
    print('\n\n\nWelcome to Blackjack!')
    # looping for as long as the player wants to hit
    while choice == 'h' or choice == 'hit':
        print(f'\nyour hand: {player_hand}')
        print(f'Dealer\'s hand: {dealer_hand[0]}, ?\n')
        blackjack(player_hand)

        choice = input('[h]it or [s]tand? ').lower()
        while choice != 'h' and choice != 's':
            choice = input('[h]it or [s]tand? ').lower()

        if choice == 'h' or choice == 'hit':
            #calling the hit function for a new card and the blackjack/bust functions to see if player hit either
            hit(player_hand)
            blackjack(player_hand)
            bust(player_hand)
    # loop for dealer to hit as long as they are under 17 points
    while checkScore(dealer_hand) < 17:
        hit(dealer_hand)
        print(f'Dealer\'s hand: {dealer_hand}')

    print(f'\nyour hand: {player_hand}')
    print(f'Dealer\'s hand: {dealer_hand}\n')
    gameStatus()

    again = input('Would you Like to play again?(y/n)')
    while again.lower != 'y' and again.lower != 'n':
        again = input('Play again? (y/n)')
    if again.lower() == 'y':
            main()
    else:
            exit()

    


def dealHand():
    # hand = random.choices(deck, k=2)
    global player_hand
    global dealer_hand

    random.shuffle(deck)
    # dealing 2 cards to each player and removing those cards from the deck
    for i in range(2):  
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

def hit(hand):
    # same thing as the function above but with one card
    random.shuffle(deck)
    hand.append(deck.pop())


def checkScore(hand):
    total = 0
    # converting kings queens and jacks to 10s and aces to 11s then adding up the rest of the numbers
    for c in hand:
        if  c == 'Q' or c=='J' or c == 'K':
            total += 10
        elif c == 'A':
            total += 11
        else:
            total += c
    return total

    
def blackjack (hand):
    # checking if player got a blackjack
    if checkScore(hand) == 21:
        print(f'\nYour hand: {hand}')
        print("Blackjack!")
        again = input('Play again? (y/n)')
        while again.lower() != 'y' and again.lower() != 'n':
            again = input('Play again? (y/n)')
        if again.lower() == 'y':
            main()
        else:
            exit()
        
def bust(hand):
    #checking if player busted
    if checkScore(hand) > 21:
        print(f'\nYour hand: {hand}')

        print('it\'s a bust.')
        again = input('Play again? (y/n)')
        while again.lower() != 'y' and again.lower() != 'n':
            again = input('Play again? (y/n)')
        if again.lower() == 'y':
            main()
        else:
            exit()

def gameStatus():
    # checking end results and if dealer busted (really ineffiecient part here)
    if checkScore(dealer_hand) > 21:
        print('Dealer bust\n You win!')
    if checkScore(dealer_hand) > checkScore(player_hand):
        print('you loose')
    if checkScore(dealer_hand) < checkScore(player_hand):
        print('congratulations you won')
    if checkScore(dealer_hand) == checkScore(player_hand):
        print('It\'s a tie!')

    
        


main()