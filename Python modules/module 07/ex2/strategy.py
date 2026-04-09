from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    pass


class AggresiveStrategy(BattleStrategy):
    pass


class DefensiveStrategy(BattleStrategy):
    pass
