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
        return self.attack_move() + f" {self.name} is used, dealing {round(self.damage * self.attack_modifier)} damage."
    
    def attack_move(self):
        return "Attacks generically with weapon."

class SingleHandedWeapon(Weapon):
    def __init__(self, name, damage, weapon_type='sword', description='', rarity='common'):
        super().__init__(name, damage, weapon_type, description, rarity)
    
    def attack_move(self):
        return f"{self._ownership} slashes swiftly with {self.name}."

class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} spins powerfully with {self.name}."

class Pike(Weapon):
    def attack_move(self):
        return f"{self._ownership} thrusts forward with {self.name}."

class RangedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} shoots precisely with {self.name}."

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

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []
    
    def add_item(self, item: Item):
        item.pick_up(self.owner)
        self.items.append(item)
        print(f"{item.name} was added to backpack")
    
    def drop_item(self, item: Item):
        if item in self.items:
            item.throw_away()
            self.items.remove(item)
            print(f"{item.name} was dropped from backpack")
    
    def view(self, item_type=None):
        if item_type:
            return [str(item) for item in self.items if isinstance(item, item_type.__class__)]
        return [str(item) for item in self.items]
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items

# Example Usage
if __name__ == "__main__":
    beleg_backpack = Inventory(owner='Beleg')
    master_sword = SingleHandedWeapon(name='Master Sword', damage=300, weapon_type='sword', rarity='legendary')
    muramasa = DoubleHandedWeapon(name='Muramasa', damage=580, weapon_type='katana', rarity='legendary')
    gungnir = Pike(name='Gungnir', damage=290, weapon_type='spear', rarity='legendary')
    belthronding = RangedWeapon(name='Belthronding', damage=500, weapon_type='bow', rarity='legendary')
    
    beleg_backpack.add_item(master_sword)
    beleg_backpack.add_item(muramasa)
    beleg_backpack.add_item(gungnir)
    beleg_backpack.add_item(belthronding)
    
    if master_sword in beleg_backpack:
        print(master_sword.equip())
        print(master_sword.use())
    
    print(beleg_backpack.view())

    beleg_backpack.drop_item(muramasa)
    print(beleg_backpack.view())