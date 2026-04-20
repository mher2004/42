from errors import ConfigFormatError

import random


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


class Maze:
    def __init__(self, width: int, height: int, config) -> None:
        self.cells = [[Cell(i, j) for j in range(0, width)]
                      for i in range(0, height)]
        self.cells[config.entry[1]][config.entry[0]].is_entry = True
        self.cells[config.exit[1]][config.exit[0]].is_exit = True
        self.width = width
        self.height = height
        self.mat_width = width * 3
        self.mat_height = height * 3
        self.entry_col = 31
        self.exit_col = 32
        self.render_matrix(config)
        if self.width >= 9 and self.height >= 7:
            self.gen_f2()
        else:
            print("Maze size is not sufficent for 42 pattern!")

    def gen_f2(self) -> None:
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

    def render_matrix(self, config) -> None:
        print(config)
        border_symb = f"\033[{config.Color.value}m█\033[0m"
        entry_symb = f"\033[{self.entry_col}m█\033[0m"
        exit_symb = f"\033[{self.exit_col}m█\033[0m"
        self.matrix = [[border_symb for j in range(0, self.width * 3)]
                       for i in range(0, self.height * 3)]
        # self.print_mat()
        for row in self.cells:
            for cell in row:
                if cell.is_entry:
                    self.matrix[cell.mat_i][cell.mat_j] = entry_symb
                elif cell.is_exit:
                    self.matrix[cell.mat_i][cell.mat_j] = exit_symb
                else:
                    self.matrix[cell.mat_i][cell.mat_j] = " "
                bords = cell.bords
                if bords[0] == '0':
                    self.matrix[cell.mat_i - 1][cell.mat_j] = " "
                if bords[1] == '0':
                    self.matrix[cell.mat_i][cell.mat_j + 1] = " "
                if bords[2] == '0':
                    self.matrix[cell.mat_i + 1][cell.mat_j] = " "
                if bords[3] == '0':
                    self.matrix[cell.mat_i][cell.mat_j - 1] = " "
        for row in self.cells:
            for cell in row:
                if cell.is_f2:
                    if cell.is_entry:
                        raise ConfigFormatError("ENTRY overlap with 42 patern")
                    elif cell.is_exit:
                        raise ConfigFormatError("EXIT overlap with 42 pattern")
                    self.matrix[cell.mat_i][cell.mat_j] = border_symb

    def print_cells(self) -> None:
        for row in self.cells:
            for cell in row:
                print(f"[{cell.i},{cell.j}]", end=" ")
            print()

    def print_mat(self, config) -> None:
        self.render_matrix(config)
        for row in self.matrix:
            for symb in row:
                print(symb, end="")
            print()


class MazeGenerator:
    def __init__(
        self,
        config,
        maze: Maze,
            seed: int) -> None:
        self.config = config
        self.maze = maze
        self.seed = seed

    def get_neighboor(self, i: int, j: int) -> list[Cell]:
        neighboors = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cells = self.maze.cells
        for di, dj in directions:
            if 0 <= di + i < self.maze.height:
                if 0 <= dj + j < self.maze.width:
                    cell = cells[di + i][dj + j]
                    if not (cell.is_f2 or cell.is_visited):
                        neighboors.append(cell)
        return neighboors

    def renew(self) -> None:
        for row in self.maze.cells:
            for cell in row:
                cell.is_visited = False

    def generate(self, new: bool = False) -> None:
        if not new:
            random.seed(self.seed)
        self.maze.cells = [
            [Cell(i, j) for j in range(
                0,
                self.maze.width)] for i in range(0, self.maze.height)]
        self.maze.cells[
            self.config.entry[1]][self.config.entry[0]].is_entry = True
        self.maze.cells[
            self.config.exit[1]][self.config.exit[0]].is_exit = True
        if self.maze.width >= 9 and self.maze.height >= 7:
            self.maze.gen_f2()
        self.renew()
        stack = [
            self.maze.cells[self.config.entry[1]][self.config.entry[0]]]
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

    def berlini_pat(self, i1: int, j1: int, i2: int, j2: int) -> None:
        direct = (i2 - i1, j2 - j1)
        directions = {
            (-1, 0): 0,
            (1, 0): 2,
            (0, 1): 1,
            (0, -1): 3
        }
        n = directions[direct]
        first = self.maze.cells[i1][j1].bords
        first = first[:n] + '0' + first[n + 1:]
        n = (n + 2) % 4
        second = self.maze.cells[i2][j2].bords
        second = second[:n] + '0' + second[n + 1:]
        self.maze.cells[i1][j1].bords = first
        self.maze.cells[i2][j2].bords = second
