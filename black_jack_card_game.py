#Black Jack Card Game
'''
Main file for Blackjack Game.
'''

from random import shuffle
from os import system
import sys
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
        '''
        Shuffles the deck of cards.
        '''
        shuffle(self.cards)


    def deal(self):
        '''
        Deals one card
        '''
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
        self.card_flip = False
        self.is_dealer = True


    def sum_cards(self):
        '''
        Returns the sum of all cards in dealer's hand
        '''
        total = 0
        for card in self.cards:
            total += card.value

        return total


    def sum_card_one(self):
        '''
        Returns the first card's value in the dealers hand.
        '''
        return self.cards[0].value


    def show_cards_one(self):
        '''
        Returns the suit and rank of the first card in the dealer's hand
        '''
        return str(self.cards[0])

    def ace_value(self):
        '''
        Checks value of ace.
        '''
        for card in self.cards:
            total = self.sum_cards()
            if card.value == 0:
                if (total + 11) <= 21:
                    card.value = 11
                else:
                    card.value = 1



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
        '''
        Returns the sum of all the cards in the player's hand.
        '''
        total = 0
        for card in self.cards:
            total += card.value

        return total

    def ace_value(self):
        '''
        Check value of Ace.
        '''
        for card in self.cards:
            for _ in range(2):
                total = self.sum_cards()
                if card.value == 0:
                    if (total + 11) <= 21:
                        card.value = 11
                    else:
                        card.value = 1
                elif card.value == 11:
                    if total > 21:
                        card.value = 1
                elif card.value == 1:
                    if (total + 10) <= 21:
                        card.value = 11                    



def main_menu():
    '''
    Function to call the main menu options.
    '''
    user_input = ''
    while user_input not in ('s', 'q'):
        user_input = input(' '*35 + '(S) Start Game   (Q) Quit\n').lower()

    if user_input == 's':
        pass
    elif user_input == 'q':
        #clear_screen()
        graphics.title()
        goodbye()


def goodbye():
    '''
    Game exit code.
    '''
    print(' '*34 + 'Thank you for playing!!!!!!')
    time.sleep(2)
    sys.exit()
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
        graphics.rules()
        main_menu()

        #NAMING THE PLAYER
        graphics.title()
        player.new_name()

        #STARTING THE MATCH
        graphics.title()


        user_input = ''
        while user_input not in ('d', 'q'):
            name_len = len(player.name)//2
            print(' '*(32-name_len) + f'Hello {player.name} are you ready to play?\n')
            user_input = input(' '*37 + '(D) Deal or (Q) Quit\n').lower()


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
            dealer.ace_value()

            graphics.title()
            graphics.game_info_bar(player.name, player.chips, match)
            graphics.show_hands(dealer.cards,dealer.sum_card_one(), player.cards,
                                player.sum_cards(), player.name, dealer.is_dealer,
                                dealer.card_flip)


            #ENTERING BET
            while True:
                player.bet_chips = input(' '*39 + 'Enter Bet Amount:\n') #need int

                try:
                    player.bet_chips = int(player.bet_chips)

                    if player.chips >= player.bet_chips:
                        player.chips -= player.bet_chips
                        dealer.card_flip = True
                        break
                    else:
                        print('you dont\'t have enough chips! Try a lower amount.')

                except:
                    graphics.title()
                    graphics.game_info_bar(player.name, player.chips, match)
                    graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                        player.sum_cards(), player.name, dealer.is_dealer,
                                        dealer.card_flip)

                    print('Error! Please enter a number.')


            #HIT OR STAND
            while True:
                player.ace_value()

                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                    player.sum_cards(), player.name, dealer.is_dealer,
                                    dealer.card_flip)

                #CHECK FOR BUST
                if player.sum_cards() > 21:
                    player.bet_chips = 0

                    graphics.title()
                    graphics.game_info_bar(player.name, player.chips, match)
                    graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                    player.sum_cards(), player.name, dealer.is_dealer,
                                    dealer.card_flip)

                    graphics.bust()
                    input()
                    break

                user_input = ''
                while user_input not in ('h', 's', 'q'):
                    user_input = input(' '*30 + '(H) Hit  (S) Stand        (Q) Quit\n').lower()

                if user_input == 'h':
                    player.cards.append(dealer.card_deck.deal())
                elif user_input == 'q':
                    match_on = False
                    break
                elif user_input == 's':
                    break


            #DEALER FINISHES LAYING DOWN CARDS
            while dealer.sum_cards() < 17:
                dealer.cards.append(dealer.card_deck.deal())
                dealer.ace_value()


            #CHECK FOR WIN OR LOSE
            d_sum = dealer.sum_cards()
            p_sum = player.sum_cards()

            if d_sum > 21 and p_sum <= 21 or p_sum > d_sum \
               and p_sum <=21 or p_sum ==21:

                player.chips += player.bet_chips*2
                player.bet_chips = 0

                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                    player.sum_cards(), player.name, dealer.is_dealer,
                                    dealer.card_flip)

                graphics.win()
                input()

            elif d_sum <= 21 and p_sum < 21 and d_sum > p_sum:

                player.bet_chips = 0

                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                    player.sum_cards(), player.name, dealer.is_dealer,
                                    dealer.card_flip)

                graphics.lose()
                input()


            #CHECK IF OUT OF CHIPS
            if player.chips == 0:
                match_on = False

                graphics.title()
                graphics.game_info_bar(player.name, player.chips, match)
                graphics.show_hands(dealer.cards,dealer.sum_cards(), player.cards,
                                    player.sum_cards(), player.name, dealer.is_dealer,
                                    dealer.card_flip)

                graphics.game_over()
                input()
                break


            # END MATCH CHECKPOINT
            user_input = ''
            while user_input != 'y' and user_input != 'n':
                user_input = input(' '*32 + 'play again? (Y) Yes or (N) No\n').lower()

            if user_input == 'y':
                player.cards.clear()
                dealer.cards.clear()
                dealer.card_flip = False

                dealer.card_deck = Deck()
                dealer.card_deck.shuffle()
            else:
                match_on = False
                break
