from src.model.models import Zone
from src.model.graph import move_cost


def build_timeline(path: list[Zone]) -> list[tuple[int, Zone]]:
    """Returns [(turn, zone), ...] — the turn each zone is entered on,
 skipping the start zone."""
    timeline: list[tuple[int, Zone]] = []
    turn = 1
    for zone in path[1:]:
        timeline.append((turn, zone))
        turn += move_cost(zone)
    return timeline


def format_output(timelines: dict[str, list[tuple[int, Zone]]]) -> list[str]:
    """timelines: {drone_id: [(turn, zone), ...], ...} -> list of output lines\
, one per turn."""
    max_turn = max(turn for tl in timelines.values() for turn, _ in tl)
    lines = []
    for turn in range(1, max_turn + 1):
        moves = [f"D{drone_id}-{zone.name}"
                 for drone_id, tl in timelines.items()
                 for t, zone in tl if t == turn]
        if moves:
            lines.append(" ".join(moves))
    return lines
