import json

class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str):
        self._ownership = character
    
    def to_json(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity,
            "ownership": self._ownership
        }

    @classmethod
    def from_json(cls, data):
        return cls(data['name'], data['description'], data['rarity'])

class Weapon(Item):
    def __init__(self, name, damage, weapon_type, description='', rarity='common'):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.weapon_type = weapon_type

    def to_json(self):
        data = super().to_json()
        data.update({"damage": self.damage, "weapon_type": self.weapon_type})
        return data

    @classmethod
    def from_json(cls, data):
        return cls(data['name'], data['damage'], data['weapon_type'], data['description'], data['rarity'])

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        item.pick_up(self.owner)
        self.items.append(item)

    def to_json(self):
        return {
            "owner": self.owner,
            "items": [item.to_json() for item in self.items]
        }

    @classmethod
    def from_json(cls, data):
        inventory = cls(data['owner'])
        for item_data in data['items']:
            item_type = globals()[item_data['type']]
            inventory.items.append(item_type.from_json(item_data))
        return inventory

# Example usage
if __name__ == "__main__":
    inv = Inventory("Beleg")
    sword = Weapon("Master Sword", 300, "sword", rarity="legendary")
    inv.add_item(sword)

    # Serialize to JSON
    json_data = json.dumps(inv.to_json(), indent=4)
    print("Serialized JSON:", json_data)

    # Deserialize from JSON
    new_inv = Inventory.from_json(json.loads(json_data))
    print("Deserialized Inventory Owner:", new_inv.owner)
