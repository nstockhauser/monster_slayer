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

| Feature               | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| **Basic Attack**      | Standard monster attack.                                            |
| **Unique Elements**   | Each monster has its own elemental affinity and stat distribution.  |
| **Phase 2 Abilities** | Planned for a future update, unlocking new abilities at low health. |

---

### 👹 Current Monsters

| Monster         | Element | Specialty                                                                        |
| --------------- | ------- | -------------------------------------------------------------------------------- |
| **Ignivar**     | Fire    | A balanced fighter with solid damage and durability.                             |
| **Frostmaw**    | Ice     | A defensive monster with high health and armor that excels in prolonged battles. |
| **Gravemantle** | Rock    | A heavily armored juggernaut that slowly wears down opponents.                   |
| **Veyra**       | Holy    | A fast, high-accuracy monster that relies on precise attacks.                    |
| **Umbros**      | Dark    | A glass cannon with devastating attacks but poor accuracy and low defenses.      |
| **Magis**       | Magic   | A well-rounded spellcaster with balanced offense, accuracy, and survivability.   |
