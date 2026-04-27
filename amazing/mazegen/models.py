from dataclasses import dataclass
from typing import Callable


@dataclass
class Cell:
    bords: str
    i: int
    j: int
    mat_i: int
    mat_j: int
    is_entry = False
    is_exit = False
    is_f2 = False
    is_visited = False


@dataclass
class MazeGenerator:
    cells = list
    width: int
    height: int
    entry: tuple
    exit: tuple
    solution: dict
    anim_func: Callable
