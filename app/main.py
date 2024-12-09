class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")

    def die(self) -> None:
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            herbivore.die()
            print(f"{herbivore.name} dies")

lion = Carnivore("King Lion")
rabbit = Herbivore("Susan", 25)
print(f"Num of animals: {len(Animal.alive)}")
print(rabbit in Animal.alive)
print(f"Rabbit health: {rabbit.health}")
lion.bite(rabbit)
print(f"Rabbit health: {rabbit.health}")
print(f"Rabbit is alive: {rabbit in Animal.alive}")
print(Animal.alive)
print(f"Num of animals: {len(Animal.alive)}")


# lion = Carnivore("Lion King")
# rabbit = Herbivore("Susan")
# print(f"Num of animals: {len(Animal.alive)}")
# print(rabbit in Animal.alive)
# print(f"Num of animals: {len(Animal.alive)}")
# print(f"Rabbit health: {rabbit.health}")
# lion.bite(rabbit)
# print(f"Rabbit health: {rabbit.health}")  # bited
#
# rabbit.hide()
# lion.bite(rabbit)
# print(f"Rabbit health: {rabbit.health}")  # lion cannot bite hidden rabbit
#
# rabbit.hide()
# lion.bite(rabbit)
# print(f"Rabbit health: {rabbit.health}")  # rabbit is dead
#
# print(f"Rabbit is alive: {rabbit in Animal.alive}")  # False
#
# print(Animal.alive)
# print(f"Num of animals: {len(Animal.alive)}")