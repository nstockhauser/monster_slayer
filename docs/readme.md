# ⚔️ Project: Monster Slayer

Monster Slayer is a turn-based roguelike RPG built in Python.

This README provides an overview of the current version of the game, including gameplay mechanics, combat systems, and the heroes and monsters available in the current build.

---

### 🔄 Core Gameplay Loop

| Step  | Description                 |
| ----- | --------------------------- |
| **1** | Select Hero                 |
| **2** | Fight Random Monster        |
| **3** | Survive as Long as Possible |
| **4** | Die and Try Again           |

---

### ⚔️ Combat System

| System                  | Description                                                                       |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Turn-Based Combat**   | Heroes and monsters alternate actions until one is defeated.                      |
| **Elemental System**    | Damage is modified by elemental strengths and weaknesses.                         |
| **Resource Management** | Healing charges and special move uses are limited, requiring strategic decisions. |

---

### 🌎 Elemental Effectiveness

| Element  | Strong Against | Weak Against |
| -------- | -------------- | ------------ |
| 🔥 Fire  | ❄️ Ice         | 🪨 Rock      |
| ❄️ Ice   | 🪨 Rock        | 🔥 Fire      |
| 🪨 Rock  | 🔥 Fire        | ❄️ Ice       |
| 🔮 Magic | ✨ Holy        | 🌑 Dark      |
| ✨ Holy  | 🌑 Dark        | 🔮 Magic     |
| 🌑 Dark  | 🔮 Magic       | ✨ Holy      |
| ⚔️ Human | None           | None         |

> **Damage Modifier**
>
> - **Strong Against:** ×1.25 Damage
> - **Weak Against:** ×0.75 Damage
> - **Neutral Matchup:** ×1.0 Damage

---

### 🎯 Current Roster

| Type         | Target Count |
| ------------ | ------------ |
| **Heroes**   | 4            |
| **Monsters** | 6            |

---

### 🧙 Hero Design

| Feature           | Description                                            |
| ----------------- | ------------------------------------------------------ |
| **Basic Attack**  | Standard attack available every turn.                  |
| **Status Move**   | Unique tactical ability that applies a special effect. |
| **Special Move**  | Powerful limited-use ability unique to each hero.      |
| **Limited Heals** | Finite healing resource available during a run.        |

---

### 🧙 Current Heroes

| Hero          | Role   | Specialty                                                                                                                |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------ |
| **Lionheart** | Tank   | High armor and durability. Uses **Boulder Toss** and **Harden** to outlast opponents.                                    |
| **Vex**       | Rogue  | High accuracy and burst damage. Uses **Shadow Lance** and **Poison Dart** to eliminate enemies quickly.                  |
| **Solara**    | Healer | Exceptional survivability through healing and regeneration. Uses **Cleanse** and **Blessing of Sol** to sustain herself. |
| **Savos**     | Mage   | Glass cannon with devastating elemental damage. Uses **Frost Nova** and **Eye of Magis** to maximize spell accuracy.     |

---

### 👹 Monster Design

| Feature               | Description                                                                  |
| --------------------- | ---------------------------------------------------------------------------- |
| **Basic Attack**      | Standard monster attack.                                                     |
| **Unique Elements**   | Each monster has its own elemental affinity and stat distribution.           |
| **Phase 2 Abilities** | Each monster activates a unique ability after falling to 33% health or less. |

---

### 👹 Current Monsters

| Monster         | Element | Specialty                                                                                      |
| --------------- | ------- | ---------------------------------------------------------------------------------------------- |
| **Ignivar**     | Fire    | Applies **Burn**, dealing damage based on Ignivar's Attack over multiple turns.                |
| **Frostmaw**    | Ice     | Charges **Winterbane** for one turn before releasing a devastating guaranteed attack.          |
| **Gravemantle** | Rock    | Triggers **Avalanche**, dealing heavy damage and permanently reducing the hero's Armor.        |
| **Veyra**       | Holy    | Uses **Divine Blessing** to restore health and permanently increase her Attack.                |
| **Umbros**      | Dark    | Uses **Slaughter** to land between **2–5 attacks** in a single turn.                           |
| **Vorath**      | Magic   | Creates an **Elemental Storm**, striking three times with randomly selected elemental attacks. |

---

### Known bugs

- Status Overwrite. Harden overwrites Ignivars Burn ( good for heor, unintended)
