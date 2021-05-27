#Black Jack Card Game

from random import shuffle
from os import name, system

suits = ('hearts', 'spades', 'diamonds', 'clubs')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'jack', 'queen', 'king', 'ace')

card_values = {'two': 2 , 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7,
    'eight' : 8, 'nine' : 9, 'ten' : 10, 'jack' : 10, 'queen' : 10, 'king' : 10,
    'ace' : 11 }

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


    def play_menu(self, deck):
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

    def show_cards(self):
        return ', '.join(str(card).title() for card in self.cards)        

 

class Dealer:
    '''
    Defines dealer.
    '''
    def __init__(self, name = 'Dealer'):
        self.pot = 0
        self.name = name
        self.cards = []

    def info(self):
        print(f'\n{self.name}')
        print('--------------')
        print('Cards: ')
        for card in self.cards:
            print(card) 

    def sum_cards(self):
        total = 0
        for card in self.cards:
            total += card.value

        return total

    def show_cards(self):
        return ', '.join(str(card).title() for card in self.cards)
        # cards = ''
        # for card in self.cards:
        #     cards += str(card)
        # return cards     
                       




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
    clear_screen()
    title()

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

def game_play_menu(match, player_name, player_chips, dealer_card_value, dealer_hand,
                   player_card_value, player_hand, player_bet = 0):
    clear_screen()
    title()
    print(f'''

     Deal #{match}
     ********************

     {player_name}
     Balance: {player_chips}
     Current Bet: {player_bet}
     
     ********************

     DEALER HAND [{dealer_card_value}]
     --------------------------------
     Cards = [{dealer_hand}]

     PLAYER NAME [{player_card_value}]
     --------------------------------
     Cards = [{player_hand}]

     ..................................................................
       (B) Bet  (H) Hit  (S) Stand     (Quit)
        ''')
    player.play_menu(deck)



def game_check(player_value, dealer_value):
    '''
    check if win, lose, bust
    '''
    if player_value > 21:
        bust = True
    elif player_value == 21:
        if dealer_value == 21:
            draw = True
        else:
            win = True
    elif dealer_value == 21:
        lose = True
    else:
        pass                    


if __name__ == '__main__': 
    
    
    
    game_on = True
    while game_on:
        main_menu()
        deck = Deck()
        deck.shuffle()
        match_count = 0

        dealer = Dealer('Dealer')
        player = Player('Player')
        
        clear_screen()
        title()
        player.new_name()

        
        while True:
            for _ in range(2):
                player.cards.append(deck.deal())
                dealer.cards.append(deck.deal())

            match_count += 1

            clear_screen()
            title()                
            
            while True:
                game_play_menu(match_count, player.name, player.chips, dealer.sum_cards(), dealer.show_cards(),
                               player.sum_cards(), player.show_cards())    

            game_on = False
            break

        options = ('y', 'n')         
        while user_input not in options:
            user_input = input('Do you want to play again?  (Y) or (N) ').lower()

        if user_input == 'y':
            del (player, dealer, deck)
            pass
        else:
            exit()                   
