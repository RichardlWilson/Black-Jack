#Black Jack Card Game

from random import shuffle
from os import name, system
import time
import graphics

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
    Class that defines a dealer.
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
    Class that defines a player
    '''
    def __init__(self,name = 'player', chips = 50):
        self.chips = chips
        self.name = name
        self.bet_chips = 0
        self.cards = []


    def new_name(self):
        '''
        Function that prompts user for the player name.
        '''
        user_input = ''
        while len(user_input) <1:
            user_input = input(' '*42 + 'Enter Name: ')
            self.name = user_input    
        

    def sum_cards(self):
        total = 0
        for card in self.cards:
            total += card.value

        return total           


    def show_cards_all(self):
        return ', '.join(str(card).title() for card in self.cards)        



def main_menu():
    '''
    Function to call the main menu options.
    '''
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
        pass

    elif user_input == 2:
        #clear_screen()
        graphics.title()
        goodbye()

            
def goodbye():
    '''
    game exit code.
    '''
    print(' '*34 + 'Thank you for playing!!!!!!')
    time.sleep(2)
    exit()
#...............................................................................


if __name__ == '__main__':
    system('mode 94, 45')
    system('color 0A')
    
    game_on = True
    while game_on:
        #BUILDING THE GAME
        dealer = Dealer()
        dealer.card_deck.shuffle()
        player = Player()
        match = 0
        
        #STARTING THE GAME
        graphics.title()
        main_menu()
        
        #NAMING THE PLAYER
        graphics.title()
        player.new_name()

        #STARTING THE MATCH
        graphics.title()
        

        user_input = ''
        while user_input != 'd' and user_input != 'q':
            name_len = len(player.name)//2
            print(' '*(32-name_len) + f'Hello {player.name} are you ready to play?\n')
            user_input = input(' '*37 + f'(D) Deal or (Q) Quit\n').lower()


        if user_input == 'q':
            graphics.title()
            goodbye()
        

        match_on = True
        while match_on:
            
            #DEALING CARDS
            for _ in range(2):
                player.cards.append(dealer.card_deck.deal())
                dealer.cards.append(dealer.card_deck.deal())

            match += 1

            graphics.title()
            graphics.game_info_bar(player.name, player.chips, match)
            graphics.show_hands(dealer.cards, player.cards, player.name)
            

            #ENTERING BET
            while True:
                player.bet_chips = input(' '*39 + 'Enter Bet Amount:\n') #need int

                try:
                    player.bet_chips = int(player.bet_chips)
                    pass
                except:
                    graphics.title()
                    graphics.game_info_bar(player.name, player.chips, match)
                    graphics.show_hands(dealer.cards, player.cards, player.name)

                    print('Error! Please enter a number.')
                    continue    

                if player.chips >= player.bet_chips:
                    player.chips -= player.bet_chips
                    break
                else:    
                    print('you dont\'t have enough chips! Try a lower amount.')
                    continue


            #HIT OR STAND
            while True:
                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards, player.cards, player.name)

                
                #CHOOSE THE ACE VALUE
                while True:
                    for card in player.cards:
                        if card.value ==0:
                            while user_input != 'a' and user_input != 'b':
                                user_input = input('For Ace, Value (A) [1] or (B) [11]').lower()

                            if user_input == 'a':
                                card.value = 1
                            else:
                                card.value = 11 

                    graphics.title()
                    graphics.game_info_bar(player.name, player.chips, match)
                    graphics.show_hands(dealer.cards, player.cards, player.name)            
                    break          
                

                #CHECK FOR BUST
                if player.sum_cards() > 21:
                    player.bet_chips = 0

                    graphics.title()
                    graphics.game_info_bar(player.name, player.chips, match)
                    graphics.show_hands(dealer.cards, player.cards, player.name)

                    graphics.bust()
                    input()
                    break

                user_input = ''
                while user_input != 'h' and user_input != 's' and user_input != 'q':
                    user_input = input(' '*30 + '(H) Hit  (S) Stand        (Q) Quit\n').lower()

                if user_input == 'h':
                    player.cards.append(dealer.card_deck.deal())
                    continue
                elif user_input == 'q':
                    match_on = False
                    break
                elif user_input == 's':
                    break    
                

            #DEALER FINISHES LAYING DOWN CARDS
            while dealer.sum_cards() < 17:
                for card in dealer.cards:
                    if card.value == 0:
                        if (dealer.sum_cards() + 11) < 21:
                            card.value = 11
                        else:
                            card.value = 1

                dealer.cards.append(dealer.card_deck.deal())


            #CHECK FOR WIN OR LOSE
            if dealer.sum_cards() > 21 and player.sum_cards() <= 21 or \
                player.sum_cards() > dealer.sum_cards() and player.sum_cards() <=21:
                
                player.chips += player.bet_chips*2
                player.bet_chips = 0
                
                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards, player.cards, player.name)

                graphics.win()
                input()

            elif dealer.sum_cards() <= 21 and player.sum_cards() < 21 and \
                dealer.sum_cards() > player.sum_cards():

                player.bet_chips = 0

                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards, player.cards, player.name)

                graphics.lose()
                input()
            

            #CHECK IF OUT OF CHIPS
            if player.chips == 0:
                match_on = False
                graphics.game_over()
                break


            # END MATCH CHECKPOINT
            user_input = ''
            while user_input != 'y' and user_input != 'n':
                user_input = input(' '*32 + 'play again? (Y) Yes or (N) No\n').lower()
            
            if user_input == 'y':
                player.cards.clear()
                dealer.cards.clear()

                dealer.card_deck = Deck()
                dealer.card_deck.shuffle()
                continue
            else:
                match_on = False
                break
