
from os import system, name


def hand(cards, is_dealer_cards = False, card_flip = True):
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
    
    if (len(cards) == 2) and (is_dealer_cards == True) and (card_flip == False):
        print(f'''     _____________________
     |     |             |
     | {values[0]}  | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |     | ^^^^^^^^^^^ |
     |_____|_____________|
     ''')
    elif len(cards) ==2:
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
     |     |     |           {values[2]}|
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


def show_hands(dealers_hand, dealer_total, players_hand, players_total,
               players_name, is_dealer_cards, card_flip):

    is_dealer_cards = True

    print(f'     Dealer\'s Hand   ({dealer_total})')
    hand(dealers_hand, is_dealer_cards, card_flip)

    print(f'     {players_name}\'s Hand   ({players_total})')
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
                                    YOU ARE OUT OF CHIPS!!!
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



