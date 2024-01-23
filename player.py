class Player():

    def __init__(self, name, bet):
        
        self.name = name
        self.bet = bet
        self.amount = 1000
        self.points = 0
        self.cartas = []
    
    def __str__(self):
        
        return f'El jugador {self.name} dispone de {self.amount}'



    