class Dealer():

    def __init__(self):
        self.hidden = []
        self.show = []
        self.amount = 1000
        self.bet = 0
        self.points = 0
    
    def empty_show(self):
        self.show = []

    def empty_hidden(self):
        self.hidden = []

    def empty_points(self):
        self.points = 0
    
    def add_show(self, card):
        self.show.append(card)
    
    def add_hidden(self, card):
        self.hidden.append(card)
    
    def add_points(self, puntos):
        self.points += puntos
    
    def __str__(self):
        return f'El dealer tiene {self.amount}'