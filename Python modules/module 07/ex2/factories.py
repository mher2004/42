from abc import ABC, abstractmethod
from health import Sproutling, Shiftling, Bloomelle, Morphagon


class CreatureFactory(ABC):
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
