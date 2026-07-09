from __future__ import annotations

from board import Board

VALID_SYMBOLS = ("X", "O")


def other_symbol(symbol: str) -> str:
    return "O" if symbol == "X" else "X"


def resolve_symbols(player1_choice: str) -> tuple[str, str]:

    choice = player1_choice.strip().upper()
    if choice not in VALID_SYMBOLS:
        raise ValueError(f"symbol must be one of {VALID_SYMBOLS!r}, got {player1_choice!r}")
    return choice, other_symbol(choice)


def GetSymbolFromUser() -> str:

    while True:
        raw = input("Player 1, choose your symbol (X or O): ").strip().upper()
        if raw in VALID_SYMBOLS:
            return raw
        print("Please type X or O.")


def ask_name(default_label: str) -> str:
    """Ask a player for a display name; fall back to `default_label`
    (e.g. 'Player 1') if they just press Enter instead of typing one.
    """
    raw = input(f"{default_label}, enter your name (or press Enter to use '{default_label}'): ").strip()
    return raw if raw else default_label


def ask_for_move(player_label: str, board: Board) -> int:

    while True:
        raw = input(f"{player_label}, enter a position (1-9): ").strip()

        if not raw.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        position = int(raw) - 1

        if not board.is_valid_move(position):
            print("That spot is taken or out of range — try again.")
            continue

        return position


def play_game() -> None:
    """Run one full game from empty board to a decided result."""
    board = Board()

    player1_name = ask_name("Player 1")
    player1_symbol = GetSymbolFromUser()
    player2_symbol = other_symbol(player1_symbol)
    player2_name = ask_name("Player 2")
    # 'X' always moves first, regardless of which human asked to be
    # 'X' or 'O' — a fixed rule beats an implicit "whoever we asked
    # first" rule, which breaks down as soon as turn order matters.
    label_for_symbol = {
        player1_symbol: f"{player1_name} ({player1_symbol})",
        player2_symbol: f"{player2_name} ({player2_symbol})",
    }
    current_symbol = "X"
    result: str | None = None

    while result is None:
        print("\n" + board.render() + "\n")
        current_label = label_for_symbol[current_symbol]
        position = ask_for_move(current_label, board)
        board.make_move(position, current_symbol)
        result = board.check_winner()
        if result is None:
            current_symbol = other_symbol(current_symbol)

    print("\n" + board.render() + "\n")
    if result == "draw":
        print("It's a draw!")
    else:
        print(f"{label_for_symbol[result]} wins!")





# def GetSymbolFromUser():
#     global User1_Letter
#     global User2_Letter
#     global Current_User
#
#     print("Please Enter the Symbol you wanna use during the game")
#     Letter = input("X or O ? ")
#
#     while(Letter not in "XOE"):
#         print("Please choose only from X or O !! ")
#         print("or Press E to Exit")
#         Letter = input("X or O ? ")
#         if Letter == 'E':
#             exit()
#
#     if Letter == 'X':
#         User1_Letter = 'X'
#         User2_Letter = 'O'
#     else:
#         User2_Letter = 'X'
#         User1_Letter = 'O'
