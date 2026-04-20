from abc import ABC, abstractmethod
from .creatures import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self):
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def revert(self):
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"

    def attack(self):
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self):
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        self.lvl = 0

    def transform(self) -> str:
        self.lvl = 1
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.lvl = 0
        return f"{self.name} returns to normal."

    def attack(self):
        if self.lvl:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        self.lvl = 0

    def transform(self) -> str:
        self.lvl = 1
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.lvl = 0
        return f"{self.name} stabilizes its form."

    def attack(self):
        if self.lvl:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
