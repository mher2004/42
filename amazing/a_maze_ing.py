import parceing
from errors import ConfigFormatError
from mazegen import MazeGenerator
from math import ceil, floor
import sys


class Render:
    """Handles all rendering logic for displaying the maze in the terminal.

    Converts the internal cell grid into a coloured block-character matrix
    and prints it to stdout. Optionally overlays the solved path and any
    special '42' pattern cells.

    Attributes:
        config (parceing.Config): The parsed configuration object.
        entry_col (int): ANSI colour code used to render the entry cell.
        exit_col (int): ANSI colour code used to render the exit cell.
        cells (list): 2-D list of Cell objects that make up the maze.
        solution (dict): BFS parent-map from the solver, mapping each cell
            coordinate to its predecessor on the shortest path.
        show_path (bool): Whether to overlay the solution path on the render.
    """

    def __init__(
            self,
            config: parceing.Config,
            cells: list,
            solution: dict):
        """Initialise the renderer with maze data.

        Args:
            config (parceing.Config): Parsed configuration containing
                dimensions, colours, entry/exit positions, etc.
            cells (list): 2-D list of Cell objects representing the maze grid.
            solution (dict): BFS parent-map returned by MazeGenerator.solve().
        """
        self.config = config
        self.entry_col = 32
        self.exit_col = 31
        self.cells = cells
        self.set_sol(solution)
        self.show_path = False

    def set_sol(self, solution: dict) -> None:
        """Replace the current solution with a new one.

        Called after the maze is regenerated so the renderer always holds
        the solution that corresponds to the currently displayed maze.

        Args:
            solution (dict): New BFS parent-map to store.
        """
        self.solution = solution

    def switch_show_path(self) -> None:
        """Toggle the visibility of the solution path overlay.

        Each call flips ``show_path`` between ``True`` and ``False``.
        The change takes effect on the next call to :meth:`print_mat`.
        """
        self.show_path = not self.show_path

    def render_matrix(self) -> None:
        """Build the display matrix from the current cell grid.

        Populates ``self.matrix`` — a 2-D list of coloured block characters
        (``█``) or spaces — by:

        1. Filling every position with the wall colour block.
        2. Carving open passages according to each cell's border flags.
        3. Marking entry and exit cells with their distinct colours.
        4. Overlaying any '42'-pattern cells with their own colour.
        5. If ``show_path`` is ``True``, tracing the BFS solution from the
           exit back to the entry and marking each step.

        Raises:
            ConfigFormatError: If a '42'-pattern cell overlaps with the
                entry or exit cell.
        """
        if isinstance(self.config.color, parceing.Color):
            border_symb = f"\033[{self.config.color.value}m█\033[0m"
        entry_symb = f"\033[{self.entry_col}m█\033[0m"
        exit_symb = f"\033[{self.exit_col}m█\033[0m"
        f2 = f"\033[{36}m█\033[0m"
        path = f"\033[{35}m█\033[0m"
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
        """Render and print the maze to stdout.

        Calls :meth:`render_matrix` to rebuild the display matrix and then
        iterates over every row, printing each symbol without a separating
        space, followed by a newline at the end of each row.
        """
        self.render_matrix()
        for row in self.matrix:
            for symb in row:
                print(symb, end="")
            print()


class Output:
    """Utility class for serialising maze data to a file.

    All methods are class methods; the class is never instantiated directly.
    The file format encodes walls as hexadecimal digits, followed by the
    entry/exit coordinates and the textual step-by-step solution.
    """

    @classmethod
    def write_file(
            cls,
            maze: list,
            entry: tuple,
            exit: tuple,
            solution: dict,
            output_file: str) -> None:
        """Serialise the maze and write it to a file on disk.

        Args:
            maze (list): 2-D list of Cell objects representing the maze grid.
            entry (tuple): ``(col, row)`` coordinates of the entry cell.
            exit (tuple): ``(col, row)`` coordinates of the exit cell.
            solution (dict): BFS parent-map produced by
                :meth:`MazeGenerator.solve`.
            output_file (str): Destination file path.
        """
        with open(output_file, "w") as f:
            f.write(cls.gen_otput(maze, entry, exit, solution))

    @classmethod
    def gen_otput(
            cls,
            maze: list,
            entry: tuple,
            exit: tuple,
            solution: dict) -> str:
        """Build the full serialised string representation of the maze.

        Each cell's four border flags (North, East, South, West) are packed
        into a 4-bit value and written as an uppercase hex digit.  Rows are
        separated by newlines.  After the grid the entry coordinates, exit
        coordinates, and solution string are appended.

        Args:
            maze (list): 2-D list of Cell objects.
            entry (tuple): ``(col, row)`` coordinates of the entry cell.
            exit (tuple): ``(col, row)`` coordinates of the exit cell.
            solution (dict): BFS parent-map produced by
                :meth:`MazeGenerator.solve`.

        Returns:
            str: The complete serialised maze string ready to be written to
                a file.
        """
        res = str()
        for row in maze:
            for cell in row:
                val = 0
                if cell.bords[3] == "1":
                    val += 8
                if cell.bords[2] == "1":
                    val += 4
                if cell.bords[1] == "1":
                    val += 2
                if cell.bords[0] == "1":
                    val += 1
                res += hex(val)[-1].upper()
            res += "\n"
        res += "\n"
        res += f"{entry[0]},{entry[1]}\n"
        res += f"{exit[0]},{exit[1]}\n"
        res += cls.gen_sol_str(solution)
        res += "\n"
        return res

    @classmethod
    def gen_sol_str(cls, solution: dict) -> str:
        """Convert the BFS parent-map into a cardinal-direction string.

        Traces the path from entry to exit using the parent-map, then
        encodes each step as a single character: ``N`` (north / up),
        ``S`` (south / down), ``E`` (east / right), or ``W`` (west / left).

        Args:
            solution (dict): BFS parent-map where each key is a
                ``(row, col)`` tuple and the value is its predecessor
                (or ``None`` for the entry cell).

        Returns:
            str: Sequence of direction characters describing the shortest
                path from entry to exit (e.g. ``"NESSWN"``).
        """
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


def clear_screen() -> None:
    """Clear the terminal screen using ANSI escape codes.

    Sends the ``\\033[2J`` (erase display) and ``\\033[H`` (move cursor to
    home) escape sequences so the next render overwrites the previous one
    in place rather than scrolling.
    """
    print("\033[2J\033[H", end="")


def menu(config: parceing.Config) -> None:
    """Run the interactive menu loop for the maze application.

    Generates an initial maze, writes it to the configured output file,
    and then repeatedly presents a numbered menu to the user until they
    choose to exit.  Available options are:

    1. Regenerate the maze with a new random seed.
    2. Toggle the shortest-path overlay.
    3. Change the wall colour.
    4. Animate the current generation algorithm step-by-step.
    5. Switch between the DFS and Randomised Prim's algorithms and
       regenerate.
    6. Exit the application.

    Args:
        config (parceing.Config): Fully parsed configuration object
            containing maze dimensions, entry/exit positions, colour
            preference, output file path, and generation flags.
    """
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
                if ren.show_path:
                    ren.switch_show_path()
                gen.generator(config.seed, is_ft=config.is_ft,
                              perfect=config.perfect, animate=True, alg=alg)
            elif option == 5:
                alg = not alg
                config.seed = gen.generator(
                    is_ft=config.is_ft, perfect=config.perfect, alg=alg)
                ren.set_sol(gen.solution)
                Output.write_file(gen.cells, config.entry,
                                  config.exit, gen.solution,
                                  config.output_file)
            elif option == 6:
                break
        except (TypeError, ValueError):
            prev_msg = "Wrong option type! Input a number from [1; 5]!"
        except ConfigFormatError as e:
            print(e)


def main() -> None:
    """Entry point for the maze application.

    Reads the config file path from ``sys.argv``, parses it via
    ``parceing.parce``, and launches the interactive :func:`menu`.
    Prints a usage message if the wrong number of arguments is supplied,
    or an error message if parsing or generation fails.
    """
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
