import unittest
import black_jack_card_game
import graphics

class Test_Blackjack(unittest.TestCase):

    def test_deck(self):
        '''
        Test deck of cards are correct length.
        '''

        deck = black_jack_card_game.Dealer().card_deck
        result = len(deck)

        self.assertEqual(result, 52)


    # def test_dealer_show_hand(self):
    #     '''
    #     testing the show hands graphic.
    #     '''
    #     hand =[]
    #     for card in range(5):
    #         card = black_jack_card_game.Card('two', 'hearts')
    #         hand.append(card)
        
    #     suit = ''
    #     if hand[4].suit =='hearts':
    #         suit = '♥'
    #     elif hand[4].suit =='clubs':
    #         suit = '♣'
    #     elif hand[4].suit == 'diamonds':
    #         suit = '♦'
    #     elif hand[4].suit == 'spades':
    #             suit = '♠'


    #     result = str(graphics.hand(hand))
        
    #     test = (f'''     ______________________________________
    #  |     |     |     |     |             |
    #  | {hand[0].value}  | {hand[1].value}  | {hand[2].value}  | {hand[3].value}  | {hand[4].value}          |
    #  |     |     |     |     |             |
    #  |     |     |     |     |             |
    #  |     |     |     |     |             |
    #  |     |     |     |     |      {suit}      |
    #  |     |     |     |     |             |
    #  |     |     |     |     |             |
    #  |     |     |     |     |             |
    #  |     |     |     |     |           {hand[4].value}|
    #  |_____|_____|_____|_____|_____________|
    #  ''')

    #     # print(test)
    #     # print(len(test), len(str(result)))
    #     # print(result)

    #     self.assertEqual(result, test)

    # def test_test(self):

    #     def test_string():
    #         return 'Test'

    #     result = str(test_string())

    #     self.assertEqual(result, 'Test')

    def test_ace_value(self):
        '''
        Testing Ace card value.
        '''
        hand =[]
        
        hand.append(black_jack_card_game.Card('king', 'hearts'))
        hand.append(black_jack_card_game.Card('ace', 'hearts'))

        player = black_jack_card_game.Player()
        player.cards = hand

        player.ace_value()

        result = player.sum_cards()
        print('Test Ace Value')
        self.assertEqual(result, 21)      
        
              

if __name__ == '__main__':
    unittest.main()        
