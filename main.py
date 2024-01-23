from registrarUsuario import registrar_usuario
from player import Player
from casa import Dealer
from deck import Deck
from checkWin import who_wins
from hitPass import hit_pass



# Preguntar el nombre del jugador
nombre, apuesta = registrar_usuario()

#Crear las instancias del dealer y del jugador
player = Player(nombre, apuesta)
dealer = Dealer()

#creando las banderas del juego, y del hit
flag_game_on = True
flag_hit_player_on = True
flag_hit_dealer_on = True
ronda = 0

#empezar el juego
while flag_game_on: 

    #Creamos la mesa 
    new_deck = Deck()
    #Creamos las cartas
    new_deck.create_deck()
    #Mezclamos las cartas
    new_deck.shuffle()

    #Repartimos las 2 cartas al dealer
    #add al hidden
    dealer.add_hidden(new_deck.deal_one())
    #add al show
    dealer.add_show(new_deck.deal_one())
    #sumamos los puntos del dealer hasta ahora
    dealer.points += dealer.show[0].value
    #mostramos los puntos del dealer hasta ahora 
    print(f'Puntos de la casa: {dealer.points}') 

    #Repartimos 2 cartas al jugador
    #add al jugador
    player.cartas.append(new_deck.deal_one())
    #sumamos el valor de la carta a los puntos del jugador 
    player.points += player.cartas[len(player.cartas)-1].value
    #add al show
    player.cartas.append(new_deck.deal_one())
    #sumamos el valor de la carta a los puntos del jugador 
    player.points += player.cartas[len(player.cartas)-1].value
    #mostramos los puntos del jugador hasta ahora 
    print(f'Puntos de {player.name}: {player.points}') 
    estado, msg = who_wins(player, dealer, apuesta, ronda)
    ronda += 1
    if estado:
        flag_game_on = False
        break
    desicion = hit_pass()
    while flag_hit_player_on:
        if desicion == 2:
            flag_hit_player_on = False
            break
        else:
            player.cartas.append(new_deck.deal_one())
            player.points += player.cartas[len(player.cartas)-1].value
            estado, msg = who_wins(player, dealer, apuesta, ronda)
            if estado:
                flag_game_on = False 
                flag_hit_player_on = False
                break 
        print(f'Puntos de la casa: {dealer.points}')
        print(f'Puntos de {player.name}: {player.points}') 
        desicion = hit_pass()
    while flag_hit_dealer_on:
        dealer.points += dealer.hidden[0].value
        while dealer.points < 17: 
            #add al show
            dealer.add_show(new_deck.deal_one())
            #sumamos los puntos del dealer hasta ahora
            dealer.points += dealer.show[len(dealer.show)-1].value
            print(f'Puntos de la casa: {dealer.points}')
        flag_hit_dealer_on = False
        break

    estado, msg = who_wins(player, dealer, apuesta, ronda)
    if estado:
        flag_game_on = False
        break
print(f'Puntos de la casa: {dealer.points}')
print(f'Puntos de {player.name}: {player.points}') 

