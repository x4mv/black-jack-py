class Player():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.cards_in_deck = []
        self.points = 0
    

    def add_amount(self, win):

        self.amount += win
    
    def sub_amount(self, loss):
        self.amount -= loss

    def __str__(self) -> str:
        return f'El jugador {self.name} dispone de {self.amount} de saldo'    