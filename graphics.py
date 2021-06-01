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

deck = Deck()

def hand(cards):

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
        print(f'''
     _____________________
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
        print(f'''
     __________________________
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
        print(f'''
     ________________________________
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
        print(f'''
     ______________________________________
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
import random
random.shuffle(deck.cards)
hand(deck.cards[0:2])
hand(deck.cards[0:3])
hand(deck.cards[0:4])
hand(deck.cards[0:5])