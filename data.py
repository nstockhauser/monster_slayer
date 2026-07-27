
################ TYPES #####################
type_chart = {
    "fire": {
        "ice": 1.25,
        "rock": 0.75
    },

    "ice": {
        "rock": 1.25,
        "fire": 0.75
    },

    "rock": {
        "fire": 1.25,
        "ice": 0.75
    },

    "magic": {
        "holy": 1.25,
        "dark": 0.75
    },

    "dark": {
        "magic": 1.25,
        "holy": 0.75
    },

    "holy": {
        "dark": 1.25,
        "magic": 0.75
    },

    "human": {
        "none": 1
    }
}


status_chart = {
    "poison": {
        "effect": "poison",
        "value": .08
    },

    "harden": {
        "effect": "harden",
        "value": .30
    },

    "regen": {
        "effect": "regen",
        "value": .04
    },

    "aim": {
        "effect": "aim",
        "value": 92
    },

    "burn": {
        "effect": "burn",
        "value": .35
    },

    "recover": {
        "effect": "recover",
        "value": 110
    },
}

################ HEROS #####################

heroes = [
    {
        "name": "Lionheart",
        "role": "Tank",
        "type": "rock",
        "max_health": 320,
        "health": 320,
        "attack": 48,
        "speed": 80,
        "heals": 2,
        "aim": 92,
        "armor": .24,

        "special": {
            "name": "Boulder Toss",
            "type": "rock",
            "uses": 2,
            "damage": 75
        },
        "status": {
            "name": "Harden",
            "effect": "armor",
            "target": "self",
            "uses": 1,
            "turns": 3,
        }
    },

    {
        "name": "Vex",
        "role": "Rogue",
        "type": "dark",
        "max_health": 235,
        "health": 235,
        "attack": 68,
        "speed": 80,
        "heals": 2,
        "aim": 84,
        "armor": .06,

        "special": {
            "name": "Shadow Lance",
            "type": "dark",
            "uses": 2,
            "damage": 85
        },
        "status": {
            "name": "Poison Dart",
            "effect": "poison",
            "target": "enemy",
            "uses": 1,
            "turns": 4,
        }
    },

    {
        "name": "Solara",
        "role": "Healer",
        "type": "holy",
        "max_health": 300,
        "health": 300,
        "attack": 42,
        "speed": 80,
        "heals": 3,
        "aim": 82,
        "armor": .12,

        "special": {
            "name": "Cleanse",
            "type": "holy",
            "uses": 2,
            "damage": 80
        },
        "status": {
            "name": "Blessing of Sol",
            "effect": "regen",
            "target": "self",
            "uses": 2,
            "turns": 5,
        }
    },

    {
        "name": "Savos",
        "role": "Mage",
        "type": "magic",
        "max_health": 215,
        "health": 215,
        "attack": 82,
        "speed": 80,
        "heals": 2,
        "aim": 70,
        "armor": .08,

        "special": {
            "name": "Frost Nova",
            "type": "ice",
            "uses": 1,
            "damage": 115
        },
        "status": {
            "name": "Eye of Magis",
            "effect": "aim",
            "target": "self",
            "uses": 1,
            "turns": 4,
        }
    }
]



################ MONSTERS #####################
monsters = [
    {
        "name": "Ignivar",
        "note": "The Cinder King",
        "type": "fire",
        "max_health": 470,
        "health": 470,
        "attack": 58,
        "aim": 78,
        "armor": .12,

        "status": {
            "name": "Burned",
            "effect": "burn",
            "target": "enemy",
            "uses": 1,
            "turns": 4
        }
    },

    {
        "name": "Frostmaw",
        "note": "The Hollow Glacier",
        "type": "ice",
        "max_health": 520,
        "health": 520,
        "attack": 50,
        "aim": 76,
        "armor": .20,

        "special": {
            "name": "Winterbane",
            "type": "magic",
            "uses": 1,
            "damage": 145
        }
    },

    {
        "name": "Gravemantle",
        "note": "The Stone Eater",
        "type": "rock",
        "max_health": 620,
        "health": 620,
        "attack": 62,
        "aim": 62,
        "armor": .26,

        "special": {
            "name": "Avalanche",
            "type": "rock",
            "uses": 1,
            "damage": 100
        }
    },

    {
        "name": "Veyra",
        "note": "Bringer of Light",
        "type": "holy",
        "max_health": 460,
        "health": 460,
        "attack": 58,
        "aim": 88,
        "armor": .10,

        "special": {
            "name": "Divine Blessing",
            "type": "holy",
            "uses": 1,
            "turns": 1
        }
    },

    {
        "name": "Umbros",
        "note": "The Hollow Watcher",
        "type": "dark",
        "max_health": 400,
        "health": 400,
        "attack": 78,
        "aim": 58,
        "armor": .06,

        "special": {
            "name": "Slaughter",
            "type": "dark",
            "uses": 1,
            "damage": 28
        }
    },

    {
        "name": "Vorath",
        "note": "The Broken Archmage",
        "type": "magic",
        "max_health": 440,
        "health": 440,
        "attack": 60,
        "aim": 82,
        "armor": .12,

        "special": {
            "name": "Elemental Storm",
            "type": "variety",
            "uses": 1,
            "damage": 32
        }
    }
]