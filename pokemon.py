class Pokemon:
    def __init__(self, name, level, ttype):
        self.name = name
        self.level = level
        self.type = ttype
        self.max_health = level * 10
        self.current_health = self.max_health
        self.is_knocked_out = False

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_type(self):
        return self.type
    
    def get_current_health(self):
        return self.current_health
    
    def lose_health(self, amount):
        self.current_health -= amount
        self.knocked_out()

        if not self.is_knocked_out:
            print(self.get_name(), "now has", self.get_current_health(), "HP.")

    def level_up(self):
        self.level += 1
        self.max_health = level * 10
        self.current_health = self.max_health
        print(self.get_name(), "now has", self.get_level())
    
    def level_down(self):
        self.level -= 1
        print(self.get_name(), "now has", self.get_level())    

    def restore_health(self):
        self.current_health = self.max_health

    def knocked_out(self, attacker):
        if self.current_health <= 0:
            self.is_knocked_out = True
            print(self.name, "has fallen.")
            return True

        return False

    def attack(self, victim):
        if self.type == 'Fire':
            if victim.type == 'Fire':
                victim.lose_health(self.level // 2)
            elif victim.type == 'Water':
                victim.lose_health(self.level // 2)
            elif victim.type == 'Grass':
                victim.lose_health(self.level)
        elif self.type == 'Water':
            if victim.type == 'Fire':
                victim.lose_health(self.level * 2)
            elif victim.type == 'Water':
                victim.lose_health(self.level // 2)
            elif victim.type == 'Grass':
                victim.lose_health(self.level // 2)
        elif self.type == 'Grass':
            if victim.type == 'Fire':
                victim.lose_health(self.level // 2)
            elif victim.type == 'Water':
                victim.lose_health(self.level * 2)
            elif victim.type == 'Grass':
                victim.lose_health(self.level // 2 )
        else:
            print("Type error. Pokemon type invalid.")


class Trainer:
    def __init__(self, name, active_pokemon):
        self.name = name
        self.potions = potions
        self.active_pokemon = active_pokemon
        self.potions = {
            "Healing": 2,
            "Reviving": 1,
            "Strengthen": 3,
            "Bandage": 4
        }

    def use_potion(self, potion_name):
        if potion_name not in potions:
            print("This is not a valid potion.")
        else:
            self.potions[potion_name] -= 1
            if potion_name == 'Healing':
                self.active_pokemon.restore_health()
                print(self.active_pokemon.get_name(), "currently has", self.active_pokemon.get_current_health())
            elif potion_name == 'Reviving':
                if self.active_pokemon.is_knocked_out:
                    self.active_pokemon.is_knocked_out = False
                    self.active_pokemon.restore_health()
                    print(self.active_pokemon.get_name(), "has been revived.")
            elif potion_name == 'Strengthen':
                self.active_pokemon.level_up()
            elif potion_name == 'Bandage':
                self.active_pokemon.current_health += self.active_pokemon.level
                if self.active_pokemon.get_current_health() > self.active_pokemon.max_health:
                    self.active_pokemon.current_health = self.active_pokemon.max_health
                print(self.active_pokemon.get_name(), "currently has", self.active_pokemon.get_current_health(), "HP.")

    def change_active_pokemon(self, new_active):
        self.active_pokemon = new_active

    


            

    
       

