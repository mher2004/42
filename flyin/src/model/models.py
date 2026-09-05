from dataclasses import dataclass, field


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


@dataclass
class ParsedMap:
    nb_drones: int = 0
    start_hub: ZoneSpec | None = None
    end_hub: ZoneSpec | None = None
    hub: list[ZoneSpec] = field(default_factory=list)
    connection: list[ConnSpec] = field(default_factory=list)
    error: int = 0


class Zone:
    def __init__(self, spec: ZoneSpec):
        self.name = spec.name
        self.x = spec.x
        self.y = spec.y
        self.zone_type = spec.zone_type
        self.max_drones = spec.max_drones
        self.connections: list["Connection"] = []
        self.occupants: set[str] = set()

    def has_space(self) -> bool:
        return len(self.occupants) < self.max_drones

    def __repr__(self) -> str:
        return f"Zone({self.name!r}, type={self.zone_type})"


class Connection:
    def __init__(self, zone_a: Zone, zone_b: Zone, max_link_capacity: int):
        self.zone_a = zone_a
        self.zone_b = zone_b
        self.max_link_capacity = max_link_capacity
        self.in_transit: set[str] = set()

    def other(self, zone: Zone) -> Zone:
        return self.zone_b if zone is self.zone_a else self.zone_a
    
    def __repr__(self) -> str:
        return f"Connection({self.zone_a.name}-{self.zone_b.name}, cap={self.max_link_capacity})"


class Graph:
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}
        self.connections: list[Connection] = []

    def add_zone(self, spec: ZoneSpec) -> Zone:
        zone = Zone(spec)
        self.zones[zone.name] = zone
        return zone

    def add_connection(self, spec: ConnSpec) -> Connection:
        conn = Connection(self.zones[spec.name1], self.zones[spec.name2], spec.max_link_capacity)
        self.connections.append(conn)
        conn.zone_a.connections.append(conn)
        conn.zone_b.connections.append(conn)
        return conn