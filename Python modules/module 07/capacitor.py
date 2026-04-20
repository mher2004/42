from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_healing(
        factory: HealingCreatureFactory
        ) -> None:
    factory.create_base()
    factory.create_evolved()
    print("Testing Creature with healing capability")
    print("base:")
    print(factory.base.describe())
    print(factory.base.attack())
    print(factory.base.heal())
    print("evolved:")
    print(factory.evolved.describe())
    print(factory.evolved.attack())
    print(factory.evolved.heal())
    print()


def testing_transforms(
        factory: TransformCreatureFactory
        ) -> None:
    factory.create_base()
    factory.create_evolved()
    print("Testing Creature with transform capability")
    print("base:")
    print(factory.base.describe())
    print(factory.base.attack())
    print(factory.base.transform())
    print(factory.base.attack())
    print(factory.base.revert())
    print("evolved:")
    print(factory.evolved.describe())
    print(factory.evolved.attack())
    print(factory.evolved.transform())
    print(factory.evolved.attack())
    print(factory.evolved.revert())
    print()


if __name__ == "__main__":
    health = HealingCreatureFactory()
    testing_healing(health)
    transform = TransformCreatureFactory()
    testing_transforms(transform)
