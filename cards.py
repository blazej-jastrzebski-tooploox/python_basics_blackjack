class Card:
    def __init__(self, name, value, color, hidden=False):
        self.name = name
        self.value = value  # can be accessed by card.value
        self.color = color
        self.hidden = hidden

    def __str__(self):
        if self.hidden:
            return 'An unknown card'
        return '{} of {}'.format(self.name, self.color)
        #f'{self.name} of {self.color}'

    def __repr__(self):
         return self.__str__()

# Values for all cards
colors = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
values_names = [(2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (10, 'Jack'), (10, 'Queen'), (10 , 'King') , (11, 'Ace')]  # Add rest

# Generate cards
deck = []
for color in colors:
    for value, name in values_names:
        deck.append(Card(name, value, color))  # card gets created here
# random shuffle?
import random
random.shuffle(deck)
