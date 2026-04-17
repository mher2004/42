import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in operations.keys():
        raise ValueError
    if spells == []:
        return 0
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    funcs = {
        "one": functools.partial(base_enchantment, 50, "onee"),
        "two": functools.partial(base_enchantment, 50, "twoo"),
        "three": functools.partial(base_enchantment, 50, "threeee"),
    }
    return funcs


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def spell(arg: Any) -> str:
        return "Unknown type"

    @spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg}"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {arg}"
    return spell


cast = spell_dispatcher()
print(memoized_fibonacci(0), memoized_fibonacci(1), memoized_fibonacci(10))
print(cast(50))
print(cast("Invisibility"))
print(cast([10, "Heal"]))
print(cast(3.14))
