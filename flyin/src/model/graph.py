from src.model.models import ParsedMap, Graph, Zone
import heapq


def build_graph(parsed: ParsedMap) -> Graph:
    assert parsed.start_hub is not None and parsed.end_hub is not None
    graph = Graph()
    for spec in [parsed.start_hub, parsed.end_hub, *parsed.hub]:
        graph.add_zone(spec)
    for spec in parsed.connection:
        graph.add_connection(spec)
    return graph


def move_cost(zone: Zone) -> int:
    return 2 if zone.zone_type == "restricted" else 1


def shortest_path(start: Zone, end: Zone, graph: Graph) -> list[Zone] | None:
    queue: list[tuple[int, str]] = [(0, start.name)]
    current_dist, current_name = heapq.heappop(queue)
    distances: dict[str, int] = {
        zone_name: float("inf") for zone_name in graph.zones}
    distances[start.name] = 0

    came_from: dict[str, str | None] = {
        zone_name: None for zone_name in graph.zones}
    came_from[start.name] = None

