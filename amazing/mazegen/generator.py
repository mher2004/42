from collections import deque
from typing import Callable, Any, Dict, Tuple, Optional
import random
import time


class Cell:
    def __init__(self, i: int, j: int) -> None:
        self.bords = "1111"
        self.i = i
        self.j = j
        self.mat_i = i * 3 + 1
        self.mat_j = j * 3 + 1
        self.is_entry = False
        self.is_exit = False
        self.is_f2 = False
        self.is_visited = False


class MazeGenerator:
    def __init__(
            self,
            width: int,
            height: int,
            entry: tuple,
            exit: tuple):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Width and height must be integers")

        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")

        if width < 2 or height < 2:
            raise ValueError("Maze must be at least 2x2")

        if not (isinstance(entry, tuple) and isinstance(exit, tuple)):
            raise TypeError("Entry and exit must be tuples")

        if len(entry) != 2 or len(exit) != 2:
            raise ValueError("Entry and exit must be (x, y)")

        ex, ey = entry
        xx, xy = exit

        if not isinstance(ex, int) or not isinstance(ey, int):
            raise TypeError("Entry must be integers")

        if not isinstance(xx, int) or not isinstance(xy, int):
            raise TypeError("Exit must be integers")

        if not (0 <= ex < width and 0 <= ey < height):
            raise ValueError("Entry is outside maze bounds")

        if not (0 <= xx < width and 0 <= xy < height):
            raise ValueError("Exit is outside maze bounds")
        self.cells = [[Cell(i, j) for j in range(0, width)]
                      for i in range(0, height)]
        self.cells[entry[1]][entry[0]].is_entry = True
        self.cells[exit[1]][exit[0]].is_exit = True
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.solution: Dict[Tuple, Tuple | None] = dict()
        self.anim_func: Optional[Callable] = None

    def set_anim_func(self, anim_func: Callable) -> None:
        """Stes the animation variable"""
        self.anim_func = anim_func

    def gen_f2(self) -> None:
        """Generates the 42 pattern"""
        ns = int((self.height - 5) / 2)
        ws = int((self.width - 5) / 2)
        self.cells[ns][ws].is_f2 = True
        self.cells[ns+1][ws].is_f2 = True
        self.cells[ns+2][ws].is_f2 = True
        self.cells[ns+2][ws+1].is_f2 = True
        self.cells[ns+2][ws+2].is_f2 = True
        self.cells[ns+3][ws+2].is_f2 = True
        self.cells[ns+4][ws+2].is_f2 = True
        self.cells[ns][ws+4].is_f2 = True
        self.cells[ns][ws+5].is_f2 = True
        self.cells[ns][ws+6].is_f2 = True
        self.cells[ns+1][ws+6].is_f2 = True
        self.cells[ns+2][ws+6].is_f2 = True
        self.cells[ns+2][ws+5].is_f2 = True
        self.cells[ns+2][ws+4].is_f2 = True
        self.cells[ns+3][ws+4].is_f2 = True
        self.cells[ns+4][ws+4].is_f2 = True
        self.cells[ns+4][ws+5].is_f2 = True
        self.cells[ns+4][ws+6].is_f2 = True

    def renew(self) -> None:
        """Clears all the information from the matrix to make a new one"""
        for row in self.cells:
            for cell in row:
                cell.bords = "1111"
                cell.is_f2 = False
                cell.is_visited = False

    def berlini_pat(self, i1: int, j1: int, i2: int, j2: int) -> None:
        """This function eliminates the wall between 2 cells"""
        direct = (i2 - i1, j2 - j1)
        directions = {
            (-1, 0): 0,
            (0, 1): 1,
            (1, 0): 2,
            (0, -1): 3
        }
        n = directions[direct]
        first = self.cells[i1][j1].bords
        first = first[:n] + '0' + first[n + 1:]
        n = (n + 2) % 4
        second = self.cells[i2][j2].bords
        second = second[:n] + '0' + second[n + 1:]
        self.cells[i1][j1].bords = first
        self.cells[i2][j2].bords = second

    def solve(self) -> None:
        """Main function for getting a solution"""
        parent: dict[tuple, tuple | None] = dict()
        parent[(self.entry[1], self.entry[0])] = None
        visited = set()
        visited.add((self.entry[1], self.entry[0]))
        cells: Any = deque()
        cells.append((self.entry[1], self.entry[0]))
        leave = True
        while cells and leave:
            current = cells.popleft()
            neighboors = self.solve_neighboors(current[0], current[1])
            for neighboor in neighboors:
                if neighboor.is_exit:
                    parent[(neighboor.i,
                            neighboor.j)] = current
                    leave = False
                    break
                elif (neighboor.i,
                      neighboor.j) not in visited:
                    parent[(neighboor.i,
                            neighboor.j)] = current
                    cells.append((neighboor.i, neighboor.j))
                    visited.add((neighboor.i,
                                 neighboor.j))
        self.solution = parent

    def check_walls(self, i1: int, j1: int, i2: int, j2: int) -> bool:
        """This function tells if 2 cells are accessible or\
        they have a wall between of them"""
        direct = (i2 - i1, j2 - j1)
        directions = {
            (-1, 0): 0,
            (0, 1): 1,
            (1, 0): 2,
            (0, -1): 3
        }
        n = directions[direct]
        firstR = self.cells[i1][j1].bords
        firstE = firstR[:n] + '0' + firstR[n + 1:]
        n = (n + 2) % 4
        secondR = self.cells[i2][j2].bords
        secondE = secondR[:n] + '0' + secondR[n + 1:]
        if firstR != firstE or secondR != secondE:
            return False
        return True

    def solve_neighboors(self, i: int, j: int) -> list[Cell]:
        """Function for getting the neighboor cells where can\
         be accessed from a specified cell"""
        neighboors = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cells = self.cells
        for di, dj in directions:
            if 0 <= di + i < self.height:
                if 0 <= dj + j < self.width:
                    cell = cells[di + i][dj + j]
                    if not cell.is_f2 and self.check_walls(
                        i,
                        j,
                        cell.i,
                        cell.j
                    ):
                        neighboors.append(cell)
        return neighboors

    def get_neighboor(self, i: int, j: int) -> list[Cell]:
        """Function for getting the not visited and not f2 cells\
         around a specified cell"""
        neighboors = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cells = self.cells
        for di, dj in directions:
            if 0 <= di + i < self.height:
                if 0 <= dj + j < self.width:
                    cell = cells[di + i][dj + j]
                    if not (cell.is_f2 or cell.is_visited):
                        neighboors.append(cell)
        return neighboors

    def make_imperfect(self) -> None:
        """Function for making the maze imperfect"""
        entry_cell = self.cells[self.entry[1]][self.entry[0]]
        if entry_cell.bords[0] == "1" and entry_cell.i != 0:
            self.berlini_pat(
                self.entry[1], self.entry[0], self.entry[1] - 1, self.entry[0])
        elif entry_cell.bords[1] == "1" and entry_cell.j != self.width - 1:
            self.berlini_pat(
                self.entry[1], self.entry[0], self.entry[1], self.entry[0] + 1)
        elif entry_cell.bords[2] == "1" and entry_cell.i != self.height - 1:
            self.berlini_pat(
                self.entry[1], self.entry[0], self.entry[1] + 1, self.entry[0])
        elif entry_cell.bords[3] == "1" and entry_cell.j != 0:
            self.berlini_pat(
                self.entry[1], self.entry[0], self.entry[1], self.entry[0] - 1)

    def generator(self, seed: str | None = None, alg: int = 0,
                  perfect: bool = True, is_ft: bool = False,
                  animate: bool = False) -> str | None:
        """The main generator function for the maze"""
        if alg not in range(0, 2):
            print("ERROR ALGO NOT FOUND")
            return None
        self.renew()
        if is_ft:
            self.gen_f2()
        if not seed:
            seed = str(time.time())
        random.seed(seed)
        if alg == 0:
            self.alg1(animate)
        elif alg == 1:
            self.alg2(animate)
        if not perfect:
            self.make_imperfect()
        self.solve()
        return seed

    def alg1(self, animate: bool) -> None:
        """Deep First Search's algorithm for maze generation."""
        stack = [self.cells[self.entry[1]][self.entry[0]]]
        stack[-1].is_visited = True
        while stack:
            neighboors = self.get_neighboor(stack[-1].i, stack[-1].j)
            if neighboors == []:
                stack.pop()
                continue
            else:
                cell = random.choice(neighboors)
                self.berlini_pat(stack[-1].i, stack[-1].j, cell.i, cell.j)
                cell.is_visited = True
                stack.append(cell)
            if animate and self.anim_func:
                print("\033[2J\033[H", end="")
                self.anim_func()
                time.sleep(0.05)

    def alg2(self, animate: bool) -> None:
        """Randomized Prim's algorithm for maze generation."""
        start = self.cells[self.entry[1]][self.entry[0]]
        start.is_visited = True
        frontier = self.get_neighboor(start.i, start.j)
        while frontier:
            cell = random.choice(frontier)
            frontier.remove(cell)
            visited_neighbors = []
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = cell.i + di, cell.j + dj
                if 0 <= ni < self.height and 0 <= nj < self.width:
                    neighbor = self.cells[ni][nj]
                    if neighbor.is_visited and not neighbor.is_f2:
                        visited_neighbors.append(neighbor)

            if visited_neighbors:
                chosen = random.choice(visited_neighbors)
                self.berlini_pat(chosen.i, chosen.j, cell.i, cell.j)
                cell.is_visited = True

                if animate and self.anim_func:
                    print("\033[2J\033[H", end="")
                    self.anim_func()
                    time.sleep(0.05)

                for new in self.get_neighboor(cell.i, cell.j):
                    if new not in frontier:
                        frontier.append(new)
