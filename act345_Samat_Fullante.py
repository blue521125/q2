#Activity 3
class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

#Activity 4
class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

perform_move(Warrior())
perform_move(Mage())
perform_move(Archer())

apply_item(HealthPotion())
apply_item(ManaPotion())
apply_item(SpeedBoost())

print("1. These methods do not care what the object is, it only works. It doesnt belond to a single class.")
print("2. It shows how different objects respond to the same command in different ways.")
print("3. Other examples are how guns fire, one can shoot bullets everywhere, one makes a laser, and more. Enemies too, they can go toward you, flee from you, or go around you.")
