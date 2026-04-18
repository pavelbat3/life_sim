# organism.py


class Organism:
    """Представляет живой организм с именем и уровнем энергии."""

    def __init__(self, name: str, energy: float):
        """Инициализирует организм."""
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float):
        """Увеличивает уровень энергии организма при поглощении пищи."""
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        """Проверяет, жив ли организм (энергия больше нуля)."""
        return self.energy > 0
