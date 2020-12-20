from RPG_attack import attack
import random
def parry(Z_health, Z_sword, player_Sword, player_health):

    #parry sucess chance=0.65
    for i in range(100):
        if random.random() <= 0.65:
            print("parry successful get a free hit in!")
            Z_health = Z_health-player_Sword
            # ensures player always hits first
            if Z_health < 1:
                print("You hit it for:",player_Sword,"HP \nYou have vanquished the zombie!")
                input("press enter if u wish to carry on")
                exit()
            elif Z_health > 0:
                print("you hit the zombie for", player_Sword, "HP it is now on:", Z_health, "HP")
                TempZhp=Z_health
                #temporarily sets zombie hp to local var

        else:
            print("parry unsuccessful")
            player_health = player_health - Z_sword

            if player_health < 1:
                print("oh no you died the zombie was on:", Z_health, "HP")
                input("press enter if u wish to carry on")
                return player_health
            elif player_health > 0:
                print("the zombie hit you for", Z_sword, "HP you are now on", player_health, "HP")
                # player hits zombie and zombie hits player then health for both is altered

    if TempZhp >0:
        choice = input("do you want to attack or attempt parry? enter a or p").lower
        if choice == "a":
            if player_health > 0:
                player_health = attack(TempZhp, 9, player_Sword, player_health)
            else:
                print("you dead")
        elif choice == "p":
            if player_health > 0:
                player_health = parry(TempZhp, 9, player_Sword, player_health)
            else:
                print("you dead")









    #make it so for any posibility of what happens there is an output and it links to the main flow of things
    #so if the player successfully parrys but doesnt kill then it will go back to main menu with health of zombie returned and the give option to attack or parry again
