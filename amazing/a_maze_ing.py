import parceing
from errors import ConfigFormatError
from generator import MazeGenerator


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
        # self.render_matrix(config)
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


def menu(config, maze, gen) -> None:
    while True:
        maze.print_mat(config)
        print("Select one of the options:")
        print("1 - regenerate a new maze and display it")
        print("2 - show/hide a valid shortest path from entry to the exit")
        print("3 - change maze wall Color")
        print("4 - Exit")
        try:
            option = int(input("Enter option:"))
            if not (option >= 1 and option <= 4):
                raise ValueError()
            if option == 1:
                print("1")
                gen.generate(True)
                maze.render_matrix(config)
            elif option == 2:
                print("2")
            elif option == 3:
                print("3")
                print("Choose from: yellow, blue, white")
                config.Color = input("Input new Color:")
            elif option == 4:
                break
        except (TypeError, ValueError):
            print("Wrong option type! Input a number from [1; 3]!")
        except ConfigFormatError as e:
            print(e)


def main() -> None:
    try:
        config = parceing.parce()
        # print(config)
        if not config:
            return
        maze = Maze(config.width, config.height, config)
        gen = MazeGenerator(config, maze, 42)
        gen.generate()
        maze.render_matrix(config)
        menu(config, maze, gen)
        # print([[[cell.i, cell.j]for cell in row] for row in maze.cells])
    except Exception as e:
        print("Unknown error:", e)


if __name__ == "__main__":
    main()
