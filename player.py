class Hand():
    def __init__(self):
        self.cards = []

    def hit(self, deck):
        self.cards.append(deck.draw_card())

    def show(self):
        print("Your hand: ")
        for card in self.cards:
            card.show()
        print("Your hand value: {}".format(player.get_value()))

    def get_value(self):
        return sum([card.value for card in self.cards])

class Player(Hand):
    def __init__(self, name, money):
        super().__init__()
        self.name = name
        self.money = money

    def __str__(self):
        return f'{self.name}, {self.money}'

    def bet(self, amount):
        player.money -= amount


class DealerHand(Hand):
    def __init__(self):
        super().__init__()

    def show(self):
        print("Dealer's hand: ")
        for card in self.cards:
            card.show()
        print("Dealer's hand value: {}".format(dealer.get_value()))

    def show_hidden(self):
        print("Dealer's hand: ")
        for card in self.cards[:-1]:
            card.show()
        print(" ___________")
        print("|??         |")
