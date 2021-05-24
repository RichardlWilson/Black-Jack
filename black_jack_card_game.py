#Black Jack Card Game

#Create:
#Cards
  #Value
  #Suit
  #Name
suits = ('hearts', 'spades', 'diamonds', 'clubs')
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

class Cards:
    def __init__(self, name, value, suit):
        self.name =  
        self.value = 
        self.suit = 

    def __str__(self):
        return self.name + ' of ' + self.suit     

#Deck

class Deck:
    def __init__(self):
        for x in range(52):
            for suit in suits:
                for card in card_values
  # class to create all the cards
  #script to shuffle cards

#player
  #name
  #player cards
  #chip ammount

#bank
  #Players name
  #chip amount  

#menus
  #title
  #menu options



#game Logic
  #create deck of cards
  #assign player and dealer
  #deal cards
    #menu options (hit, stay)
    #dealer hand
    #compare agains win or bust



