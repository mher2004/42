import parceing
from errors import ConfigFormatError
from generator import MazeGenerator
from math import ceil, floor
import sys


class Render:
    def __init__(
            self,
            config: parceing.Config,
            cells: list,
            solution: dict):
        self.config = config
        self.entry_col = 32
        self.exit_col = 31
        self.cells = cells
        self.set_sol(solution)
        self.show_path = False

    def set_sol(self, solution: dict) -> None:
        self.solution = solution

    def switch_show_path(self) -> None:
        self.show_path = not self.show_path

    def render_matrix(self) -> None:
        border_symb = f"\033\
[{self.config.color.value}m█\033[0m"
        entry_symb = f"\033[{self.entry_col}m█\033[0m"
        exit_symb = f"\033[{self.exit_col}m█\033[0m"
        f2 = f"\033[{36}m█\033[0m"
        path = f"\033[{33}m█\033[0m"
        self.matrix = [[border_symb for j in range(0, self.config.width * 3)]
                       for i in range(0, self.config.height * 3)]
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
                    bords = cell.bords
                    self.matrix[cell.mat_i - 1][cell.mat_j] = f2
                    self.matrix[cell.mat_i - 1][cell.mat_j - 1] = f2
                    self.matrix[cell.mat_i - 1][cell.mat_j + 1] = f2
                    self.matrix[cell.mat_i][cell.mat_j + 1] = f2
                    self.matrix[cell.mat_i - 1][cell.mat_j + 1] = f2
                    self.matrix[cell.mat_i + 1][cell.mat_j + 1] = f2
                    self.matrix[cell.mat_i + 1][cell.mat_j] = f2
                    self.matrix[cell.mat_i][cell.mat_j - 1] = f2
                    self.matrix[cell.mat_i - 1][cell.mat_j - 1] = f2
                    self.matrix[cell.mat_i + 1][cell.mat_j - 1] = f2
                    self.matrix[cell.mat_i][cell.mat_j] = f2
            current = (self.config.exit[1], self.config.exit[0])
            while current and self.show_path:
                ci, cj = current
                if self.solution[current] is None:
                    break

                pi, pj = self.solution[current]
                ci_mat = ci * 3 + 1
                cj_mat = cj * 3 + 1
                step = ((pi - ci) * 3, (pj - cj) * 3)
                cell = self.cells[ci][cj]

                if cell.is_entry:
                    self.matrix[ci_mat][cj_mat] = path
                    current = self.solution[current]
                    continue

                if not cell.is_exit:
                    self.matrix[ci_mat][cj_mat] = path

                self.matrix[
                    ci_mat + floor(step[0] / 2)
                ][cj_mat + floor(step[1] / 2)] = path

                self.matrix[
                    ci_mat + ceil(step[0] / 2)
                ][cj_mat + ceil(step[1] / 2)] = path

                current = self.solution[current]

    def print_mat(self) -> None:
        self.render_matrix()
        for row in self.matrix:
            for symb in row:
                print(symb, end="")
            print()


class Output:
    @classmethod
    def write_file(
            cls,
            maze: list,
            entry: tuple,
            exit: tuple,
            solution: dict,
            output_file: str) -> None:
        with open(output_file, "w") as f:
            f.write(cls.gen_otput(maze, entry, exit, solution))

    @classmethod
    def gen_otput(
            cls,
            maze: list,
            entry: tuple,
            exit: tuple,
            solution: dict) -> str:
        res = str()
        for row in maze:
            for cell in row:
                res += hex(int(cell.bords, 2))[-1].upper()
            res += "\n"
        res += "\n"
        res += f"{entry[0]},{entry[1]}\n"
        res += f"{exit[0]},{exit[1]}\n"
        res += cls.gen_sol_str(solution)
        res += "\n"
        return res

    @classmethod
    def gen_sol_str(cls, solution: dict) -> str:
        res = str()
        seq = list()
        curr = list(solution.keys())[-1]
        while curr:
            seq.append(curr)
            curr = solution[curr]
        seq.reverse()
        for i in range(1, len(seq)):
            if seq[i-1][0] > seq[i][0]:
                res += "N"
            elif seq[i-1][0] < seq[i][0]:
                res += "S"
            elif seq[i-1][1] < seq[i][1]:
                res += "E"
            elif seq[i-1][1] > seq[i][1]:
                res += "W"
        return res


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
        self.is_path = False


def clear_screen() -> None:
    print("\033[2J\033[H", end="")


def menu(config: parceing.Config) -> None:
    alg = 0
    gen = MazeGenerator(config.width, config.height, config.entry, config.exit)
    gen.generator(config.seed, is_ft=config.is_ft,
                  perfect=config.perfect, alg=alg)
    ren = Render(config, gen.cells, gen.solution)
    gen.set_anim_func(ren.print_mat)
    Output.write_file(gen.cells, config.entry, config.exit,
                      gen.solution, config.output_file)
    prev_msg = str()
    if not config.is_ft:
        prev_msg = "Maze is not big enough to fit 42 pattern"
    while True:
        clear_screen()
        ren.print_mat()
        if prev_msg:
            print(f"!!!!! {prev_msg} !!!!!\n", end="")
        prev_msg = str()
        print("Select one of the options:")
        print("1 - regenerate a gen maze and display it")
        print("2 - show/hide a valid shortest path from entry to the exit")
        print("3 - change maze wall color")
        print("4 - animate current generation")
        print("5 - Change algorithm (DFS/Randomized Prim's)")
        print("6 - Exit")
        try:
            option = int(input("Enter option:"))
            if not (option >= 1 and option <= 6):
                raise ValueError()
            if option == 1:
                config.seed = gen.generator(
                    is_ft=config.is_ft, perfect=config.perfect, alg=alg)
                ren.set_sol(gen.solution)
                Output.write_file(gen.cells, config.entry,
                                  config.exit, gen.solution,
                                  config.output_file)
            elif option == 2:
                ren.switch_show_path()
            elif option == 3:
                print("Choose from: yellow, blue, white")
                config.color = input("Input new Color:")
            elif option == 4:
                gen.generator(config.seed, is_ft=config.is_ft,
                              perfect=config.perfect, animate=True, alg=alg)
            elif option == 5:
                alg = not alg
                print(alg)
            elif option == 6:
                break
        except (TypeError, ValueError):
            prev_msg = "Wrong option type! Input a number from [1; 5]!"
        except ConfigFormatError as e:
            print(e)


def main() -> None:
    argv = sys.argv
    if len(argv) != 2:
        print("Invalid atgv! Should be: python3 a_maze_ing.py <configfile>")
        return
    config_file = argv[1]
    try:
        config = parceing.parce(config_file)
        if not config:
            return
        menu(config)
    except ConfigFormatError as e:
        print(e)
    except Exception as e:
        print(f"UnknownError:{e}")


if __name__ == "__main__":
    main()
