class Character:
    def __init__(self, level: int):
        self.level = level
        self.attack_power = self.base_attack_power * level
        self.health_points = self.base_health_points * level

    def atack(self, *, target: "Character"):
        print(
            f"{self.character_name} attacks {target.character_name} ({target.health_points} health points)"
            f" with {self.attack_power} power."
        )
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} has hp {target.health_points}")

    def is_alive(self) -> bool:
        return  self.health_points > 0

    def __str__(self):
        return (f"self.character_name with level: {self.level}, health points: {self.health_points} " and
                f"with attack power {self.attack_power}")


class Ork(Character):
    base_attack_power = 10
    base_health_points = 100
    character_name = "Ork"


class Elf(Character):
    base_attack_power = 15
    base_health_points = 50
    character_name = "Elf"


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.atack(target=character_2)
        if character_2.is_alive():
            character_2.atack(target=character_1)

    print(f"Character 1: {character_1}, is alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is alive: {character_2.is_alive()}")


ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork, character_2=elf)


"""
class Ork:
    def __init__(self, level: int) -> None:
        self.level = level
        self.attack_power = level * 100
        self.health_points = level * 10

    def atack(self):
        print(f"Ork attacks with {ork.attack_power} power")

# IMPORTANT! How to print Ork class:
    def __str__(self):
        return f"Ork with level: {self.level}, health points: {self.health_points}"

ork = Ork(level=5)
ork.atack()
print(ork)

"""