from __future__ import annotations

EMPTY = ""

WINNING_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
)

class Board:

    def __init__(self) -> None:
        self.cells: list[str] = [EMPTY] * 9
        self.winning_line: tuple[int, int, int] | None = None

    def is_valid_move(self, position: int) -> bool:
        return 0 <= position <= 8 and self.cells[position] == EMPTY

    def make_move(self, position: int, symbol: str) -> None:
        self.cells[position] = symbol

    def undo_move(self, position: int) -> None:
        self.cells[position] = EMPTY

    def empty_positions(self) -> list[int]:
        return [i for i, cell in enumerate(self.cells) if cell == EMPTY]

    def check_winner(self) -> str | None:
        self.winning_line = None

        for line in WINNING_LINES:
            a, b, c = line
            if self.cells[a] != EMPTY and self.cells[a] == self.cells[b] == self.cells[c]:
                self.winning_line = line
                return self.cells[a]

        if EMPTY not in self.cells:
            return "draw"

        return None

    def render(self) -> str:
        """Build a human-readable string of the board.

        Empty cells show their 1-9 position number instead of a blank,
        so a player always sees exactly which digit to type next —
        this doubles as the "which moves are still open" display, so
        there's no separate function needed just to list open spots.
        If `check_winner()` has already found a win, the three winning
        cells are wrapped in asterisks, e.g.:

             *X*| *X*| *X*
            ---+---+---
             4 | O | 6
            ---+---+---
             O | 8 | 9
        """
        display_cells = []
        for i, cell in enumerate(self.cells):
            label = cell if cell != EMPTY else str(i + 1)
            if self.winning_line and i in self.winning_line:
                label = f"*{label}*"
            display_cells.append(label)

        rows = []
        for r in range(3):
            row_cells = display_cells[r * 3:(r + 1) * 3]
            rows.append(" " + " | ".join(row_cells) + " ")
        return "\n---+---+---\n".join(rows)

