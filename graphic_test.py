# #graphic
# print('''
# ---BlackJack---

# *********************

# DEALER     Value: 3     

# *********************
# .------.
# |C --. | Card 1
# | :  : | Three of Diamonds
# | :  : | Value: 3
# | '--'C|
# `------'

# *********************

# PLAYER     $:       

# *********************
# .------.
# |C --. | Card 1
# | :  : | Three of Diamonds
# | :  : | Value: 3
# | '--'C|
# `------'

# .------.
# |C --. | Card 2
# | :  : | Three of Diamonds
# | :  : | Value: 3
# | '--'C|
# `------'

# .------.
# |C --. | Card 1
# | :  : | Three of Diamonds
# | :  : | Value: 3
# | '--'C|
# `------'

# (H) Hit  (S)Stand  (Q) Quit


# ---------------
# | 7           |
# | *           |




# ''')

cards = [2,3]

if len(cards) ==2:
    print(f'''
.---------------------.
| {cards[0]}     | {cards[1]}            |
|       |              |
|       |              |
|       |              |
|       |              |
|       |              |
|       |              |
|       |              |
|       |              |
|       |              |
|       |            {cards[1]} |
._______.______________.
    ''')

'''
♥ = alt + 3
♦ = alt + 4
♠ = alt + 6
♣ = alt + 5
'''