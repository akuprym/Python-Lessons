
class Character:
    def __init__(self, level: int):
        self.level = level
        self.attack_power = self.base_attack_power * level
        self.health_points = self.base_health_points * level

    def atack(self, *, target: "Character"):
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    def is_alive(self) -> bool:
        return  self.health_points > 0

    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence

    @ property
    def max_health_points(self) -> int:
        return self.base_health_points * self.level

    def health_points_percent(self):
        return 100 * self.health_points / self.max_health_points

    def __str__(self):
        return (f"{self.character_name} (level: {self.level}, health points: {self.health_points})")


class Ork(Character):
    base_attack_power = 10
    base_health_points = 100
    base_defence = 15
    character_name = "Ork"

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3
        return defence


class Elf(Character):
    base_attack_power = 15
    base_health_points = 50
    base_defence = 10
    character_name = "Elf"

    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power = self.attack_power * 3
        print(f"Elf's attack power: {attack_power}")
        target.got_damage(damage=attack_power)


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.atack(target=character_2)
        if character_2.is_alive():
            character_2.atack(target=character_1)

    print(f"Character 1: {character_1}. is alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is alive: {character_2.is_alive()}")


ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork, character_2=elf)
