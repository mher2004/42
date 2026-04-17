def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda k: k["power"],
        reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell:  "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    return {
        'max_power': max(mages, key=lambda x: x["power"])['power'],
        'min_power': min(mages, key=lambda x: x["power"])['power'],
        'avg_power': round(
            sum(map(lambda m: m['power'], mages)) / len(mages), 2)
        }


a = [{'name': "str", 'power': 7, 'tpe': 'str'},
     {'name': "str", 'power': 1, 'tpe': 'str'},
     {'name': "str", 'power': 8, 'tpe': 'str'},
     {'name': "str", 'power': 155, 'tye': 'str'}]

print(artifact_sorter(a))
print(power_filter(a, 7))
print(spell_transformer(["1234", "1fds"]))
print(mage_stats(a))
