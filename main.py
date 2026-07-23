import random
import data

MONSTER_COUNT = 0

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

        self.active_status = None
        self.status_turns_remaining = 0
        
        self.base_armor = self.armor
        self.base_aim = self.aim

        self.round = 1
        
    
    def win_round(self):
        self.round += 1
        self.health = self.character_data["health"]
        self.heals = self.character_data.get("heals", 0)
        self.special_uses = self.special.get("uses", 0)
        self.status_uses = self.status.get("uses", 0)

        self.armor = self.base_armor
        self.active_status = None
        self.status_turns_remaining = 0
        


    def is_alive (self):
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
        hit_num = random.randint(1,100)
        if hit_num <= self.aim:
            return True
        return False

    def crit_hit(self):
        crit_num = random.randint(1,100)
        if crit_num >= 90:
            return True
        return False
    
    def special_move(self):
        if self.special_uses == 0:
            return False
        self.special_uses -= 1
        return True
    
    def status_move(self):
        if self.status_uses == 0:
            return False
        if self.active_status is not None:
            return False
        self.status_uses -=1
        return True
    

class Battle:
    def __init__ (self, player, enemy):
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
        print(f"HP:     {self.player.health}/{self.player.max_health} | Type: {self.player.type} | Armor: {self.player.armor:.0%}")
        print(f"Attack: {self.player.attack} | Heals:  {self.player.heals}")
        print(f"Special Move: {self.player.special_name} | Type: {self.player.special_type} | Uses: {self.player.special_uses} | Damage: {self.player.special_damage}")
        print(f"Status Move: {self.player.status_name} | Turns: {self.player.status_turns_remaining} | Uses: {self.player.status_uses}")


        print("-" * 40)

        print(self.enemy.name)
        print(f"HP:     {self.enemy.health}/{self.enemy.max_health}")
        print(f"Attack: {self.enemy.attack}")
        print(f"Type: {self.enemy.type}")

        print("\n" + "=" * 40)
        print(f"          PAST TURN RESULTS")
        print("=" * 40)

        print(self.player_note)
        print(self.enemy_note)
        print("=" * 40 + "\n")

        print(f"Monsters Slayed: {MONSTER_COUNT}")
        print("=" * 40 + "\n")





    def attack(self, attacker, defender):
        if attacker.hit_chance() == True:
            modifier = data.type_chart[attacker.type].get(defender.type, 1)
            effectiveness = self.modifier_check(modifier)
            damage_taken = round(attacker.attack * (1 - defender.armor)*modifier)
            
            if attacker.crit_hit() == True:
                damage_taken *= 2
                defender.health -= damage_taken
                return f"{attacker.name} Landed a CRITICAL HIT {damage_taken} damage to {defender.name} {effectiveness}"
            
            defender.health -= damage_taken
            return f"{attacker.name} caused {damage_taken} damage to {defender.name} {effectiveness}"
        
        else:
            return f"{attacker.name} missed their attack!"
        
    def special_attack(self,attacker,defender):
        
        modifier = data.type_chart[attacker.special_type].get(defender.type, 1)
        effectiveness = self.modifier_check(modifier)
        damage_taken = round(attacker.special_damage * (1 - defender.armor)*modifier)
        
        defender.health -= damage_taken
        
        return f"{attacker.name} used {attacker.special_name}! It caused {damage_taken} damage to {defender.name} {effectiveness}"






    def status_inflict(self, character, enemy):

        if character.status_target == "self":


            if character.status_effect == "armor":
                armor_buff = data.status_chart["harden"].get("value")
                character.armor += armor_buff
                character.active_status = character.status_effect
                character.status_turns_remaining = character.status_turns

                return(
                    f"{character.name} used {character.status_name}! "
                    f"Armor increased by {armor_buff:.0%} "
                    f"for {character.status_turns} turns. "
                )


            if character.status_effect == "aim":
                aim_buff = data.status_chart["aim"].get("value")
                character.aim = aim_buff
                character.active_status = character.status_effect
                character.status_turns_remaining = character.status_turns

                return(
                    f"{character.name} used {character.status_name}! "
                    f"Aim increased to {character.aim}% "
                    f"for {character.status_turns} turns. "
                )
            


            if character.status_effect == "regen":
                regen_buff = data.status_chart["regen"].get("value")
                character.active_status = character.status_effect
                character.status_turns_remaining = character.status_turns

                return(
                    f"{character.name} used {character.status_name}! "
                    f"Health Regen increased by {regen_buff:.0%} "
                    f"for {character.status_turns} turns. "
                )  

        if character.status_target == "enemy":

            if character.status_effect == "poison":
                enemy.active_status = character.status_effect
                enemy.status_turns_remaining = character.status_turns

                return f"{character.name} used {character.status_name}! {enemy.name} has been Poisoned!"
            
        
        
        return f"{character.status_name} is not supported yet"
    





    def process_status_effects(self, character):
        if character.active_status is None:
            return ""
        
        character.status_turns_remaining -= 1


        if character.active_status == 'armor':
            if character.status_turns_remaining <= 0:
                character.armor = character.base_armor
                character.active_status = None
                return f"{character.status_name} has worn off from {character.name}."

        if character.active_status == 'aim':
            if character.status_turns_remaining <= 0:
                character.aim = character.base_aim
                character.active_status = None
                return f"{character.status_name} has worn off from {character.name}."


        if character.active_status == 'regen':
            if character.status_turns_remaining <= 0:
                character.active_status = None
                return f"{character.status_name} has worn off from {character.name}."
            
            regen_buff = data.status_chart["regen"].get("value")
            character.health += round(character.max_health * regen_buff)
            if character.health > character.max_health:
                character.health = character.max_health

            
        

        if character.active_status == "poison":
            if character.status_turns_remaining <= 0:
                character.active_status = None
                return f"{character.status_name} has worn off from {character.name}."            
            
    
            poison_damage = data.status_chart["poison"].get("value")
            poison_dealt = round(character.max_health * poison_damage)
            character.health -= poison_dealt
            if character.health < 0:
                character.health = 0
            return f"{character.name} took {poison_dealt} Poison Damage: {character.status_turns_remaining} turns of Poison Left" 

        

        return f"{character.status_name}: {character.status_turns_remaining} turns remaining."
    

    def modifier_check(self,modifier):
        if modifier > 1:
            effectiveness = ", It was extra effective!"
        elif modifier <1:
            effectiveness = ", It was less effective!"
        else:
            effectiveness = ""
        return effectiveness


    def enemy_turn(self):
        self.enemy_note = self.attack(self.enemy, self.player)


    def player_turn(self):
        print(f"{self.player.name}, What would you like to do?")
        print("[1] Attack")
        print("[2] Heal")
        print("[3] Special Attack")
        print("[4] Status Move")

        choice = input("> ")

        if choice == "1":
            self.player_note = self.attack(self.player,self.enemy)
        elif choice == "2":
            if self.player.heal() == True:
                self.player_note = f"{self.player.name} Healed 100 Points"
            else:
                self.player_note = f"{self.player.name} is out of Heals!"
                self.enemy_note = ""
                self.show_stats()
                return self.player_turn()
        elif choice =="3":
            if self.player.special_move() == True:
                self.player_note = self.special_attack(self.player, self.enemy)
            else:
                self.player_note = f"{self.player.name} is out of Specials!"
                self.enemy_note = ""
                self.show_stats()
                return self.player_turn()
        elif choice == "4":
            if self.player.status_move():
                self.player_note = self.status_inflict(self.player,self.enemy)
            else:
                self.player_note = (
                    f"{self.player.name} cannot use "
                    f"{self.player.status_name} right now!"
                )
                self.enemy_note = ""
                self.show_stats()
                return self.player_turn()
        else:
            self.player_note = f"Not a valid choice {self.player.name}, Try Again"
            self.enemy_note = ""
            self.show_stats()
            return self.player_turn()  
        
    def advance_turn(self):
        self.turn_count += 1
    


    def win_check(self):

        print("\n" + "=" * 40)
        print("              BATTLE OUTCOME")
        print("=" * 40)

        if self.enemy.health <= 0:
            print(f"{self.enemy.name} has been Slayed!")
            print("=" * 40 + "\n")
        else:
            MONSTER_COUNT += 1
            print(f"{self.player.name} has Fallen after slaying {MONSTER_COUNT} Monsters")
            print("=" * 40 + "\n")

    def next_round(self):
        self.turn_count = 0




##### GAME PLAY LOOP ######

##### HERO SELECTION ######
print("\n" + "=" * 40)
print("              HERO SELECTION")
print("=" * 40)

for index, hero in enumerate(data.heroes):
    print(f"[{index + 1}] {hero['name']} - {hero['role']} ")




## actually get choice of hero ##
hero_choice = int(input("\nWhich Hero, would you like to Summon?\n> "))
hero = Character(data.heroes[hero_choice - 1])


while hero.is_alive():

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
            break
                
        battle.enemy_turn()
       
        enemy_status_note = battle.process_status_effects(current_mob)
        if enemy_status_note:
            battle.enemy_note += f"\n{enemy_status_note}"
     
        if not current_mob.is_alive():
            current_mob.health = 0
            break
        
        if not hero.is_alive():
            hero.health = 0

        battle.advance_turn()
    
    battle.show_stats()

    if hero.is_alive():
        hero.win_round()
        battle.win_check()
        battle.next_round()
    else:
        battle.win_check()
        

    
