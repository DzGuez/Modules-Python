#!/usr/bin/env python3

from ex1 import TransformCreatureFactory, HealingCreatureFactory


def test_healing(factory_heal: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base = factory_heal.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    evolved = factory_heal.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print()


def test_transform(factory_trans: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")

    print(" base:")
    base = factory_trans.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    evolved = factory_trans.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
    print()


def main() -> None:
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()

    test_healing(heal_factory)
    test_transform(trans_factory)


if __name__ == "__main__":
    main()
