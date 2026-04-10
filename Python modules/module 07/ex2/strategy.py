from abc import ABC, abstractmethod
from .creatures import Creature
from .health import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
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
    def act(self, creature: TransformCapability) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament:\
 Invalid Creature '{creature.name}' for this aggresive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
        print()

    def is_valid(self, creature: TransformCapability):
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: HealCapability) -> None:
        if not self.is_valid(creature):
            raise CreatureError(f"Battle error, aborting tournament:\
 Invalid Creature '{creature.name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: HealCapability):
        return isinstance(creature, HealCapability)
