from dataclasses import dataclass
from rich import print


@dataclass
class ZoneSpec:
    name: str
    x: int
    y: int
    zone_type: str = "normal"
    color: str | None = None
    max_drones: int = 1


@dataclass
class ConnSpec:
    name1: str
    name2: str
    max_link_capacity: int = 1


def zone_maker(specs: str) -> ZoneSpec:
    if len(specs.split()) < 3:
        raise ValueError("Wrong hub data insertion format")
    name = specs.split()[0]
    x = int(specs.split()[1])
    y = int(specs.split()[2])
    zone = "normal"
    max_drones = 1
    color = None
    if len(specs.split()) >= 4:
        other = specs.split()[3:]
        if other[0][0] != "[" or other[-1][-1] != "]":
            raise ValueError("Wrong hub data insertion format")
        other[0] = other[0][1:]
        other[-1] = other[-1][:-1]
        for i in other:
            if len(i) == 0:
                pass
            if "color" in i:
                color = i.split("=")[1]
            elif "zone" in i:
                zone = i.split("=")[1]
            elif "max_drones" in i:
                max_drones = i.split("=")[1]
            else:
                raise ValueError("Wrong format for option list")

    obj = ZoneSpec(name, x, y, zone, color, max_drones)
    return obj


def connection_maker(specs: str) -> ConnSpec:
    if len(specs.split()) not in (1, 2):
        raise ValueError("Wrong connection data insertion format")
    if len(specs.split()[0]) < 3 or len(specs.split()[0].split("-")) != 2:
        raise ValueError("Wrong connection data insertion format")
    names = specs.split()[0].split("-")
    other = 1
    if len(specs.split()) == 2:
        if specs.split()[-1][0] != "[" or specs.split()[-1][-1] != "]":
            raise ValueError("Wrong connection data insertion format")
        if len(specs.split()[-1][1:-1].split("=")) != 2:
            raise ValueError("Wrong connection data insertion format")
        other = int(specs.split()[-1][1:-1].split("=")[1])

    obj = ConnSpec(names[0], names[1], other)
    return obj


def parse_metadata(raw: str) -> dict[str, str]:
    """Parses '[zone=priority color=green max_drones=2]' -> dict."""
    metadata = {
        "nb_drones": 0,
        "start_hub": 0,
        "end_hub": 0,
        "hub": [],
        "connection": [],
        "error": 0
    }
    raw_lines = raw.splitlines()

    try:
        if len(raw_lines) < 5:
            raise ValueError("Not enough information for the graph")
        if raw_lines[0][:len("nb_drones:")] != "nb_drones:":
            raise ValueError("Error of nb_drones data input format")
        else:
            metadata["nb_drones"] = int(raw_lines[0][len("nb_drones:"):])
        if raw_lines[1][:len("start_hub:")] != "start_hub:":
            raise ValueError("Error of start_hub data input format")
        else:
            metadata["start_hub"] = zone_maker(raw_lines[1].split(":")[1])
        if raw_lines[2][:len("end_hub:")] != "end_hub:":
            raise ValueError("Error of end_hub data input format")
        else:
            metadata["end_hub"] = zone_maker(raw_lines[2].split(":")[1])
        for i in raw_lines[3:]:
            if i[:len("hub:")] == "hub:":
                metadata["hub"].append(zone_maker(i[len("hub:"):]))
            elif i[:len("connection:")] == "connection:":
                metadata["connection"].append(
                    connection_maker(i[len("connection:"):])
                    )
            else:
                raise ValueError("Wrong data input format")
    except ValueError as error:
        print(error)
        metadata["error"] = 1
    return metadata


print(parse_metadata('''nb_drones: 5
start_hub: hub 0 0 [color=green]
end_hub: goal 10 10 [color=yellow]
hub: roof1 3 4 [zone=restricted color=red]
hub: roof2 6 2 [zone=normal color=blue]
hub: corridorA 4 3 [zone=priority color=green max_drones=2]
hub: tunnelB 7 4 [zone=normal color=red]
hub: obstacleX 5 5 [zone=blocked color=gray]
connection: hub-roof1
connection: hub-corridorA
connection: roof1-roof2
connection: roof2-goal
connection: corridorA-tunnelB [max_link_capacity=2]
connection: tunnelB-goal
'''))
