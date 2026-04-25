from dataclasses import dataclass


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
    is_path = False
