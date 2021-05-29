#Black Jack Card Game

from random import shuffle
from os import name, system
import time

suits = ('hearts', 'spades', 'diamonds', 'clubs')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'jack', 'queen', 'king', 'ace')

card_values = {'two': 2 , 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7,
    'eight' : 8, 'nine' : 9, 'ten' : 10, 'jack' : 10, 'queen' : 10, 'king' : 10,
    'ace' : 0 }

class Card:
    '''
    Class for creating each card.
    '''

    def __init__(self, rank, suit):
        self.rank =  rank
        self.value = card_values[rank]
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit + f' ({self.value})'  

    def __int__(self):
        return self.value       


class Deck:
    '''
    Creates a card deck of 52 cards
    '''
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.cards.append(created_card)

    
    def __len__(self):
        return len(self.cards)
    

    def shuffle(self):
        shuffle(self.cards)


    def deal(self):
        return self.cards.pop(0)    



class Dealer:
    '''
    Defines dealer.
    '''
    def __init__(self, name = 'Dealer'):
        self.pot = 0
        self.name = name
        self.cards = []
        self.card_deck = Deck() 


    def sum_cards(self):
        total = 0
        for card in self.cards:
            total += card.value

        return total


    def sum_card_one(self):
        return dealer.cards[0].value

    def show_cards_one(self):
        return str(self.cards[0])

    def show_cards_all(self):    
        return ', '.join(str(card).title() for card in self.cards) 




class Player:
    '''
    class that defines a player
    '''
    def __init__(self,name = 'player', chips = 50):
        self.chips = chips
        self.name = name
        self.bet_chips = 0
        self.cards = []

    def new_name(self):
        user_input = ''
        while len(user_input) <1:
            user_input = input('    Enter Name: ')
            self.name = user_input    


    def bet(self, chips):
        self.chips -= chips
        self.bet_chips = chips
        

    def sum_cards(self):
        total = 0
        for card in self.cards:
            total += card.value

        return total           


    def play_menu(self,):
        '''
        Function to call the player options.
        '''

        options = ('b', 'h', 's', 'q')

        user_input = ''
        while user_input not in options:
            user_input = input('   Enter: ').lower()

        if user_input == 'b':
            self.bet()

        elif user_input == 'h':
            player.cards.append(deck.deal())
            pass #check if bust

        elif user_input == 's':
            pass

        elif user_input == 'q':
            main_menu() 


    def show_cards_all(self):
        return ', '.join(str(card).title() for card in self.cards)        



def clear_screen():
    '''
    Function to clear the screen.
    '''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def title():
    '''
    Function to show the Title screen.
    '''
    clear_screen()
    print('''
    ______  _               _       ___               _     _ 
    | ___ \\| |             | |     |_  |             | |   | |
    | |_/ /| |  __ _   ___ | | __    | |  __ _   ___ | | __| |
    | ___ \\| | / _` | / __|| |/ /    | | / _` | / __|| |/ /| |
    | |_/ /| || (_| || (__ |   < /\\__/ /| (_| || (__ |   < |_|
    \\____/ |_| \\__,_| \\___||_|\\_\\ ____/  \\__,_| \\___||_|\\_\\(_)\n
        ''')  


def main_menu():
    '''
    Function to call the main menu options.
    '''
    # clear_screen()
    # title()

    options = (1,2,3,4)
    menu = '    1. Start Game \n    2. Exit\n'

    print(menu)
    
    user_input = 0
    while user_input not in options:
        user_input = input('    Enter the number of the option: ')
        try:
            user_input = int(user_input)
            break
        except TypeError:
            print('Sorry, That is not a valid option!')
            continue

    if user_input == 1:
        deck = Deck()
        dealer = Dealer('Dealer')
        player = Player('Player')

    elif user_input == 2:
        del (player, dealer, deck)
        exit()


def game_play_menu(dealer_cards, dealer_card_value):
    # clear_screen()
    # title()
    print(f'''

     Deal #{match}
     ********************

     {player.name}
     Balance: {player.chips}
     Current Bet: {player.bet_chips}
     
     ********************

     DEALER HAND [{dealer_card_value}]
     --------------------------------
     Cards = [{dealer_cards}]

     PLAYER HAND [{player.sum_cards()}]
     --------------------------------
     Cards = [{player.show_cards_all()}]

     Deck_count = {len(dealer.card_deck)}
    
    ''')

                    

def goodbye():
    print('    Thank you for playing!!!!!!')
    time.sleep(3)
    exit()

if __name__ == '__main__': 
    
    game_on = True
    while game_on:
        dealer = Dealer()
        player = Player()
        match = 0
        
        clear_screen()
        title()
        main_menu()

        clear_screen()
        title()
        player.new_name()

        clear_screen()
        title()
        

        user_input = ''
        while user_input != 'd' and user_input != 'q':

            print(' '*14 + f'Hello {player.name} are you ready to play?\n')
            user_input = input(' '*4 + f'(D) Deal or (Q) Quit : ').lower()

        if user_input == 'q':
            clear_screen()
            title()
            goodbye()

        else:
            pass
        

        match_on = True
        while match_on:

            for _ in range(2):
                player.cards.append(dealer.card_deck.deal())
                dealer.cards.append(dealer.card_deck.deal())

            match += 1

            clear_screen()
            title()
            game_play_menu(dealer.show_cards_one(), dealer.sum_card_one())
            

            while True:
                player.bet_chips = input(' '*4 + 'Enter Bet Amount: ') #need int

                try:
                    player.bet_chips = int(player.bet_chips)
                    pass
                except:
                    clear_screen()
                    title()
                    game_play_menu(dealer.show_cards_one(),dealer.sum_cards())

                    print('Error! Please enter a number.')
                    continue    

                if player.chips >= player.bet_chips:
                    player.chips -= player.bet_chips
                    break
                else:    
                    print('you dont\'t have enough chips! Try a lower amount.')
                    continue


            #Hit or Stand Options
            while True:
                clear_screen()
                title()
                game_play_menu(dealer.show_cards_all(), dealer.sum_cards())

                while True:
                    for card in player.cards:
                        if card.value ==0:
                            while user_input != 'a' and user_input != 'b':
                                user_input = input('For Ace, Value (A) [1] or (B) [11]').lower()

                            if user_input == 'a':
                                card.value = 1
                            else:
                                card.value = 11 

                    clear_screen()
                    title()
                    game_play_menu(dealer.show_cards_all(), dealer.sum_cards())            
                    break          

                if player.sum_cards() > 21:
                    player.bet_chips = 0
                    clear_screen()
                    title()
                    print('''
               ______   _   _   _____   _____   _ 
               | ___ \\ | | | | /  ___| |_   _| | |
               | |_/ / | | | | \\ `--.    | |   | |
               | ___ \\ | | | |  `--. \\   | |   | |
               | |_/ / | |_| | /\\__/ /   | |   |_|
               \\____/   \\___/  \\____/    \\_/   (_)\n
                     Press Enter to Continue!
                    ''')
                    input()
                    break

                user_input = ''
                while user_input != 'h' and user_input != 's' and user_input != 'q':
                    user_input = input('     (H) Hit  (S) Stand        (Q) Quit ').lower()

                if user_input == 'h':
                    player.cards.append(dealer.card_deck.deal())
                    continue
                elif user_input == 'q':
                    match_on = False
                    break
                elif user_input == 's':
                    break    

                
                #dealer finishes turn if player stands
                

            while dealer.sum_cards() < 17:
                for card in dealer.cards:
                    if card.value == 0:
                        if (dealer.sum_cards() + 11) < 21:
                            card.value = 11
                        else:
                            card.value = 1

                dealer.cards.append(dealer.card_deck.deal())

            
            if dealer.sum_cards() > 21 and player.sum_cards() <= 21 or player.sum_cards() > dealer.sum_cards() \
                and player.sum_cards() <=21:
                
                player.chips += player.bet_chips*2
                player.bet_chips = 0
                
                clear_screen()
                title()
                game_play_menu(dealer.show_cards_all(), dealer.sum_cards())

                print('''
     __   __  _____   _   _     _    _   _____   _   _   _   _   _ 
     \\ \\ / / |  _  | | | | |   | |  | | |_   _| | \\ | | | | | | | |
       \\ /   | | | | | | | |   | |/\\| |   | |   | . ` | | | | | | |
       | |   \\ \\_/ / | |_| |   \\  /\\  /  _| |_  | |\\  | |_| |_| |_|
       \\_/    \\___/   \\___/     \\/  \\/   \\___/  \\_| \\_/ (_) (_) (_)\n
                        Press Enter to Continue!
                     ''')
                input()

            elif dealer.sum_cards() <= 21 and player.sum_cards() < 21 and dealer.sum_cards() > player.sum_cards():
                player.bet_chips = 0

                clear_screen()
                title()
                game_play_menu(dealer.show_cards_all(), dealer.sum_cards())

                print('''    
     __   __  _____   _   _     _       _____   _____   _____   _   _   _ 
     \\ \\ / / |  _  | | | | |   | |     |  _  | /  ___| |_   _| | | | | | |
      \\ V /  | | | | | | | |   | |     | | | | \\ `--.    | |   | | | | | |
       \\ /   | | | | | | | |   | |     | | | |  `--. \\   | |   | | | | | |
       | |   \\ \\_/ / | |_| |   | |____ \\ \\_/ / /\\__/ /   | |   |_| |_| |_|
       \\_/    \\___/   \\___/    \\_____/  \\___/  \\____/    \\_/   (_) (_) (_)\n
                      Press Enter to Continue!
  ''')

            if player.chips == 0:
                match_on = False
                clear_screen()
                print('''
      _____   ___  ___  ___ _____   _____  _   _ ___________ 
     |  __ \\ / _ \\ |  \\/  ||  ___| |  _  || | | |  ___| ___ \
     | |  \\// /_\\ \\| .  . || |__   | | | || | | | |__ | |_/ /
     | | __ |  _  || |\\/| ||  __|  | | | || | | |  __||    / 
     | |_\\ \\| | | || |  | || |___  \\ \\_/ /\\ \\_/ / |___| |\\ \\ 
      \\____/\\_| |_/\\_|  |_/\\____/   \\___/  \\___/\\____/\\_| \\_|\n
      YOU ARE OUT OF CHIPS!!!
                    ''')
                break


            #end match
            user_input = ''
            while user_input != 'y' and user_input != 'n':
                user_input = input('    play again? (Y) Yes or (N) No : ').lower()
            
            if user_input == 'y':
                player.cards.clear()
                dealer.cards.clear()

                dealer.card_deck = Deck()
                dealer.card_deck.shuffle()
                continue
            else:
                match_on = False
                break

    input()

                




