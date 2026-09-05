# This file/class was originally written by Claude. I was still learning classes and got stuck on how to handle data transfer across bot states

class BattleMon:

    def __init__(self, species, stats, weakness, level, moveset, hp=1.0, boosts=None, status=None):

        self.species = species
        self.stats = stats            # {"hp":357, "atk":296, ...}
        self.weakness = weakness      # {"FIRE":2.0, "GRASS":0.25, ...}
        self.level = level
        self.moveset = moveset        # Friendly = 4 moves, enemy = randbat movelist
        self.hp = hp                  # fraction, 1.0 = full
        self.status = status          # None, "brn", "par", ...      

        if boosts:
            self.boosts = boosts
        else:
            self.boosts = {"atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}

    def copy(self):

        return BattleMon(
            self.species,
            self.stats,
            self.weakness,
            self.level,
            self.moveset,
            self.hp,
            dict(self.boosts),
            self.status,
        )

    def is_fainted(self):
        return self.hp <= 0
