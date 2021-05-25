#Black Jack Card Game

from random import shuffle
from os import name, system

suits = ('hearts', 'spades', 'diamonds', 'clubs')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'jack', 'queen', 'king', 'ace')

card_values = {
    'two': 2 , 
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    'ten' : 10,
    'jack' : 10,
    'queen' : 10,
    'king' : 10,
    'ace' : 11
}

class Card:
    '''
    Class for creating each card.
    '''

    def __init__(self, rank, suit):
        self.rank =  rank
        self.value = card_values[rank]
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit     

#Deck

class Deck:
    '''
    Creates a card deck of 52 cards
    '''

    # init method to create all the cards
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)
                self.cards.append(created_card)

    # len method for calling the length of the deck
    def __len__(self):
        return len(self.cards)
    

    def shuffle(self):
        '''
        Method for shuffling the deck of cards.
        '''

        shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)




class Player:
    def __init__(self,name = 'player', chips = 50):
        self.chips = chips
        self.name = name
        self.bet_chips = 0
        self.cards = []


    def bet(self, chips):
        self.chips -= chips
        self.bet_chips = chips
        

    def info(self):
        print(f'\n{self.name}')
        print('--------------')
        print(f'Chips: {self.chips}')
        print('Cards: ')
        for card in self.cards:
            print(card)


    def game_play(self):
        '''
        Function to call the player options.
        '''

        clear_screen()

        #options
        options = (1,2,3,4)
        menu = '1. Stand \n2. Hit'

        #print(f'\n---BlackJack---\n\n{menu}')
        
        user_input = 0
        while user_input not in options:
            user_input = input('Enter the number of the option: ')
            try:
                user_input = int(user_input)
                break
            except TypeError:
                print('Sorry, That is not a valid option!')
                continue

        if user_input == 1:
            game_play()

        elif user_input == 2:
            exit()

 

class Dealer:
    def __init__(self, name = 'Dealer'):
        self.pot = 0
        self.name = name
        self.cards = []

    def hit(self):
        pass
    
    def stand(self):
        pass  



def clear_screen():
    '''
    Function to clear the screen.
    '''

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def title_screen():
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
\\____/ |_| \\__,_| \\___||_|\\_\\____/  \\__,_| \\___||_|\\_\\(_)\n
            ..........Press Enter........
''')
    input()   


def main_menu():
    '''
    Function to call the main menu options.
    '''

    clear_screen()

    #options
    options = (1,2,3,4)
    menu = '1. Start Game \n2. Exit'

    print(f'\n---BlackJack---\n\n{menu}')
    
    user_input = 0
    while user_input not in options:
        user_input = input('Enter the number of the option: ')
        try:
            user_input = int(user_input)
            break
        except TypeError:
            print('Sorry, That is not a valid option!')
            continue

    if user_input == 1:
        pass

    elif user_input == 2:
        exit()

#game Logic

  #deal cards
    #menu options (hit, stay)
    #dealer hand
    #compare agains win or bust
if __name__ == '__main__': 
    title_screen()
    deck = Deck()
    dealer = Dealer('Dealer')
    player = Player('Player')
    main_menu()
    
    game_on = True
    while game_on:
        deck.shuffle()
        player.cards.append(deck.deal())
        dealer.cards.append(deck.deal())
        player.cards.append(deck.deal())
        dealer.cards.append(deck.deal())
        
        clear_screen()
        player.info()
        break


        #bet
        #stand or hit
            #if hit, check for bust
        #dealer finishes 
        # check for win or loss









