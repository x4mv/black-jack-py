import player
import deck
import dealer
import cards

name = input('Ingrese el su nombre: ')
saldo = int(input('Ingrese el saldo a apostar'))

flag_end_game = True
flag_hit = True

player = player.Player(name, saldo)
dealer = dealer.Dealer()

while flag_end_game:

    #validaciones si el jugador no tiene saldo
    if player.amount <= 0 : 
        break
    
    #empezamos el juego creando un nuevo escritorio
    #instanciamos la clase deck
    new_deck = deck.Deck()
    #creamos el escritorio
    new_deck.create_deck()
    #mezclamos las cartas
    new_deck.shuffle()

    #repartimos las cartas al dealer
    dealer.hidden.append(new_deck.deal_one())
    dealer.show.append(new_deck.deal_one())
    dealer.points += dealer.show[0].value

    #repartimos las carta al jugador 
    player.cards_in_deck.append(new_deck.deal_one())
    player.cards_in_deck.append(new_deck.deal_one())
    player.points += player.cards_in_deck[0].values + player.cards_in_deck[1]

    
    #mostrar los valores de las cartas
    print(f'El dealer tiene: {dealer.show[0]} {dealer.points}')

    #mostrar las cartas del jugador
    print(f'el jugador tiene: {player.cards_in_deck[0]} \n'
          f'{player.cards_in_deck[1]}'
          )

    action = int(input('1: HIT, 2:PASS'))

    while flag_hit:

        if action == 2:
            flag_hit = False

            dealer.points += dealer.hidden[0].value

            if dealer > 21 :
                print('El dealer fue bust!!! ')
                





