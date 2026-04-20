from abc import ABC, abstractmethod
from .health import Sproutling, Shiftling, Bloomelle, Morphagon
from .creatures import Flameling, Aquabub, Pyrodon, Torragon
from .creatures import Creature


class CreatureFactory(ABC):
    def __init__(self) -> None:
        self.base: Creature
        self.evolved: Creature
        super().__init__()

    @abstractmethod
    def create_base(self) -> None:
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        pass


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> None:
        self.base = Sproutling()

    def create_evolved(self) -> None:
        self.evolved = Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> None:
        self.base = Shiftling()

    def create_evolved(self) -> None:
        self.evolved = Morphagon()


class FlameFactory(CreatureFactory):
    def create_base(self) -> None:
        self.base = Flameling("Flameling", "Fire")

    def create_evolved(self) -> None:
        self.evolved = Pyrodon("Pyrodon", "Fire/Bird")


class AquaFactory(CreatureFactory):
    def create_base(self) -> None:
        self.base = Aquabub("Aquabub", "Water")

    def create_evolved(self) -> None:
        self.evolved = Torragon("Torragon", "Water")
