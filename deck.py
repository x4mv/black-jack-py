from random import shuffle
import cards

class Deck():

    def __init__(self):
        self.cards = []

    def create_deck(self):

        for x in cards.suits:
            for i in cards.ranks:
                self.cards.append(cards.Card(x, i))
    
    def shuffle(self):
        return shuffle(self.cards)
        
    def deal_one(self):
        return self.cards.pop(0)
    
    def __str__(self) -> str:
        return f' {self.cards[0]} has a value of {self.cards[0].value}'

    


new_deck = Deck()
new_deck.create_deck()
#new_deck.shuffle()
print(f' {new_deck.cards[0]} value -> {new_deck.cards[0].value}')

