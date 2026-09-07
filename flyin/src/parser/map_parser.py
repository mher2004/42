from rich import print
from src.model.models import ZoneSpec, ConnSpec, ParsedMap
from src.model.graph import build_graph


def parse_positive_int(raw: str, field_name: str) -> int:
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"{field_name} must be an integer, got {raw!r}")
    if value <= 0:
        raise ValueError(f"{field_name} must be positive, got {value}")
    return value


def zone_maker(specs: str) -> ZoneSpec:
    VALID_ZONE_TYPES = {"normal", "blocked", "restricted", "priority"}
    if len(specs.split()) < 3:
        raise ValueError("Wrong hub data insertion format")
    name = specs.split()[0]
    if "-" in name:
        raise ValueError(f"Zone name '{name}' must not contain dashes")
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
            if not i:
                continue
            if "color" in i:
                color = i.split("=")[1]
            elif "zone" in i:
                zone = i.split("=")[1]
            elif "max_drones" in i:
                max_drones = parse_positive_int(i.split("=")[1], "max_drones")
            else:
                raise ValueError("Wrong format for option list")

    if zone not in VALID_ZONE_TYPES:
        raise ValueError(f"Invalid zone type: {zone!r}")

    obj = ZoneSpec(name, x, y, zone, color, max_drones)

    return obj


def connection_maker(specs: str) -> ConnSpec:
    if len(specs.split()) not in (1, 2):
        raise ValueError("Wrong connection data insertion format")
    if len(specs.split()[0]) < 3 or len(specs.split()[0].split("-")) != 2:
        raise ValueError("Wrong connection data insertion format")
    names = specs.split()[0].split("-")
    if names[0] == names[1]:
        raise ValueError("Wrong connection data insertion same name")
    other = 1
    if len(specs.split()) == 2:
        if specs.split()[-1][0] != "[" or specs.split()[-1][-1] != "]":
            raise ValueError("Wrong connection data insertion format")
        if len(specs.split()[-1][1:-1].split("=")) != 2:
            raise ValueError("Wrong connection data insertion format")
        if specs.split()[-1][1:-1].split("=")[0] != "max_link_capacity":
            raise ValueError("Wrong connection data insertion format")
        other = parse_positive_int(
            specs.split()[-1][1:-1].split("=")[1],
            "max_link_capacity")

    obj = ConnSpec(names[0], names[1], other)
    return obj


def validate_structure(metadata: ParsedMap) -> None:
    all_zones = [metadata.start_hub, metadata.end_hub, *metadata.hub]
    names = [z.name for z in all_zones]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate zone name detected")

    zone_names = set(names)
    seen_edges: set[frozenset[str]] = set()
    for conn in metadata.connection:
        if conn.name1 not in zone_names or conn.name2 not in zone_names:
            raise ValueError(f"Connection references unknown zone:\
 {conn.name1}-{conn.name2}")
        edge = frozenset({conn.name1, conn.name2})
        if edge in seen_edges:
            raise ValueError(f"Duplicate connection:\
 {conn.name1}-{conn.name2}")
        seen_edges.add(edge)


def parse_metadata(raw: str) -> ParsedMap:
    """Parses '[zone=priority color=green max_drones=2]' -> dict."""
    metadata = ParsedMap()
    raw_lines = raw.splitlines()
    raw_lines = [
        (i, raw_lines[i - 1]) for i in range(1, len(raw_lines) + 1)
    ]
    raw_lines = [
        i for i in raw_lines if i[1].strip() and not i[1].strip().startswith(
            "#")
        ]

    try:
        if len(raw_lines) < 5:
            raise ValueError("Not enough information for the graph")
        if raw_lines[0][1][:len("nb_drones:")] != "nb_drones:":
            raise ValueError(f"Line {raw_lines[0][0]}: \
Error of nb_drones data input format")
        else:
            metadata.nb_drones = parse_positive_int(
                raw_lines[0][1][len("nb_drones:"):], "nb_drones")
        if raw_lines[1][1][:len("start_hub:")] != "start_hub:":
            raise ValueError(f"Line {raw_lines[1][0]}: \
Error of start_hub data input format")
        else:
            try:
                metadata.start_hub = zone_maker(
                    raw_lines[1][1].split(":")[1])
            except ValueError as err:
                raise ValueError(f"Line {raw_lines[1][0]}: {err}") from err
        if raw_lines[2][1][:len("end_hub:")] != "end_hub:":
            raise ValueError(f"Line {raw_lines[2][0]}: \
Error of end_hub data input format")
        else:
            try:
                metadata.end_hub = zone_maker(raw_lines[2][1].split(":")[1])
            except ValueError as err:
                raise ValueError(f"Line {raw_lines[2][0]}: {err}") from err
        for i in raw_lines[3:]:
            if i[1][:len("hub:")] == "hub:":
                try:
                    metadata.hub.append(zone_maker(i[1][len("hub:"):]))
                except ValueError as err:
                    raise ValueError(f"Line {i[0]}: {err}") from err
            elif i[1][:len("connection:")] == "connection:":
                try:
                    metadata.connection.append(
                        connection_maker(i[1][len("connection:"):])
                        )
                except ValueError as err:
                    raise ValueError(f"Line {i[0]}: {err}") from err
            else:
                raise ValueError(f"Line {i[0]}: Wrong data input format")
        validate_structure(metadata)
    except ValueError as error:
        print(error)
        metadata.error = 1
    return metadata


aaa = parse_metadata('''nb_drones: 5
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
''')

test = build_graph(aaa)

print(test.zones["hub"].connections[0].other(test.zones["hub"]))

# print(build_graph(aaa).zones, build_graph(aaa).connections)
