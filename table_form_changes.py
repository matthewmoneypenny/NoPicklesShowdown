# This file was originally written by Claude.

FORM_CHANGES = {
    "cramorant": {
        "cramorant":         {"surf_above_half": "cramorantgulping", "surf_below_half": "cramorantgorging"},
        "cramorantgulping":  {"hit": "cramorant", "switch_out": "cramorant"},
        "cramorantgorging":  {"hit": "cramorant", "switch_out": "cramorant"},
    },
    "eiscue": {
        "eiscue":            {"physical_hit": "eiscuenoice"},
        "eiscuenoice":       {"snow": "eiscue"},
    },
    "meloetta": {
        "meloetta":          {"relicsong": "meloettapirouette"},
        "meloettapirouette": {"relicsong": "meloetta", "switch_out": "meloetta"},
    },
    "mimikyu": {
        "mimikyu":           {"hit": "mimikyubusted"},
    },
    "minior": {
        "minior":            {"above_half": "miniormeteor"},
        "miniormeteor":      {"below_half": "minior"},
    },
    "morpeko": {
        "morpeko":           {"end_of_turn": "morpekohangry"},
        "morpekohangry":     {"end_of_turn": "morpeko", "switch_out": "morpeko"},
    },
    "ogerpon": {
        "ogerpon":           {"tera": "ogerpontealtera"},
    },
    "ogerponcornerstone": {
        "ogerponcornerstone": {"tera": "ogerponcornerstonetera"},
    },
    "ogerponhearthflame": {
        "ogerponhearthflame": {"tera": "ogerponhearthflametera"},
    },
    "ogerponwellspring": {
        "ogerponwellspring": {"tera": "ogerponwellspringtera"},
    },
    "palafin": {
        "palafin":           {"switch_out": "palafinhero"},
    },
    "terapagos": {
        "terapagos":         {"switch_in": "terapagosterastal"},
        "terapagosterastal": {"tera": "terapagosstellar"},
    },
}


# Alternate form -> base form. Base forms are the keys used in FORM_CHANGES and RANDOM_SETS.
# Only alternate forms are listed. Look up with BASE_FORMS.get(species, species) so
# base forms and mons without form changes return their own name.
# Each Ogerpon mask maps to its own mask entry, because RANDOM_SETS lists the masks separately.

BASE_FORMS = {
    "cramorantgulping":        "cramorant",
    "cramorantgorging":        "cramorant",
    "eiscuenoice":             "eiscue",
    "meloettapirouette":       "meloetta",
    "mimikyubusted":           "mimikyu",
    "miniormeteor":            "minior",
    "morpekohangry":           "morpeko",
    "ogerpontealtera":         "ogerpon",
    "ogerponcornerstonetera":  "ogerponcornerstone",
    "ogerponhearthflametera":  "ogerponhearthflame",
    "ogerponwellspringtera":   "ogerponwellspring",
    "palafinhero":             "palafin",
    "terapagosterastal":       "terapagos",
    "terapagosstellar":        "terapagos",

    # Cosmetic and permanent variants. These never change during a battle; they are
    # listed so a variant name still finds its base entry in RANDOM_SETS.
    "alcremiecaramelswirl":    "alcremie",
    "alcremielemoncream":      "alcremie",
    "alcremiematchacream":     "alcremie",
    "alcremiemintcream":       "alcremie",
    "alcremierainbowswirl":    "alcremie",
    "alcremierubycream":       "alcremie",
    "alcremierubyswirl":       "alcremie",
    "alcremiesaltedcream":     "alcremie",
    "basculinbluestriped":     "basculin",
    "basculinwhitestriped":    "basculin",
    "dudunsparcethreesegment": "dudunsparce",
    "florgesblue":             "florges",
    "florgesorange":           "florges",
    "florgeswhite":            "florges",
    "florgesyellow":           "florges",
    "gastrodoneast":           "gastrodon",
    "magearnaoriginal":        "magearna",
    "mausholdfour":            "maushold",
    "miniorblue":              "minior",
    "miniorgreen":             "minior",
    "miniorindigo":            "minior",
    "miniororange":            "minior",
    "miniorviolet":            "minior",
    "minioryellow":            "minior",
    "pikachualola":            "pikachu",
    "pikachubelle":            "pikachu",
    "pikachucosplay":          "pikachu",
    "pikachuhoenn":            "pikachu",
    "pikachukalos":            "pikachu",
    "pikachulibre":            "pikachu",
    "pikachuoriginal":         "pikachu",
    "pikachupartner":          "pikachu",
    "pikachuphd":              "pikachu",
    "pikachupopstar":          "pikachu",
    "pikachurockstar":         "pikachu",
    "pikachusinnoh":           "pikachu",
    "pikachustarter":          "pikachu",
    "pikachuunova":            "pikachu",
    "pikachuworld":            "pikachu",
    "polteageistantique":      "polteageist",
    "sawsbuckautumn":          "sawsbuck",
    "sawsbucksummer":          "sawsbuck",
    "sawsbuckwinter":          "sawsbuck",
    "sinistchamasterpiece":    "sinistcha",
    "tatsugiridroopy":         "tatsugiri",
    "tatsugiristretchy":       "tatsugiri",
    "toxtricitylowkey":        "toxtricity",
    "vivillonarchipelago":     "vivillon",
    "vivilloncontinental":     "vivillon",
    "vivillonelegant":         "vivillon",
    "vivillonfancy":           "vivillon",
    "vivillongarden":          "vivillon",
    "vivillonhighplains":      "vivillon",
    "vivillonicysnow":         "vivillon",
    "vivillonjungle":          "vivillon",
    "vivillonmarine":          "vivillon",
    "vivillonmodern":          "vivillon",
    "vivillonmonsoon":         "vivillon",
    "vivillonocean":           "vivillon",
    "vivillonpokeball":        "vivillon",
    "vivillonpolar":           "vivillon",
    "vivillonriver":           "vivillon",
    "vivillonsandstorm":       "vivillon",
    "vivillonsavanna":         "vivillon",
    "vivillonsun":             "vivillon",
    "vivillontundra":          "vivillon",
    "zarudedada":              "zarude",
}