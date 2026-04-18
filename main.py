from ecosystem import Ecosystem
from organism import Organism


def main():
    eco = Ecosystem()
    # Создание трёх (3) объектов
    eco.add_organism(Organism("Заяц", 20))
    eco.add_organism(Organism("Лиса", 30))
    eco.add_organism(Organism("Растение", 30))

    eco.simulate_day()


if __name__ == "__main__":
    main()
