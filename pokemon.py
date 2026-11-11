# This file/class was originally written by Claude and further modified by me.

from table_form_changes import FORM_CHANGES, BASE_FORMS

class BattleMon:

    def __init__(self, species, stats, weakness, level, moveset, base = None, hp = None, boosts = None, status = None, forms = None):

        self.species = species
        self.stats = stats            # {"hp":357, "atk":296, ...}
        self.weakness = weakness      # {"FIRE":2.0, "GRASS":0.25, ...}
        self.level = level
        self.moveset = moveset        # Friendly = 4 moves, enemy = randbat movelist

        if hp is None: # Current HP
            self.hp = stats["hp"]
        else:
            self.hp = hp

        self.base = BASE_FORMS.get(species, species)
        self.status = status          # None, "brn", "par", ...      

        if forms is None:
            # Lookup logic here
            self.forms = FORM_CHANGES.get(base, {})
        else:
            self.forms = forms


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
            self.base,
            self.hp,
            dict(self.boosts),
            self.status,
            self.forms,
        )

    def is_fainted(self):
        return self.hp <= 0
