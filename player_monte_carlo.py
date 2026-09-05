from poke_env import Player
from calculations import damage
from table_defense_chart import DEFENSE_MATCHUP
from table_species_info import POKEDEX
import calculations
from pokemon import BattleMon


class monte_carlo_bot(Player):

    def setup(self, battle):

            self.my_sets = {}
            self.opp_sets = {}

            for identifier, mon in battle.team.items(): # identifier = "p1: Great Tusk", mon = Pokemon object with information on it

                if len(POKEDEX[mon.species][1]) == 1:
                    weakness =  dict(DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]])

                else:
                    type_1 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]]
                    type_2 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[1]]
                    weakness = {type: type_1[type] * type_2[type] for type in type_1}

                self.my_sets[mon.species] = BattleMon(mon.species, calculations.stats_calc(mon.species, mon.level), weakness, mon.level, mon.moves, hp = 1.0, boosts = None, status = None)

            for identifier, mon in battle.opponent_team.items():

                if len(POKEDEX[mon.species][1]) == 1:
                    weakness =  dict(DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]])

                else:
                    type_1 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[0]]
                    type_2 = DEFENSE_MATCHUP[POKEDEX[mon.species].types[1]]
                    weakness = {type: type_1[type] * type_2[type] for type in type_1}

                self.opp_sets[mon.species] = BattleMon(mon.species, calculations.stats_calc(mon.species, mon.level), weakness, mon.level, mon.moves, hp = 1.0, boosts = None, status = None)

            return


    def choose_move(self, battle):
        try:

            self.setup(battle)

            my_active = self.my_sets[battle.active_pokemon.species]

            opp_active = self.opp_sets[battle.opponent_active_pokemon.species]

            #move_list = self.get_options(battle)

            move_list = battle.available_moves

            if not battle.available_moves:
                return self.choose_random_move(battle)

            evaluation = {move: self.evaluate(battle, move, my_active, opp_active) 
                        for move in move_list}
            
            best_move = max(evaluation, key=evaluation.get)      

            if not battle.available_moves:
                return self.choose_random_move(battle)

            #best_move = max(battle.available_moves, key=lambda move: move.base_power)
        
        except Exception:
            import traceback
            traceback.print_exc()
            return self.choose_random_move(battle)


        return self.create_order(best_move)



    
        #options = self.get_options()

        #my_mon = battle.active_pokemon.species 
        #opp_mon = battle.opponent_active_pokemon.species
        
        return #self.create_order(best_move)

    def next_turn(self, battle):
        


        

        return

    def evaluate(self, battle, action, my_active, opp_active):

        '''determine who goes first or who is attacker/defender here'''

        attacker = my_active
        defender = opp_active

        damage_dealt = damage(battle, attacker, defender, action)



        #my_hp = battle.active_pokemon.current_hp_fraction
        opp_hp = battle.opponent_active_pokemon.current_hp_fraction

        #if opp_hp > 0:                  # + if speed is higher or - for lower
            #score = my_hp/opp_hp        # + dead pokemon

        #else:
            #score = 200                 # + dead pokemon

        return damage_dealt


    def get_options(self, battle):

        options = battle.available_moves
        options.append = battle.available_switches
        # also self.available_switches      
 
        return options


