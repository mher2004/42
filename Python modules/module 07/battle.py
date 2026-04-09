from ex0 import AquaFactory, FlameFactory
from typing import Union


def testing_factory(
        factory: Union[FlameFactory, AquaFactory],
        names: list[str],
        types:  list[str]
        ) -> None:
    print("Testing factory")
    factory.create_base(names[0], types[0])
    factory.create_evolved(names[1], types[1])
    print(factory.base.describe())
    print(factory.base.attack())
    print(factory.evolved.describe())
    print(factory.evolved.attack())
    print()


def testing_battle(
        factory: list[Union[FlameFactory, AquaFactory]],
        names: list[str],
        types:  list[str]
        ) -> None:
    print("Testing battle")
    factory[0].create_base(names[0], types[0])
    factory[1].create_base(names[1], types[1])
    print(factory[0].base.describe())
    print("vs.")
    print(factory[1].base.describe())
    print("Fight!!!")
    print(factory[0].base.attack())
    print(factory[1].base.attack())


if __name__ == "__main__":
    names = ["Flameling", "Pyrodon",
             "Aquabub", "Torragon"]
    types = ["Fire", "Fire/Flying",
             "Water", "Water"]
    flame = FlameFactory()
    aqua = AquaFactory()
    testing_factory(flame, names[:2], types[:2])
    testing_factory(aqua, names[2:], types[2:])
    testing_battle([flame, aqua], names[::2], types[::2])
