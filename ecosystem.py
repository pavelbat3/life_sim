from organism import Organism


class Ecosystem:
    """Управление популяцией организмов"""

    def __init__(self):
        self.organisms = []

    def add_organism(self, organism: Organism):
        self.organisms.append(organism)

    def simulate_day(self):
        """Основной цикл симуляции"""
        for org in self.organisms:
            if org.is_alive():
                org.eat(10)
            else:
                print(f"{org.name} мёртв.")
