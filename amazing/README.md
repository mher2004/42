*This project has been created as part of the 42 curriculum by mmkrtchy, vpolikha.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and visualizer. Given a configuration file, it generates a random maze — optionally perfect (exactly one path between entry and exit) — renders it in the terminal using colored block characters, and writes the result to an output file in a hexadecimal wall-encoding format. The maze always contains a hidden **"42" pattern** made of fully closed cells (when the maze is large enough), and a shortest-path solver is built in.

**Features:**
- Two generation algorithms: Depth-First Search (recursive backtracker) and Randomized Prim's
- Perfect and imperfect maze modes
- Seed-based reproducibility
- Terminal color customization (white, blue, yellow)
- Show/hide shortest path overlay
- Generation animation mode
- Bonus: algorithm switching at runtime

---

## Instructions

### Installation

```bash
make install
```

This installs all dependencies from `requirements.txt` (pydantic).

### Running

```bash
make run
# or directly:
python3 a_maze_ing.py config.txt
```

### Linting

```bash
make lint          # flake8 + mypy with standard flags
make lint-strict   # flake8 + mypy --strict
```

### Cleaning

```bash
make clean
```
### Debug

```bash
make debug
```
---

## Configuration File Format

The config file uses `KEY=VALUE` pairs, one per line. Lines starting with `#` are comments and are ignored.

| Key           | Required | Description                                 | Example                  |
|---------------|----------|---------------------------------------------|--------------------------|
| `WIDTH`       | Yes      | Maze width in cells (≥ 1)                   | `WIDTH=18`               |
| `HEIGHT`      | Yes      | Maze height in cells (≥ 1)                  | `HEIGHT=10`              |
| `ENTRY`       | Yes      | Entry cell coordinates as `x,y`             | `ENTRY=0,0`              |
| `EXIT`        | Yes      | Exit cell coordinates as `x,y`              | `EXIT=13,9`              |
| `OUTPUT_FILE` | Yes      | Path to write the output maze file          | `OUTPUT_FILE=out.txt`    |
| `PERFECT`     | Yes      | `True` for a perfect maze, `False` otherwise| `PERFECT=True`           |
| `SEED`        | No       | Seed string for reproducibility             | `SEED=asdda`             |
| `COLOR`       | No       | Wall color: `white`, `blue`, or `yellow`    | `COLOR=blue`             |

**Example `config.txt`:**
```
WIDTH=18
HEIGHT=10
ENTRY=0,0
EXIT=13,9
OUTPUT_FILE=out.txt
PERFECT=True
SEED=asdda
COLOR=blue
```

> The "42" pattern is only rendered when `WIDTH ≥ 9` and `HEIGHT ≥ 7`. If the maze is too small, a warning is printed.

---

## Output File Format

Each cell is encoded as a single uppercase hexadecimal digit, where each bit represents a wall:

| Bit | Direction |
|-----|-----------|
| 0   | North |
| 1   | East  |
| 2   | South |
| 3   | West  |

`1` = wall closed, `0` = wall open.

Cells are written row by row, one row per line. After a blank line, three more lines follow: entry coordinates, exit coordinates, and the shortest path expressed as a sequence of `N`, `E`, `S`, `W` steps.

---

## Maze Generation Algorithms

Two algorithms are available and can be switched at runtime (option 5 in the menu):

### Algorithm 0 — Depth-First Search (Recursive Backtracker)
Starting from the entry cell, the generator picks a random unvisited neighbor, removes the wall between them, and recurses. When it hits a dead end it backtracks. This tends to produce mazes with long winding corridors and relatively few dead ends.

**Why we chose it as the default:** DFS is simple to implement correctly, produces visually interesting mazes, and runs efficiently. Its stack-based nature maps cleanly onto the perfect-maze requirement.

### Algorithm 1 — Randomized Prim's
Starting from the entry, the generator maintains a frontier of cells adjacent to the already-visited region. It picks a random frontier cell, connects it to a random visited neighbor, and expands the frontier. This produces mazes with a more uniform texture and more branching than DFS.

---

## Visual Representation

The terminal renderer uses Unicode block characters (`█`) with ANSI color codes. The display shows:

- **Walls** — colored blocks (white / blue / yellow, configurable)
- **Entry** — green block
- **Exit** — red block
- **"42" pattern** — cyan blocks
- **Shortest path** — yellow blocks (toggle with option 2)

### Interactive Menu

| Option | Action |
|--------|--------|
| 1 | Regenerate maze with a new random seed |
| 2 | Show / hide shortest path |
| 3 | Change wall color (white / blue / yellow) |
| 4 | Animate the current generation algorithm |
| 5 | Switch algorithm (DFS ↔ Randomized Prim's) |
| 6 | Exit |

---

## Reusable Module — `mazegen`

The maze generation logic lives entirely in `generator.py` as the `MazeGenerator` class. It has no dependency on the display or config-parsing code and can be imported independently.

### Quick Start

```python
from generator import MazeGenerator

# Create a 20×15 maze with entry at (0,0) and exit at (19,14)
gen = MazeGenerator(width=20, height=15, entry=(0, 0), exit=(19, 14))

# Generate with a fixed seed, DFS algorithm, perfect maze
seed = gen.generator(seed="my_seed", alg=0, perfect=True)

# Access the cell grid
for row in gen.cells:
    for cell in row:
        print(cell.bords, end=" ")  # e.g. "1011" = walls on N, S, W
    print()

# Access the solution (dict mapping (i,j) → parent (i,j) or None for entry)
print(gen.solution)
```

### Custom Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `width` | `int` | Number of columns |
| `height` | `int` | Number of rows |
| `entry` | `tuple[int,int]` | `(x, y)` of the entry cell |
| `exit` | `tuple[int,int]` | `(x, y)` of the exit cell |
| `seed` | `str \| None` | RNG seed; uses `time.time()` if `None` |
| `alg` | `int` | `0` = DFS, `1` = Randomized Prim's |
| `perfect` | `bool` | `True` = single path between entry and exit |
| `is_ft` | `bool` | `True` = embed the "42" pattern |
| `animate` | `bool` | `True` = call `anim_func` each step |

### Accessing the Generated Structure

After calling `generator()`:

- `gen.cells[i][j]` — a `Cell` object with:
  - `bords: str` — 4-character binary string `"NESW"` (`'1'` = wall present)
  - `i, j` — row and column indices
  - `is_entry`, `is_exit`, `is_f2`, `is_visited` — boolean flags
- `gen.solution` — `dict[(i,j), (i,j) | None]` — BFS parent map from entry to exit

### Building the Package

```bash
pip install build
python -m build --outdir .
# produces mazegen-1.0.0-py3-none-any.whl and mazegen-1.0.0.tar.gz
```

Install in any virtualenv:
```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

---

## Resources

### Maze Generation
- [Maze generation algorithm — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Jamis Buck's "Think Labyrinth" — comprehensive algorithm guide](http://www.astrolog.org/labyrnth/algrithm.htm)
- [Prim's algorithm — Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm)

### Python / Libraries
- [Pydantic v2 documentation](https://docs.pydantic.dev/latest/)
- [Python `collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque)
- [ANSI escape codes reference](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [flake8](https://flake8.pycqa.org/) / [mypy](https://mypy.readthedocs.io/)

### AI Usage
Claude (Anthropic) was used for:
- Generating this README from project files and subject requirements.
- Reviewing docstring and type hint completeness.
- Suggesting edge cases to test in the config parser.

All generated content was reviewed, tested, and understood by the team before inclusion.

---

## Team & Project Management

### Roles

| Member | Responsibilities |
|--------|-----------------|
| **mmkrtchy** | Core maze generator (`generator.py`, DFS/RP), BFS solver, Makefile |
| **vpolikha** | Config parser (`parce.py`), terminal renderer (`a_maze_ing.py`), interactive menu, error handling |

### Planning

Initially we planned to deliver the core generator and a basic renderer in the first week, then refine the config parser and add the interactive menu in the second. In practice, aligning the wall-encoding format between the generator and the renderer took longer than expected, and we added the Randomized Prim's algorithm as a bonus toward the end.

### What Worked Well
- Keeping `MazeGenerator` completely decoupled from display code made testing straightforward and satisfies the reusability requirement cleanly.
- Using Pydantic for config validation caught bad inputs early with clear error messages.

### What Could Be Improved
- The `Cell` class is duplicated across `generator.py` and `a_maze_ing.py`; a shared `models.py` (already present but not fully adopted) should be the single source of truth.
- The animation mode blocks the interactive menu loop; a cleaner design would use a separate thread or async approach.

### Tools Used
- **Python 3.10+**, **Pydantic v2**, **mypy**, **flake8**
- **Git** for version control
- **Claude (Anthropic)** for documentation assistance (see AI Usage above)
