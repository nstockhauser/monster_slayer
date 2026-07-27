# Monster Slayer RPG Roadmap

---

# Version 1.0 — Core Combat ✅

Version 1 establishes the complete command-line combat foundation.

## Heroes

- 4 playable heroes
- Each hero has:
  - 1 Special Move
  - 1 Status Move

## Bosses

- 6 bosses
- Each boss has a unique Phase 2 ability
- Phase 2 activates when the boss reaches low health

## Combat Systems

- Standard attacks
- Critical hits
- Healing
- Special attacks
- Status effects
- Type effectiveness
- Boss Phase 2 mechanics

## Version 1 Status

**Complete**

No additional features will be added to Version 1.

---

# Version 1.5 — Refactor and Presentation

Version 1.5 improves the existing game code without adding any gameplay systems.

## Code Refactor

- Clean up combat logic
- Improve file organization
- Reduce duplicate code
- Improve naming
- Simplify large functions
- Separate responsibilities between classes and methods
- Fix known bugs and edge cases

## Presentation

- Add color-coded terminal text
- Improve combat message readability
- Make Special Moves visually distinct
- Make boss Phase 2 attacks visually distinct
- Improve menu formatting
- Improve battle result formatting

---

# Version 2.0 - Onslaught Mode

- Onslaught Mode
- 5 playable heroes
- 10-monsters
- High-score system

## Onslaught Mode

- Add an explicit main menu
- Select Onslaught Mode from the menu
- Choose 1 hero
- Fight through as many monsters as you can before you fall
- Display the player’s final score
- Save and display the high score

## v2.0 Monsters and Ultimates

| Monster            | Identity        | Ultimate               | Trigger       | Effect                                                                                                                                                          | Duration               |
| ------------------ | --------------- | ---------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| 🔥 **Ignivar**     | Fire Lord       | **Infernal Cataclysm** | 33% HP        | Immediately deals **40 Fire Damage**, then applies **Burn** for **3 turns**. Burn damage each turn = **50% of Ignivar's Attack**.                               | Burn lasts **3 Turns** |
| ❄ **Frost Maw**    | Executioner     | **Winterbane**         | 33% HP        | Unleashes a **Guaranteed Ice Blast** dealing **150–175 Magic Damage**. Pure burst damage.                                                                       | Instant                |
| 🪨 **Gravemantle** | Living Mountain | **Avalanche**          | 33% HP        | Causes **2–6 falling boulders**. Each boulder deals **20 Physical Damage** with **75% accuracy**. Every boulder hit lowers armor by 5% permanently.             | Instant                |
| ✨ **Veyra**       | Holy Guardian   | **Divine Ascension**   | 33% HP        | Restores health to **60% Max HP**, gains **+20 Armor** and **+20 Attack** for the remainder of the battle.                                                      | Until Defeated         |
| 🌑 **Umbra**       | Shadow Assassin | **Into the Shadows**   | 33% HP        | Gains **50% Dodge Chance** and **+20 Aim**, becoming extremely difficult to finish off.                                                                         | **3 Turns**            |
| 🔮 **Vorath**      | Archmage        | **Arcane Convergence** | 33% HP        | Randomly selects **3 unique elements**. Each launches a **Guaranteed Magic Attack** dealing **40 Base Damage**, modified by elemental strengths and weaknesses. | Instant                |
| 👑 **Goblin King** | Horde Commander | **Minion Swarm**       | Every 3 Turns | Commands his minions to perform **2–5 separate attacks** against the hero.                                                                                      | Recurring              |

---

## v2.0 Heroes and Moves

| Hero             | Identity                    | Special                                                                                          | Status                                                                                                |
| ---------------- | --------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| 🛡️ **Lionheart** | Unkillable Tank             | **Retribution** – For **3 turns**, reflects **50% of all damage received** back to the attacker. | **Iron Wall** – Increases Armor by **50%** for **3 turns**.                                           |
| 🏹 **Vex**       | Rogue Assassin              | **Assassinate** – A **Guaranteed Critical Hit** that **ignores Armor** against a single target.  | **Poison Dart** – Poisons the enemy for **4 turns**, dealing damage over time.                        |
| ☀️ **Solara**    | Cleric / Paladin            | **Smite** – Deals **85 Holy Damage** and heals Solara for **40 HP**.                             | **Blessing of Sol** – Restores **5% Max Health** each turn for **5 turns**.                           |
| 🪄 **Savos**     | Glass Cannon / Mage Scholar | **Arcane Barrage** – Fires **3 Arcane Missiles**, each dealing **40 Magic Damage**.              | **Arcane Overload** – The next spell deals **300% damage**. Can be used **twice per battle**.         |
| 🪓 **Barbarian** | Reckless Bruiser            | **Cripple** – Deals damage and reduces the enemy's **Speed**.                                    | **Berserk** – Increases the Barbarian's **Attack**, but lowers his own **Accuracy** for the duration. |

---

# Version 3.0 — Adventure Mode

Version 3 introduces boss battles, teammates, and team-based Special Moves.

## Adventure Mode

Each adventure contains:

- 3 standard monster battles
- 1 boss battle

Before the boss fight:

- Choose 1 teammate
- Enter the boss battle as a two-hero team

## Team Special Moves

- Add team-based Special Moves
- Team Moves are only available during boss battles
- Team Moves depend on the selected hero combination

# Future Team Move Concepts

| Hero             | Team Move            | Effect                                                     | Uses |
| ---------------- | -------------------- | ---------------------------------------------------------- | ---- |
| 🛡️ **Lionheart** | **Protect**          | Blocks the next attack against an ally.                    | 2    |
| 🏹 **Vex**       | **Marked for Death** | The next attack against the target deals increased damage. | 2    |
| 🪓 **Barbarian** | **Sweep**            | Damages all enemies.                                       | 2    |
| ☀️ **Solara**    | **Cleanse**          | Removes all status effects and blocks the next one.        | 2    |
| 🪄 **Savos**     | **Elemental Shift**  | Changes an ally's elemental type.                          | 2    |

# Future Boss Concepts

| Boss                | Identity       | Signature Ability            | Core Mechanic                                        |
| ------------------- | -------------- | ---------------------------- | ---------------------------------------------------- |
| 🟢 **Slimer**       | Living Blob    | **Blob Split** _(TBD)_       | High durability and slime-based battlefield control. |
| ☠️ **Death Knight** | Undead Warlord | **Army of the Dead** _(TBD)_ | Drains health and summons undead minions.            |

---

# Version 4.0 — Pygame Desktop Release

Version 4 is entirely focused on converting the finished command-line game into a desktop application.

## Goals

- Build the graphical version using Pygame
- Replace terminal menus with a graphical interface
- Replace text-only combat presentation with visual battle screens
- Package the game as a desktop application
- Launch the game from a desktop icon
- Eliminate the need to run the game manually from the command line

## Version 4 Scope

Version 4 does not add _ANY_ new gameplay systems.

Its purpose is to present the completed game through a proper desktop interface.

---

# Scope Lock

The Current Roadmap ends with Version 4.
