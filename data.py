
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
        "value": .15
    },

    "harden": {
        "effect": "harden",
        "value": .50
    },

    "regen": {
        "effect": "regen",
        "value": .05
    },

    "aim": {
        "effect": "aim",
        "value": 100
    }

}

################ HEROS #####################
heroes = [
    {
        "name": "Lionheart",
        "role": "Tank",
        "type": "human",
        "max_health": 280,
        "health": 280,
        "attack": 60,
        "heals": 3,
        "aim": 75,
        "armor": .22,

        "special": {
            "name": "Boulder Toss",
            "type": "rock",
            "uses": 3,
            "damage": 65
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
        "type": "human",
        "max_health": 230,
        "health": 230,
        "attack": 70,
        "heals": 2,
        "aim": 85,
        "armor": .05,

        "special": {
            "name": "Shadow Lance",
            "type": "dark",
            "uses": 2,
            "damage": 90
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
        "type": "human",
        "max_health": 300,
        "health": 300,
        "attack": 35,
        "heals": 4,
        "aim": 80,
        "armor": .12,

        "special": {
            "name": "Cleanse",
            "type": "holy",
            "uses": 2,
            "damage": 75
        },
        "status": {
            "name": "Blessing of Sol",
            "effect": "regen",
            "target": "self",
            "uses": 3,
            "turns": 5,
        }
    },

    {
        "name": "Savos",
        "role": "Mage",
        "type": "human",
        "max_health": 200,
        "health": 200,
        "attack": 80,
        "heals": 2,
        "aim": 65,
        "armor": .08,

        "special": {
            "name": "Frost Nova",
            "type": "ice",
            "uses": 1,
            "damage": 100
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
        "max_health": 300,
        "health": 300,
        "attack": 55,
        "aim": 75,
        "armor": .10

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    },

    {
        "name": "Frostmaw",
        "note": "The Hollow Glacier",
        "type": "ice",
        "max_health": 340,
        "health": 340,
        "attack": 42,
        "aim": 65,
        "armor": .18

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    },

    {
        "name": "Gravemantle",
        "note": "The Stone Eater",
        "type": "rock",
        "max_health": 520,
        "health": 520,
        "attack": 35,
        "aim": 70,
        "armor": .28

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    },

    {
        "name": "Veyra",
        "note": "Choir of Blinding Light",
        "type": "holy",
        "max_health": 230,
        "health": 230,
        "attack": 70,
        "aim": 85,
        "armor": .06

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    },

    {
        "name": "Umbros",
        "note": "The Hollow Watcher",
        "type": "dark",
        "max_health": 250,
        "health": 250,
        "attack": 80,
        "aim": 45,
        "armor": .04

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    },

    {
        "name": "Magis",
        "note": "The Broken Archmage",
        "type": "magic",
        "max_health": 285,
        "health": 285,
        "attack": 60,
        "aim": 80,
        "armor": .12

######### PHASE 2 ATTACK #############

        # "special": {
        #     "name": "Frost Nova",
        #     "type": "ice",
        #     "uses": 3,
        #     "damage": 55
        # }
    }
]