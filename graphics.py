
from os import system, name

# suits = ('hearts', 'spades', 'diamonds', 'clubs')

# ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
#          'jack', 'queen', 'king', 'ace')

# card_values = {'two': 2 , 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7,
#     'eight' : 8, 'nine' : 9, 'ten' : 10, 'jack' : 10, 'queen' : 10, 'king' : 10,
#     'ace' : 0 }   



# class Card:
#     '''
#     Class for creating each card.
#     '''

#     def __init__(self, rank, suit):
#         self.rank =  rank
#         self.value = card_values[rank]
#         self.suit = suit

#     def __str__(self):
#         return self.rank + ' of ' + self.suit + f' ({self.value})'  

#     def __int__(self):
#         return self.value       


# class Deck:
#     '''
#     Creates a card deck of 52 cards
#     '''
#     def __init__(self):
#         self.cards = []

#         for suit in suits:
#             for rank in ranks:
#                 created_card = Card(rank, suit)
#                 self.cards.append(created_card)

# deck = Deck()

def hand(cards):
    '''
    Function to display each players hand as card graphics
    '''

    def card_value():
        pass
        values = []
        suits = []
        for card in cards:
            if card.rank == 'jack':
                values.append('J ')
            elif card.rank == 'queen':
                values.append('Q ')
            elif card.rank == 'king':
                values.append('K ')
            elif card.rank == 'ace':
                values.append('A ')
            elif card.rank == 'ten':
                values.append(str(card.value))    
            else:
                values.append(str(card.value) + ' ')

            if card.suit =='hearts':
                suits.append('♥')
            elif card.suit =='clubs':
                suits.append('♣')
            elif card.suit == 'diamonds':
                suits.append('♦')
            elif card.suit == 'spades':
                suits.append('♠')

        return values, suits                      


    values, suits = card_value()
    if len(cards) ==2:
        print(f'''     _____________________
     |     |             |
     | {values[0]}  | {values[1]}          |
     |     |             |
     |     |             |
     |     |             |
     |     |      {suits[1]}      |
     |     |             |
     |     |             |
     |     |             |
     |     |           {values[1]}|
     |_____|_____________|
     ''')
    elif len(cards) ==3:
        print(f'''     __________________________
     |     |     |             |
     | {values[0]}  | {values[1]}  | {values[2]}          |
     |     |     |             |
     |     |     |             |
     |     |     |             |
     |     |     |      {suits[2]}      |
     |     |     |             |
     |     |     |             |
     |     |     |             |
     |     |     |           {values[1]}|
     |_____|_____|_____________|
     ''')
    elif len(cards) ==4:
        print(f'''     ________________________________
     |     |     |     |             |
     |{values[0]}   | {values[1]}  | {values[2]}  | {values[3]}          |
     |     |     |     |             |
     |     |     |     |             |
     |     |     |     |             |
     |     |     |     |      {suits[3]}      |
     |     |     |     |             |
     |     |     |     |             |
     |     |     |     |             |
     |     |     |     |           {values[3]}|
     |_____|_____|_____|_____________|
     ''')
    elif len(cards) == 5:
        print(f'''     ______________________________________
     |     |     |     |     |             |
     | {values[0]}  | {values[1]}  | {values[2]}  | {values[3]}  | {values[4]}          |
     |     |     |     |     |             |
     |     |     |     |     |             |
     |     |     |     |     |             |
     |     |     |     |     |      {suits[4]}      |
     |     |     |     |     |             |
     |     |     |     |     |             |
     |     |     |     |     |             |
     |     |     |     |     |           {values[4]}|
     |_____|_____|_____|_____|_____________|
     ''')


def clear_screen():
    '''
    Function to clear the screen.
    '''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def title():
    '''Clears the screen and displays the title banner.
    '''
    clear_screen()
    print("""

  .______    __          ___       ______  __  ___        __       ___       ______  __  ___ 
  |   _  \\  |  |        /   \\     /      ||  |/  /       |  |     /   \\     /      ||  |/  / 
  |  |_)  | |  |       /  ^  \\   |  ,----'|  '  /        |  |    /  ^  \\   |  ,----'|  '  /  
  |   _  <  |  |      /  /_\\  \\  |  |     |    <   .--.  |  |   /  /_\\  \\  |  |     |    <   
  |  |_)  | |  `----./  _____  \\ |  `----.|  .  \\  |  `--'  |  /  _____  \\ |  `----.|  .  \\  
  |______/  |_______/__/     \\__\\ \\______||__|\\__\\  \\______/  /__/     \\__\\ \\______||__|\\__\\
                                                   B Y :   R I C H A R D   W I L S O N                 """)


def game_info_bar(players_name, players_chips, match_num):
    print(f'''  ##########################################################################################  
  {players_name}      Chips ({players_chips})                                                 Match ({match_num})
  ##########################################################################################
  ''')


def show_hands(dealers_hand, players_hand, players_name):    

    print('     Dealer\'s Hand')
    hand(dealers_hand)

    print(f'     {players_name}\'s Hand')
    hand(players_hand) 
  
    print('''  ##########################################################################################  ''')


def bust():
    print('''                              ______   _   _   _____   _____   _ 
                              | ___ \\ | | | | /  ___| |_   _| | |
                              | |_/ / | | | | \\ `--.    | |   | |
                              | ___ \\ | | | |  `--. \\   | |   | |
                              | |_/ / | |_| | /\\__/ /   | |   |_|
                              \\____/   \\___/  \\____/    \\_/   (_)\n
                                   Press Enter to Continue!''')


def win():
    print('''                __   __  _____   _   _     _    _   _____   _   _   _   _   _ 
                \\ \\ / / |  _  | | | | |   | |  | | |_   _| | \\ | | | | | | | |
                  \\ /   | | | | | | | |   | |/\\| |   | |   | . ` | | | | | | |
                  | |   \\ \\_/ / | |_| |   \\  /\\  /  _| |_  | |\\  | |_| |_| |_|
                  \\_/    \\___/   \\___/     \\/  \\/   \\___/  \\_| \\_/ (_) (_) (_)\n
                                   Press Enter to Continue!''')


def lose():
    print('''            __   __  _____   _   _     _       _____   _____   _____   _   _   _ 
            \\ \\ / / |  _  | | | | |   | |     |  _  | /  ___| |_   _| | | | | | |
             \\ V /  | | | | | | | |   | |     | | | | \\ `--.    | |   | | | | | |
              \\ /   | | | | | | | |   | |     | | | |  `--. \\   | |   | | | | | |
              | |   \\ \\_/ / | |_| |   | |____ \\ \\_/ / /\\__/ /   | |   |_| |_| |_|
              \\_/    \\___/   \\___/    \\_____/  \\___/  \\____/    \\_/   (_) (_) (_)\n
                                   Press Enter to Continue!''')


def game_over():
    print('''                    _____   ___  ___  ___ _____   _____  _   _ ___________ 
                    |  __ \\ / _ \\ |  \\/  ||  ___| |  _  || | | |  ___| ___ \\
                    | |  \\// /_\\ \\| .  . || |__   | | | || | | | |__ | |_/ /
                    | | __ |  _  || |\\/| ||  __|  | | | || | | |  __||    / 
                    | |_\\ \\| | | || |  | || |___  \\ \\_/ /\\ \\_/ / |___| |\\ \\ 
                    \\____/\\_| |_/\\_|  |_/\\____/   \\___/  \\___/\\____/\\_| \\_|\n
                                    YOU ARE OUT OF CHPS!!!
                                   Press Enter to Continue!''')                                      

def rules():
    print('''   ########################################################################################
   #                                                                                      #
   #          Basic Blackjack Rules:                                                      #
   #                                                                                      #
   #  • The goal of blackjack is to beat the dealer's hand without going over 21.         #
   #  • Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.   #
   #    Each player starts with two cards, one of the dealer's cards is hidden until      #
   #    the end.                                                                          #
   #  • To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end     #
   #    your turn.                                                                        #
   #  • If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.  #
   #  • If you are dealt 21 from the start (Ace & 10), you got a blackjack.               #
   #  • Blackjack means you win 1.5 the amount of your bet.                               #
   #  • Dealer will hit until his/her cards total 17 or higher.                           #
   #  • Doubling is like a hit, only the bet is doubled and you only get one more card.   #
   #                                                                                      #
   ########################################################################################\n''')
# • Split can be done when you have two of the same card - the pair is split into
#   two hands.
# • Splitting also doubles the bet, because each new hand is worth the original bet.
# • You can only double/split on the first move, or first move of a hand created
#   by a split.
# • You cannot play on two aces after they are split.
# • You can double on a hand resulting from a split, tripling or quadrupling you bet.

# players_name = 'Richard'
# players_chips = 50
# match_num = 1
# dealers_hand = deck.cards[0:5]
# players_hand = deck.cards[0:5]


# title()
# game_over()
# game_info_bar(players_name, players_chips, match_num)
# show_hands(dealers_hand, players_hand)

