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

