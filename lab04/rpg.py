class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is now owned by {character}."
    
    def throw_away(self):
        self._ownership = ''
        return f"{self.name} is thrown away."
    
    def use(self):
        if not self._ownership:
            return "NO OUTPUT"
        return f"{self.name} is used."

    def __str__(self):
        return f"{self.name} ({self.rarity}) - {self.description}"

class Weapon(Item):
    def __init__(self, name, damage, weapon_type, description='', rarity='common'):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
    
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        return f"{self.name} is used, dealing {round(self.damage * self.attack_modifier)} damage."

class Shield(Item):
    def __init__(self, name, defense, broken=False, description='', rarity='common'):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.10 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
    
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        modifier = 0.5 if self.broken else 1.0
        return f"{self.name} is used, blocking {round(self.defense * self.defense_modifier * modifier)} damage."

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, description='', rarity='common'):
        super().__init__(name, description, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.used = False
    
    def use(self):
        if not self._ownership or self.used:
            return "NO OUTPUT"
        self.used = True
        return f"{self._ownership} used {self.name}, and {self.potion_type} increased by {self.value} for {self.effective_time}s."
    
    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name, potion_type, value=50, effective_time=30, rarity='common')
        potion.pick_up(owner)
        return potion

# Example Usage
if __name__ == "__main__":
    sword = Weapon(name='Excalibur', damage=100, weapon_type='sword', rarity='legendary')
    print(sword.pick_up('Arthur'))
    print(sword.equip())
    print(sword.use())
    print(sword.throw_away())
    print(sword.use())
    
    shield = Shield(name='Aegis', defense=50, broken=False, rarity='epic')
    print(shield.pick_up('Zeus'))
    print(shield.equip())
    print(shield.use())
    
    potion = Potion.from_ability(name='Power Boost', owner='Athena', potion_type='attack')
    print(potion)
    print(potion.use())
    print(potion.use())
