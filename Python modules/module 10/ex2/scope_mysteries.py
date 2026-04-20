from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    a = 0

    def counter() -> int:
        nonlocal a
        a += 1
        return a
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def accumulator(power: int) -> int:
        nonlocal total
        total += power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def desc(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return desc


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


cont = mage_counter()
cont2 = mage_counter()
print(cont(), cont())
print(cont2(), cont2())
acc = spell_accumulator(20)
acc2 = spell_accumulator(20)
print(acc(15), acc(14))
print(acc2(15), acc2(14))
fac1 = enchantment_factory("fac1")
fac2 = enchantment_factory("fac2")
print(fac1("1234"), fac1("87654"))
print(fac2("uhbv"), fac2("jhgfd"))
store = memory_vault()
store["store"]("name", 123)
store["store"]("name2", 111)
print(store["recall"](123), store["recall"]("name2"))
print(store)
