def who_wins(player, dealer, apuesta, ronda):

    #La casa gana, el player fue bust
    if player.points > 21 and ronda != 0: 
        player.amount -= apuesta
        dealer.amount += apuesta
        return True, print('La casa gana, el jugador se fue BUST!!!')
    
    #El jugador gana, la casa se fue bust
    elif dealer.points > 21  and ronda != 0 : 
        player.amount += apuesta
        dealer.amount -= apuesta
        return True, print(f'El jugador {player.name} gana, la casa se fue BUST!!!')

    # El jugador gana, mayor puntos y menos de 21
    elif player.points > dealer.points  and ronda != 0:
        player.amount += apuesta
        dealer.amount -= apuesta
        return True, print(f'El jugador {player} gana!!!')

    
    # El dealer gana, mayor puntos y menos de 21
    elif player.points < dealer.points  and ronda != 0:
        player.amount -= apuesta
        dealer.amount += apuesta

        return True, print('La casa gana!!!')
    
    
    else: 
        return False, ''

        
