def attack(Z_health, Z_sword, player_Sword, player_health):

    while Z_health > 0 and player_health > 0:
        Z_health = Z_health-player_Sword
        if Z_health < 1:
            print("You hit it for:",player_Sword,"HP \nYou have vanquished the zombie!")
            input("press enter if u wish to carry on")
            break
        # ensures player always hits first
        elif Z_health > 0:
            print("you hit the zombie for", player_Sword, "HP it is now on:", Z_health, "HP")

            # player hits zombie and zombie hits player then health for both is altered

            player_health = player_health - Z_sword

            if player_health < 1:
                print("oh no you died the zombie was on:", Z_health, "HP")
                input("press enter if u wish to carry on")
                break
            elif player_health > 0:
                print("the zombie hit you for", Z_sword, "HP you are now on", player_health, "HP")
                # player hits zombie and zombie hits player then health for both is altered

    return player_health