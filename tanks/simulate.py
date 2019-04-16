
from .models import Tank
from .views import tank_1, tank_2, tank_3, tank_4

# These are the functions used for the simulation of the battle
# Each function compares the rows of the two set tables and and adds
# 1 to a variable for the frist tank for each true statement
# and 1 to a varibale for the second tank for each false statements
# After that, the values of the two variables are compared,
# giving the winner

tank1 = 0
tank2 = 0


def compare_tanks1(tank_1, tank_2):
    if Tank.barrel_caliber(pk=1) > Tank.barrel_caliber(pk=2):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.barrel_rate_of_fire(pk=1) > Tank.barrel_rate_of_fire(pk=2):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.turret(pk=1) is True:
        tank1 + 1

    if Tank.turret(pk=2) is True:
        tank2 + 1

    if Tank.turret_caliber(pk=1) > Tank.turret_caliber(pk=2):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.front_armor(pk=1) is True:
        tank1 + 1

    if Tank.front_armor(pk=2) is True:
        tank2 + 1

    if Tank.side_armor(pk=1) is True:
        tank1 + 1

    if Tank.side_armor(pk=2) is True:
        tank2 + 1

    if tank1 > tank2:
        print("Tank 1 wins")
    else:
        print("Tank 2 wins")

        pass


tank3 = 0
tank4 = 0


def compare_tanks2(tank_3, tank_4):
    if Tank.barrel_caliber(pk=3) > Tank.barrel_caliber(pk=4):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.barrel_rate_of_fire(pk=3) > Tank.barrel_rate_of_fire(pk=4):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.turret(pk=3) is True:
        tank1 + 1

    if Tank.turret(pk=4) is True:
        tank2 + 1

    if Tank.turret_caliber(pk=3) > Tank.turret_caliber(pk=4):
        tank1 + 1
    else:
        tank2 + 1

    if Tank.front_armor(pk=3) is True:
        tank1 + 1

    if Tank.front_armor(pk=4) is True:
        tank2 + 1

    if Tank.side_armor(pk=3) is True:
        tank1 + 1

    if Tank.side_armor(pk=4) is True:
        tank2 + 1

    if tank1 > tank2:
        print("Tank 3 wins")
    else:
        print("Tank 4 wins")

        pass
