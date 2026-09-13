import random
from table_species_info import POKEDEX
from math import floor
from table_random_sets import RANDOM_SETS
from poke_env.battle import Status
from poke_env.battle import Weather
from table_attack_chart import ATTACK_MATCHUP

STAGE_MULT = {-6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -1: 2/3,
               0: 1.0, 1: 3/2, 2: 2.0, 3: 5/2, 4: 3.0, 5: 7/2, 6: 4.0}  


def stats_calc(mon, level):

        # call strategy.py later

    IV = 31

    EV = 85

    nature = [""] # for later
    nature = 1

    calc = {}

    stat_list = ("hp", "atk", "def", "spa", "spd", "spe")

    # hp stat - shedinja does not exist in gen 9 ou yet

    for stat, base in zip(stat_list, POKEDEX[mon].stats):

        if stat == "hp":

            calc[stat] = floor(((2 * (base)) + IV + (EV//4)) * level/100) + level + 10 # instead have this calc loop then return a whole dict instead of one stat

        # other stats

        else:
            calc[stat] = floor(((((2 * (base)) + IV + (EV//4)) * level/100) + 5) * nature)

    return calc



def boost_stats(mon):

    stat_list = ("hp", "atk", "def", "spa", "spd", "spe")

        # boosted stats here  

    boosted = {}

    for stat in stat_list:
        if stat == "hp":
            boosted[stat] = mon.stats[stat]
        else:
            multiplier = STAGE_MULT[mon.boosts[stat]]
            boosted[stat] = floor(mon.stats[stat] * multiplier)

    return boosted



def damage(battle, attacking_mon, defending_mon, move):

    critical_chance = 1 / 24
    critical_damage = 1.5

    """if move or stats are different:
        checkstatsagain (or have something else change stats elsewhere)"""

    """set up 'other' checker"""

    """set up terrarin checker"""

    """set up immunity checker, somewhere before accuracy check. probable need to reorganize everything."""

    stab = 1.0
    critical = 1.0
    weather = 1.0

    if battle.weather:

        if Weather.SUNNYDAY in battle.weather:
            if move.type.name == "FIRE":
                weather = 1.5
            if move.type.name == "WATER":
                weather = 0.5


        elif Weather.RAINDANCE in battle.weather:
            if move.type.name == "WATER":
                weather = 1.5
            if move.type.name == "FIRE":
                weather = 0.5

    if move.type.name in POKEDEX[attacking_mon.species].types:
        stab = 1.5

    burn = 1.0
    if attacking_mon.status == Status.BRN:
        if move.category.name == "PHYSICAL":
            burn = 0.5

    effectiveness = defending_mon.weakness[move.type.name]

    typing = stab * effectiveness

    level = attacking_mon.level

    if random.random() > move.accuracy:
        '''MISS'''
        return 0 # if statement checking for miss in main bot function
        

    #random_roll = (85 + int(random.random() * 16))/100  # fix: right now max roll is 101 ?
                                                        # Split into killing and non-killing rolls

    random_roll = 1 # random should be done on rollouts

    attacker_boosted_stats = boost_stats(attacking_mon)
    defender_boosted_stats = boost_stats(defending_mon)

    if random.random() < critical_chance:
        critical = critical_damage

        if move.category.name == "PHYSICAL":
            attack = max(attacker_boosted_stats['atk'], attacking_mon.stats['atk'])
            defense = min(defender_boosted_stats['def'], defending_mon.stats['def'])

        elif move.category.name == "SPECIAL":
            attack = max(attacker_boosted_stats['spa'], attacking_mon.stats['spa'])
            defense = min(defender_boosted_stats['spd'], defending_mon.stats['spd'])

        else:
            return 0

    else:
        if move.category.name == "PHYSICAL":
            attack = attacker_boosted_stats['atk']
            defense = defender_boosted_stats['def']

        elif move.category.name == "SPECIAL":
            attack = attacker_boosted_stats['spa']
            defense = defender_boosted_stats['spd']

            '''status/etc.'''
        else: 
            return 0 

    damage_dealt = max(1, floor((floor(floor(floor((2 * level / 5) + 2) * move.base_power * attack / defense) / 50) + 2) * typing * critical * random_roll * burn * weather)) # * other 
                                                                                                    
    return damage_dealt                                                                             
                                                                                                    

def var_check():
    # turn ends
    # look at used table used table of moves or abilities, weather changes, etc.
    # assign stat changes to them after a lookup in another table
    # change any stat modified
    # make sure done for each stat/move/ability
    # then do precalcs
    # then start bot and looping
    # need to save this somehow for future parts of the loop (and other loops as well?)
    # INCLUDE ACCURACY
    return 1