import random
import data


class Character:
    def __init__(self, character_data):
        self.character_data = character_data

        self.name = character_data["name"]
        self.type = character_data["type"]
        self.health = character_data["health"]
        self.max_health = character_data["max_health"]
        self.attack = character_data["attack"]
        self.aim = character_data["aim"]
        self.armor = character_data["armor"]
        self.heals = character_data.get("heals", 0)
        self.speed = character_data.get("speed", 0)
        self.icon = character_data.get("icon", "none")

        self.special = character_data.get("special", {})
        self.special_name = self.special.get("name", "None")
        self.special_type = self.special.get("type", "None")
        self.special_uses = self.special.get("uses", 0)
        self.special_damage = self.special.get("damage", 0)

        self.status = character_data.get("status", {})
        self.status_name = self.status.get("name", "None")
        self.status_effect = self.status.get("effect", "None")
        self.status_target = self.status.get("target", "None")
        self.status_uses = self.status.get("uses", 0)
        self.status_turns = self.status.get("turns", 0)

        # Runtime status information.
        self.active_status = None
        self.active_status_name = None
        self.status_turns_remaining = 0

        self.base_armor = self.armor
        self.base_aim = self.aim

        # Each monster can use its phase-two move only once.
        self.phase_2_triggered = False
        self.charging = False

        # These are mostly meaningful for the selected hero.
        self.round = 1
        self.monsters_slain = 0

    def win_round(self):
        self.round += 1
        self.health = self.character_data["health"]
        self.heals = self.character_data.get("heals", 0)
        self.special_uses = self.special.get("uses", 0)
        self.status_uses = self.status.get("uses", 0)

        self.armor = self.base_armor
        self.aim = self.base_aim
        self.active_status = None
        self.active_status_name = None
        self.status_turns_remaining = 0
        self.phase_2_triggered = False

    def is_alive(self):
        if self.health > 0:
            return True

        self.health = 0
        return False

    def heal(self):
        if self.heals == 0:
            return False

        self.heals -= 1
        self.health += 100

        if self.health > self.max_health:
            self.health = self.max_health

        return True

    def hit_chance(self):
        hit_num = random.randint(1, 100)
        return hit_num <= self.aim

    def crit_hit(self):
        crit_num = random.randint(1, 100)
        return crit_num >= 90

    def special_move(self):
        if self.special_uses == 0:
            return False

        self.special_uses -= 1
        return True

    def status_move(self):
        if self.status_uses == 0:
            return False

        self.status_uses -= 1
        return True

    def phase_2_check(self):
        if self.phase_2_triggered:
            return False

        health_percentage = self.health / self.max_health

        if health_percentage <= .33:
            return True

        return False


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.player_note = ""
        self.enemy = enemy
        self.enemy_note = ""
        self.turn_count = 0
        self.round_count = 1

    def show_stats(self):
        print("\n" + "=" * 40)
        print("              BATTLE STATS")
        print("=" * 40)

        print(self.player.name)
        print(
            f"HP:     {self.player.health}/{self.player.max_health} | "
            f"Type: {self.player.type} | Armor: {self.player.armor:.0%}"
        )
        print(f"Attack: {self.player.attack} | Heals: {self.player.heals}")
        print(
            f"Special Move: {self.player.special_name} | "
            f"Type: {self.player.special_type} | "
            f"Uses: {self.player.special_uses} | "
            f"Damage: {self.player.special_damage}"
        )
        print(
            f"Status Move: {self.player.status_name} | "
            f"Active Status: {self.player.active_status_name or 'None'} | "
            f"Turns: {self.player.status_turns_remaining} | "
            f"Uses: {self.player.status_uses}"
        )

        print("-" * 40)

        print(self.enemy.name)
        print(f"HP:     {self.enemy.health}/{self.enemy.max_health}")
        print(f"Attack: {self.enemy.attack}")
        print(f"Type: {self.enemy.type}")
        print(
            f"Active Status: {self.enemy.active_status_name or 'None'} | "
            f"Turns: {self.enemy.status_turns_remaining}"
        )

        print("\n" + "=" * 40)
        print("          PAST TURN RESULTS")
        print("=" * 40)

        print(self.player_note)
        print(self.enemy_note)
        print("=" * 40 + "\n")

        print(f"Monsters Slayed: {self.player.monsters_slain}")
        print("=" * 40 + "\n")

    def attack(self, attacker, defender):
        if attacker.hit_chance():
            modifier = data.type_chart.get(attacker.type, {}).get(defender.type, 1)
            effectiveness = self.modifier_check(modifier)
            damage_taken = round(
                attacker.attack
                * (1 - defender.armor)
                * modifier
            )

            if attacker.crit_hit():
                damage_taken *= 2
                defender.health -= damage_taken
                return (
                    f"{attacker.name} landed a CRITICAL HIT for "
                    f"{damage_taken} damage to {defender.name}{effectiveness}"
                )

            defender.health -= damage_taken
            return (
                f"{attacker.name} caused {damage_taken} damage "
                f"to {defender.name}{effectiveness}"
            )

        return f"{attacker.name} missed their attack!"

    def special_attack(self, attacker, defender):
        # Unknown or non-elemental special types receive a neutral modifier.
        modifier = data.type_chart.get(attacker.special_type, {}).get(
            defender.type,
            1,
        )
        effectiveness = self.modifier_check(modifier)

        if attacker.special_name == "Winterbane":
            if not attacker.charging:
                attacker.charging = True
                return "Frostmaw is Charging Winterbane......"

            attacker.charging = False

            damage_taken = round(attacker.special_damage * (1 - defender.armor) * modifier) 
            defender.health -= damage_taken


            return (
                f"FROSTMAW UNLEASHED WINTERBANE!! "
                f"It caused {damage_taken} damage to "
                f"{defender.name}{effectiveness}"
            )

        if attacker.special_name == "Avalanche":

            damage_taken = round(attacker.special_damage * (1 - defender.armor) * modifier) 
            defender.health -= damage_taken

            defender.armor -= .10

            return (
                f"GRAVEMANTLE TRIGGERED AVALANCHE!! "
                f"{defender.name}'s armor has been reduced by 10% "
                f"It caused {damage_taken} damage to "
                f"{defender.name}{effectiveness}"
            )



        if attacker.special_name == "Divine Blessing":

            attacker.health = round(attacker.max_health * .60)
            attacker.attack = round(attacker.attack * 1.20)

            return (
                f"VEYRA RECIEVED A DIVINGE BLESSING!! "
                f"{attacker.name}'s Health has increased to 60% "
                f"{attacker.name}'s Attack has increased by 20% "
            )





        if attacker.special_name == "Slaughter":
            hits_landed = []
            num_hits = random.randint(2,5)
            total_damage = 0

            for hit in range(num_hits):
                damage_taken = round(attacker.special_damage * modifier)
                defender.health -= damage_taken
                total_damage += damage_taken

                hits_landed.append(f"hit #{hit + 1} landed for {damage_taken} Damage")

            
            return (
                f"\n UMBROS WENT ON A SLAUGHTER!! \n\n"
                + "\n".join(hits_landed)
                + f"\n\n{attacker.name} landed {num_hits} "
                f"for a total of {total_damage} damage"
            )


        if attacker.special_name == "Elemental Storm":
            hits_landed = []
            num_hits = 3
            total_damage = 0

            elements = ["fire", "ice", "rock", "magic", "dark", "holy"]

            for hit in range(num_hits):
                attack_element = random.choice(elements)
                
                modifier = data.type_chart.get(attack_element, {}).get(
                defender.type, 1)

                effectiveness = self.modifier_check(modifier)

                damage_taken = round(attacker.special_damage * (1 - defender.armor) * modifier)
                defender.health -= damage_taken
                total_damage += damage_taken

                hits_landed.append(f"Element {attack_element.title()} hit for {damage_taken} Damage {effectiveness}")

            
            return (
                f"\n VORATH CREATED AN ELEMENTAL STORM \n\n"
                + "\n".join(hits_landed)
                + f"\n\nThe Elemental Storm raged for a total of {total_damage} damage"
            )



        damage_taken = round(
            attacker.special_damage
            * (1 - defender.armor)
            * modifier
        )

        defender.health -= damage_taken

        return (
            f"{attacker.name} used {attacker.special_name}! "
            f"It caused {damage_taken} damage to "
            f"{defender.name}{effectiveness}"
        )

    def status_inflict(self, character, enemy):
        if character.status_target == "self":
            if character.status_effect == "armor":
                armor_buff = data.status_chart["harden"].get("value", 0)
                character.armor += armor_buff
                character.active_status = "armor"
                character.active_status_name = character.status_name
                character.status_turns_remaining = character.status_turns

                return (
                    f"{character.name} used {character.status_name}! "
                    f"Armor increased by {armor_buff:.0%} "
                    f"for {character.status_turns} turns."
                )

            if character.status_effect == "aim":
                aim_buff = data.status_chart["aim"].get("value", 100)
                character.aim = aim_buff
                character.active_status = "aim"
                character.active_status_name = character.status_name
                character.status_turns_remaining = character.status_turns

                return (
                    f"{character.name} used {character.status_name}! "
                    f"Aim increased to {character.aim}% "
                    f"for {character.status_turns} turns."
                )

            if character.status_effect == "regen":
                regen_buff = data.status_chart["regen"].get("value", 0)
                character.active_status = "regen"
                character.active_status_name = character.status_name
                character.status_turns_remaining = character.status_turns

                return (
                    f"{character.name} used {character.status_name}! "
                    f"Health regeneration increased by {regen_buff:.0%} "
                    f"for {character.status_turns} turns."
                )

            if character.status_effect == "recover":
                recover_amount = data.status_chart["recover"].get("value", 0)
                old_health = character.health
                character.health += recover_amount

                if character.health > character.max_health:
                    character.health = character.max_health

                health_recovered = character.health - old_health

                return (
                    f"{character.name} used {character.status_name} and "
                    f"recovered {health_recovered} health!"
                )

        if character.status_target == "enemy":
            if enemy.active_status is not None:
                return (
                    f"{character.name} tried to use {character.status_name}, "
                    f"but {enemy.name} is already affected by "
                    f"{enemy.active_status_name}!"
                )

            if character.status_effect == "poison":
                enemy.active_status = "poison"
                enemy.active_status_name = character.status_name
                enemy.status_turns_remaining = character.status_turns

                return (
                    f"{character.name} used {character.status_name}! "
                    f"{enemy.name} has been poisoned!"
                )

            if character.status_effect == "burn":
                enemy.active_status = "burn"
                enemy.active_status_name = character.status_name
                enemy.status_turns_remaining = character.status_turns
                enemy.status_caster = character

                return (
                    f"{character.name} used {character.status_name}! "
                    f"{enemy.name} has been burned!"
                )

        return f"{character.status_name} is not supported yet."

    def clear_active_status(self, character):
        character.active_status = None
        character.active_status_name = None
        character.status_turns_remaining = 0

    def process_status_effects(self, character):
        if character.active_status is None:
            return ""

        character.status_turns_remaining -= 1

        if character.active_status == "armor":
            if character.status_turns_remaining <= 0:
                expired_status_name = character.active_status_name
                character.armor = character.base_armor
                self.clear_active_status(character)
                return (
                    f"{expired_status_name} has worn off from "
                    f"{character.name}."
                )

            return (
                f"{character.active_status_name}: "
                f"{character.status_turns_remaining} turns remaining."
            )

        if character.active_status == "aim":
            if character.status_turns_remaining <= 0:
                expired_status_name = character.active_status_name
                character.aim = character.base_aim
                self.clear_active_status(character)
                return (
                    f"{expired_status_name} has worn off from "
                    f"{character.name}."
                )

            return (
                f"{character.active_status_name}: "
                f"{character.status_turns_remaining} turns remaining."
            )

        if character.active_status == "regen":
            if character.status_turns_remaining <= 0:
                expired_status_name = character.active_status_name
                self.clear_active_status(character)
                return (
                    f"{expired_status_name} has worn off from "
                    f"{character.name}."
                )

            regen_percent = data.status_chart["regen"].get("value", 0)
            regen_amount = round(character.max_health * regen_percent)
            old_health = character.health
            character.health += regen_amount

            if character.health > character.max_health:
                character.health = character.max_health

            health_recovered = character.health - old_health

            return (
                f"{character.name} recovered {health_recovered} health. "
                f"{character.status_turns_remaining} turns of "
                f"{character.active_status_name} remain."
            )

        if character.active_status == "poison":
            if character.status_turns_remaining <= 0:
                expired_status_name = character.active_status_name
                self.clear_active_status(character)
                return (
                    f"{expired_status_name} has worn off from "
                    f"{character.name}."
                )

            poison_percent = data.status_chart["poison"].get("value", 0)
            poison_damage = round(character.max_health * poison_percent)
            character.health -= poison_damage

            if character.health < 0:
                character.health = 0

            return (
                f"{character.name} took {poison_damage} poison damage. "
                f"{character.status_turns_remaining} turns of poison remain."
            )



        if character.active_status == "burn":
            if character.status_turns_remaining <= 0:
                expired_status_name = character.active_status_name
                self.clear_active_status(character)
                return (
                    f"{expired_status_name} has worn off from "
                    f"{character.name}."
                )

            burn_percent = data.status_chart["burn"].get("value", 0)
            
            burn_damage = round(
                character.status_caster.attack * burn_percent
                )
            
            character.health -= burn_damage

            if character.health < 0:
                character.health = 0

            return (
                f"{character.name} took {burn_damage} burn damage. "
                # f"{character.status_turns_remaining} turns of burn remain."
            )

        unknown_status = character.active_status_name or character.active_status
        self.clear_active_status(character)
        return f"{unknown_status} is not a supported active status."

    def modifier_check(self, modifier):
        if modifier > 1:
            return ", it was extra effective!"

        if modifier < 1:
            return ", it was less effective!"

        return ""

    def enemy_turn(self, character):

        if character.charging:
            self.enemy_note = self.special_attack(character, self.player)
            return
          
        if character.phase_2_check():
            character.phase_2_triggered = True

            if character.special_name != "None":
                if character.special_move():
                    self.enemy_note = self.special_attack(
                        character,
                        self.player,
                    )
                    return

            if character.status_name != "None":
                if character.status_move():
                    self.enemy_note = self.status_inflict(
                        character,
                        self.player,
                    )
                    return

        self.enemy_note = self.attack(character, self.player)

    def player_turn(self):
        print(f"{self.player.name}, what would you like to do?")
        print("[1] Attack")
        print("[2] Heal")
        print("[3] Special Attack")
        print("[4] Status Move")

        choice = input("> ")

        if choice == "1":
            self.player_note = self.attack(self.player, self.enemy)
            return

        if choice == "2":
            if self.player.heal():
                self.player_note = f"{self.player.name} healed 100 points."
                return

            self.player_note = f"{self.player.name} is out of heals!"
            self.enemy_note = ""
            self.show_stats()
            return self.player_turn()

        if choice == "3":
            if self.player.special_move():
                self.player_note = self.special_attack(
                    self.player,
                    self.enemy,
                )
                return

            self.player_note = f"{self.player.name} is out of specials!"
            self.enemy_note = ""
            self.show_stats()
            return self.player_turn()

        if choice == "4":
            if self.player.status_move():
                self.player_note = self.status_inflict(
                    self.player,
                    self.enemy,
                )
                return

            self.player_note = (
                f"{self.player.name} cannot use "
                f"{self.player.status_name} right now!"
            )
            self.enemy_note = ""
            self.show_stats()
            return self.player_turn()

        self.player_note = (
            f"Not a valid choice, {self.player.name}. Try again."
        )
        self.enemy_note = ""
        self.show_stats()
        return self.player_turn()

    def advance_turn(self):
        self.turn_count += 1

    def win_check(self):
        print("\n" + "=" * 40)
        print(f"              BATTLE OUTCOME ({self.turn_count} Turns)")
        print("=" * 40)

        if self.enemy.health <= 0:
            self.player.monsters_slain += 1
            print(f"{self.enemy.name} has been slain!")
            print(
                f"{self.player.name} has now slain "
                f"{self.player.monsters_slain} monsters."
            )
            print("=" * 40 + "\n")
            return

        print(
            f"{self.player.name} has fallen after slaying "
            f"{self.player.monsters_slain} monsters."
        )
        print("=" * 40 + "\n")

    def next_round(self):
        self.turn_count = 0


# GAMEPLAY LOOP

# HERO SELECTION
print("\n" + "=" * 40)
print("              HERO SELECTION")
print("=" * 40)

for index, hero_data in enumerate(data.heroes):
    print(f"[{index + 1}] {hero_data['name']} - {hero_data['role']}")

while True:
    try:
        hero_choice = int(
            input("\nWhich hero would you like to summon?\n> ")
        )

        if 1 <= hero_choice <= len(data.heroes):
            break

        print("Please choose one of the listed hero numbers.")

    except ValueError:
        print("Please enter a number.")

hero = Character(data.heroes[hero_choice - 1])

while hero.is_alive():
    # Use this line when testing one specific monster.
    # current_mob = Character(data.monsters[0])

    # Use this line when you want random monsters instead.
    current_mob = Character(random.choice(data.monsters))

    battle = Battle(hero, current_mob)

    print(f"\nROUND {hero.round}")
    print(f"{current_mob.name} appears!")

    while hero.is_alive() and current_mob.is_alive():
        battle.show_stats()
        battle.player_turn()

        hero_status_note = battle.process_status_effects(hero)
        if hero_status_note:
            battle.player_note += f"\n{hero_status_note}"

        if not current_mob.is_alive():
            current_mob.health = 0
            battle.enemy_note = ""
            break

        battle.enemy_turn(current_mob)

        enemy_status_note = battle.process_status_effects(current_mob)
        if enemy_status_note:
            battle.enemy_note += f"\n{enemy_status_note}"

        if not current_mob.is_alive():
            current_mob.health = 0
            break

        if not hero.is_alive():
            hero.health = 0
            break

        battle.advance_turn()

    battle.show_stats()
    battle.win_check()

    if hero.is_alive():
        hero.win_round()
        battle.next_round()
