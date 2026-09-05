from src.model.models import ParsedMap, Graph


def build_graph(parsed: ParsedMap) -> Graph:
    assert parsed.start_hub is not None and parsed.end_hub is not None
    graph = Graph()
    for spec in [parsed.start_hub, parsed.end_hub, *parsed.hub]:
        graph.add_zone(spec)
    for spec in parsed.connection:
        graph.add_connection(spec)
    return graph