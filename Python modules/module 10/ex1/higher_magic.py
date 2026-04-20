from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def heal2(target: str, power: int) -> str:
    return f"Heal2 restores {target} for {power} HP"


def spell_combiner(
        spell1: Callable, spell2: Callable
        ) -> Callable:
    if not (callable(spell1) and callable(spell2)):
        raise TypeError
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError
    return lambda t, p: base_spell(t, p * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not (callable(condition) and callable(spell)):
        raise TypeError
    return lambda t, p: spell(t, p) if condition(t, p) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    for i in spells:
        if not callable(i):
            raise TypeError
    return lambda t, p: [spell(t, p) for spell in spells]


print(spell_combiner(heal, heal2)("qwe", 88))
print(power_amplifier(heal, 8)("qwe", 88))
print(conditional_caster(lambda t, p: p > 5, heal2)("qwe", 88))
print(spell_sequence([heal, heal2])("qwe", 88))
