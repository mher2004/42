import functools
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if kwargs.get("power") is None:
                power = args[0]
            else:
                power = kwargs.get("power")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            failed = True
            for i in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... \
(attempt {i}/{max_attempts})")
                else:
                    failed = False
                    break
            if failed:
                result = f"Spell casting failed after {max_attempts} attempts"
            return result
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with <{power}> power"


@spell_timer
def test(n: int) -> int:
    a = 0
    for i in range(n):
        a += 1
    return a


@retry_spell(4)
def test2(n: int) -> int:
    a = 0
    for i in range(n):
        a += 1
    return a


print(test2("asdf"))
print(test2(5))
mag = MageGuild()
print(mag.validate_mage_name("Valod"))
print(mag.validate_mage_name("###"))
print(mag.cast_spell(spell_name="Hagob", power=78))
print(mag.cast_spell(spell_name="Hagob", power=7))
print(test(7))
