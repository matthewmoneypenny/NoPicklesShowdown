from poke_env import Player
from calculations import damage, boost_stats
from table_defense_chart import DEFENSE_MATCHUP
from table_species_info import POKEDEX
from table_random_sets import RANDOM_SETS
from table_form_changes import BASE_FORMS
from table_moves import MOVES
import calculations
from pokemon import BattleMon
import traceback
import random

'''to commit:
git add .
git commit -m "description"
git push'''


class monte_carlo_bot(Player):

    def setup(self, battle):

            self.gen_moves = MOVES["gen9"]

            self.my_sets[battle.battle_tag] = {}
            self.opp_sets[battle.battle_tag] = {}

            for mon in battle.team.values():

                if len(POKEDEX[mon.species][1]) == 1:
                    weakness =  dict(DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]])

                else:
                    type_1 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]]
                    type_2 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[1]]
                    weakness = {type: type_1[type] * type_2[type] for type in type_1}

                self.my_sets[battle.battle_tag][BASE_FORMS.get(mon.species, mon.species)] = BattleMon(mon.species, calculations.stats_calc(mon.species, mon.level), weakness, mon.level, mon.moves, base = None, hp = None, boosts = None, status = None, forms = None)

            return


    def choose_move(self, battle): # goes over all choices, rollouts, and averages the scores from evaluate


        if not hasattr(self, "my_sets"):
            self.my_sets = {}
            self.opp_sets = {}

        if battle.battle_tag not in self.my_sets:
            self.setup(battle)

        self.refresh(battle) # resets to data from the game after the turn is over

        try:

            my_active = self.my_sets[battle.battle_tag][self.base_lookup(battle.active_pokemon.species)]

            opp_active = self.opp_sets[battle.battle_tag][self.base_lookup(battle.opponent_active_pokemon.species)]

            #move_list = self.get_options(battle)

            move_list = battle.available_moves

            if not battle.available_moves:
                return self.choose_random_move(battle)
            
            opp_action = self.gen_moves[random.choice(opp_active.moveset)]

            evaluation = {move: self.simulate_move(battle, self.gen_moves[move.id], opp_action, my_active, opp_active) 
                        for move in move_list}
            
            best_move = max(evaluation, key=evaluation.get)      

            if not battle.available_moves:
                return self.choose_random_move(battle)
        
        except Exception:
            traceback.print_exc()
            self.error_count = getattr(self, "error_count", 0) + 1
            return self.choose_random_move(battle)


        return self.create_order(best_move)


        #options = self.get_options()

        #my_mon = battle.active_pokemon.species 
        #opp_mon = battle.opponent_active_pokemon.species
        
        return #self.create_order(best_move)

    def simulate_switch(self, battle, my_action, opp_action, my_active, opp_active):

        return

        if my_active.stats["spe"] > opp_active.stats["spe"]:
            first = my_active
            second = opp_active

        else:
            first = opp_active
            second = my_active

        # Switch logic here
               

        result = self.evaluate(battle)

        return result

    def simulate_move(self, battle, my_action, opp_action, my_active, opp_active):

        future_my_sets = dict()
        future_opp_sets = dict()
        future_sets = (future_my_sets, future_opp_sets)

        for mon in self.my_sets[battle.battle_tag].values():
            future_my_sets[mon.base] = mon.copy()

        for mon in self.opp_sets[battle.battle_tag].values():
            future_opp_sets[mon.base] = mon.copy()

        if my_active.stats["spe"] > opp_active.stats["spe"]:
            attacker = future_my_sets[self.base_lookup(my_active.species)]
            defender = future_opp_sets[self.base_lookup(opp_active.species)]
            action = my_action
            second_action = opp_action

        else:
            attacker = future_opp_sets[self.base_lookup(opp_active.species)]
            defender = future_my_sets[self.base_lookup(my_active.species)]
            action = opp_action
            second_action = my_action

        # Form changes check here? in refresh? including item change checks?

        damage_dealt = damage(battle, attacker, defender, action)

        # add check to see if this damage calc has been done before?

        defender.hp = defender.hp - damage_dealt # this is the mon who just defended's hp

        if defender.is_fainted(): # if next attacker is dead, no need to calc damage again
            return self.evaluate(battle, future_sets)

        # phase two of the turn

        # Need to add recoil checks

        damage_dealt = damage(battle, defender, attacker, second_action)
        attacker.hp = attacker.hp - damage_dealt

        return self.evaluate(battle, future_sets)

    def evaluate(self, battle, future_sets):

        my_active = future_sets[0][self.base_lookup(battle.active_pokemon.species)]
        opp_active = future_sets[1][self.base_lookup(battle.opponent_active_pokemon.species)]

        health = 0
        field_state = 0

        # fainted mon scoring

        for mon in future_sets[0].values():
            if mon.is_fainted():
                health -= 100
            else:    
                health += 100 * (mon.hp / mon.stats["hp"])

        for mon in future_sets[1].values():
            if mon.is_fainted():
                health += 100
            else:
                health -= 100 * (mon.hp / mon.stats["hp"])

        # speed check

        # speed or boosted speed halved when paralyzed?

        if boost_stats(my_active)["spe"] > boost_stats(opp_active)["spe"]:
            field_state += 250
        elif boost_stats(my_active)["spe"] < boost_stats(opp_active)["spe"]:
            field_state -= 250
            
        score = health + field_state

        return score


    def get_options(self, battle):
        options = battle.available_moves + battle.available_switches
        return options

    def refresh(self, battle):

        for identifier, mon in battle.opponent_team.items():
            if BASE_FORMS.get(mon.species, mon.species) not in self.opp_sets[battle.battle_tag]:

                if len(POKEDEX[mon.species][1]) == 1:
                    weakness =  dict(DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]])

                else:
                    type_1 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]]
                    type_2 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[1]]
                    weakness = {type: type_1[type] * type_2[type] for type in type_1}

                
                movelist = set()
                for random_set in RANDOM_SETS[self.base_lookup(mon.species)].sets:
                    movelist.update(random_set.movepool)
                movelist = tuple(movelist)

                self.opp_sets[battle.battle_tag][BASE_FORMS.get(mon.species, mon.species)] = BattleMon(mon.species, calculations.stats_calc(mon.species, mon.level), weakness, mon.level, movelist, base = None, hp = None, boosts = None, status = None, forms=None)                                                 

        for mon in battle.team.values():
            self.my_sets[battle.battle_tag][self.base_lookup(mon.species)].hp = mon.current_hp

        for mon in battle.opponent_team.values():
            self.opp_sets[battle.battle_tag][self.base_lookup(mon.species)].hp = mon.current_hp_fraction * self.opp_sets[battle.battle_tag][self.base_lookup(mon.species)].stats["hp"]

        return


    def base_lookup(self, species):
        return BASE_FORMS.get(species, species)