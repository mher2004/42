from abc import ABC, abstractmethod
from .creatures import Creature
from .health import TransformCapability, HealCapability
from .health import Shiftling, Morphagon, Sproutling, Bloomelle
from typing import Any, Union


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creatur: Any) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass


class CreatureError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament:\
 Invalid Creature '{creature.name}' for this normal strategy")
        print(creature.attack())

    def is_valid(self, creature: Creature):
        return isinstance(creature, Creature)


class AggresiveStrategy(BattleStrategy):
    def act(self, creature: Union[Shiftling, Morphagon]) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament:\
 Invalid Creature '{creature.name}' for this aggresive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
        print()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Union[Sproutling, Bloomelle]) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament:\
 Invalid Creature '{creature.name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: Creature):
        return isinstance(creature, HealCapability)
