from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, animal_type: str) -> None:
        self.name = name
        self.animal_type = animal_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.animal_type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, animal_type: str) -> None:
        super().__init__(name, animal_type)

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, animal_type: str) -> None:
        super().__init__(name, animal_type)

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, animal_type: str) -> None:
        super().__init__(name, animal_type)

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, animal_type: str) -> None:
        super().__init__(name, animal_type)

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self, name: str, anm_type: str) -> None:
        pass

    @abstractmethod
    def create_evolved(self, name: str, anm_type: str) -> None:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, name: str, anm_type: str) -> None:
        self.base = Flameling(name, anm_type)

    def create_evolved(self, name: str, anm_type: str) -> None:
        self.evolved = Pyrodon(name, anm_type)


class AquaFactory(CreatureFactory):
    def create_base(self, name: str, anm_type: str) -> None:
        self.base = Aquabub(name, anm_type)

    def create_evolved(self, name: str, anm_type: str) -> None:
        self.evolved = Torragon(name, anm_type)
