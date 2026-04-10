from ex2 import TransformCreatureFactory, HealingCreatureFactory
from ex2 import FlameFactory, AquaFactory, CreatureFactory
from ex2 import AggresiveStrategy, DefensiveStrategy, NormalStrategy
from ex2 import BattleStrategy, CreatureError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    try:
        print("*** Tournament ***")
        print(f"{len(opponents)} opponents involved\n")
        for one in range(len(opponents)):
            for two in range(one, len(opponents)):
                if opponents[one] != opponents[two]:
                    print("* Battle *")
                    print(opponents[one][0].base.describe())
                    print("vs.")
                    print(opponents[two][0].base.describe())
                    print("now fight!")
                    opponents[one][1].act(opponents[one][0].base)
                    opponents[two][1].act(opponents[two][0].base)
                    print()
    except CreatureError as error:
        print(error)
        print()


if __name__ == "__main__":
    defence = DefensiveStrategy()
    aggresive = AggresiveStrategy()
    normal = NormalStrategy()

    aqua = AquaFactory()
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    health = HealingCreatureFactory()

    factories = [aqua, flame, transform, health]

    for i in factories:
        i.create_base()
        i.create_evolved()

    opponents = [
        (aqua, normal),
        (flame, normal),
        (transform, aggresive),
        (health, defence)
    ]
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print()
    battle(opponents[1::2])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggresive), (Healing+Defensive) ]")
    print()
    battle([(flame, aggresive), (health, defence)])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print()
    battle([(aqua, normal), (health, defence), (transform, aggresive)])
