import random, time
from RPG_attack import attack
from leaderboard import leaderboardAdd
from leaderboard import leaderboardRead
from ascii import asciiIMG
from RPG_parry import parry

asciiIMG()

#THIS BIT IS FOR USERNAME VALIDITY CHECKING
name_validity=False
while name_validity == False:
    name=input("Please enter a name no longer than 7 characters>>>")
    if len(name) > 7:
        print("That name is longer than 7 characters!")
    elif len(name) < 1:
        print("Please enter a name")
    else:
        name_validity=True
        print("Name entered as: "+name)

room=0

if room == 0:
    print("you have entered the first cell and a LVL 1 zombie has appeared!")
    player_Sword = random.randint(5,10)
    # sets sword attack damage to a random integer from 5 to 10 damage
    player_health = 60
    # player starting health mr P suggested 20 but that is much too low i suggest around 50-60
    if player_health > 0:
        player_health = attack(8, 2, player_Sword, player_health)
        # calls function and sets the players health to the returned value in the function in this case player_health
        room += 1
    else:
        print("you dead")

#rinse and repete with comments for subsequent few

if room == 1:

    print("you have entered the second cell and a LVL 2 zombie has appeared!")
    player_Sword = random.randint(5, 10)
    if player_health > 0:
        player_health = attack(11, 2, player_Sword, player_health)
        room += 1
    else:
        print("you dead")
        room = 0


if room == 2:
    print("you have entered the third cell and a LVL 3 zombie has appeared!")
    player_Sword = random.randint(5, 10)
    if player_health > 0:
        player_health = attack(15, 7, player_Sword, player_health)
        #even when setting output of function to variable it will still output the whole function (i know im dumb but just a reminder)
        room += 1
    else:
        print("you dead")
        room=0

#mr P sugessted adding 3 potions one health potion, one death potion and one null potion at this point may do so in future
#If i was to set HP at line 29 to 20HP this system could work

if room == 3:
    print("you have entered the fourth cell and a LVL 4 zombie has appeared!")
    player_Sword = random.randint(5, 10)


    choice=input("do you want to attack or attempt parry? enter a or p").lower
    if choice=="a":
        if player_health > 0:
            player_health = attack(18, 9, player_Sword, player_health)
            room += 1
        else:
            print("you dead")
            room = 0
    elif choice=="p":
        if player_health > 0:
            player_health = parry(18, 9, player_Sword,player_health)
            room += 1
        else:
            print("you dead")
            room = 0



if room == 4:
    print("well done you defeated Zombie Arena")

leaderboardAdd(name, player_health)
leaderboardRead()
time.sleep(5)